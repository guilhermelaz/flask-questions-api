from flask import Flask, render_template, request, jsonify
from services.pergunta_factory import PerguntaFactory
from services.quiz_builder import QuizBuilder
from services.quiz_strategy import (
    QuizFacilStrategy,
    QuizMedioStrategy,
    QuizDificilStrategy,
    QuizMistoStrategy,
    TimedModeStrategy,
    UntimedModeStrategy
)
from services.quiz_template import QuizPadrao
from services.quiz_decorator import (
    TimeMultiplierDecorator,
    DifficultyMultiplierDecorator,
    ConsecutiveCorrectDecorator
)
import random

app = Flask(__name__)

# Utilizando o Factory para carregar as perguntas em memória
todas_perguntas = PerguntaFactory.criar_perguntas_do_json('perguntas.json')

# Strategies de dificuldade
estrategias = {
    'facil': QuizFacilStrategy(),
    'medio': QuizMedioStrategy(),
    'dificil': QuizDificilStrategy(),
    'misto': QuizMistoStrategy()
}

perguntas_atuais = []
dificuldade_atual = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/criar_quiz', methods=['POST'])
def criar_quiz():
    dificuldade = request.form.get('dificuldade', 'facil')
    modo_jogo = request.form.get('modo', 'sem_tempo')
    max_perguntas = int(request.form.get('max_perguntas', 5))
    embaralhar = request.form.get('embaralhar', 'false').lower() == 'true'
    
    # Select Strategy (Context)
    estrategia = estrategias.get(dificuldade)
    if not estrategia:
        return jsonify({'erro': 'Dificuldade inválida'}), 400
    
    # Carrega todas as perguntas primeiro usando o método estático da factory
    todas_perguntas = PerguntaFactory.criar_perguntas_do_json('perguntas.json')
    
    # Cria o quiz usando builder
    quiz = (
        QuizBuilder()
        .set_dificuldade(dificuldade)
        .set_max_perguntas(max_perguntas)
        .set_embaralhar(embaralhar)
        .adicionar_perguntas(todas_perguntas)
        .build()
    )
    
    # Enviar pro Index
    perguntas_json = []
    for p in quiz.perguntas:
        perguntas_json.append({
            'texto': p.texto,
            'alternativas': p.alternativas,
            'resposta_correta': p.alternativas.index(p.resposta_correta)
        })
    
    global perguntas_atuais, dificuldade_atual
    perguntas_atuais = quiz.perguntas
    dificuldade_atual = dificuldade
    
    return jsonify({
        'perguntas': perguntas_json,
        'modo': modo_jogo,
        'dificuldade': dificuldade
    })

@app.route('/submeter_resposta', methods=['POST'])
def submeter_resposta():
    data = request.get_json()
    respostas_usuario = data.get('respostas', [])
    tempo = data.get('tempo')
    
    # Conta respostas corretas
    respostas_corretas = 0
    for i, resposta in enumerate(respostas_usuario):
        if resposta is not None and i < len(perguntas_atuais):
            pergunta = perguntas_atuais[i]
            if pergunta.alternativas[resposta] == pergunta.resposta_correta:
                respostas_corretas += 1
    
    # Aplicanndo DECORATORS na estratégia para calcular
    estrategia_base = estrategias[dificuldade_atual]
    estrategia_decorada = TimeMultiplierDecorator(
        DifficultyMultiplierDecorator(
            ConsecutiveCorrectDecorator(estrategia_base)
        )
    )
    
    pontuacao = estrategia_decorada.calcular_pontuacao(
        respostas_corretas,
        dificuldade_atual,
        tempo
    )
    
    return jsonify({
        'status': 'success',
        'pontuacao': pontuacao,
        'respostas_corretas': respostas_corretas
    })

if __name__ == '__main__':
    app.run(debug=True)
