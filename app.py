# app.py
# Usando Flask
# Import das perguntas do arquivo json usando padrão Factory, mapeando o json para objetos da classe pergunta.
# usar strategy e builder pra construir o quiz, com base na dificuldade das perguntas: Fácil, Médio, Difícil, Misto.
# Criar packages/diretórios: classes, services.

# Ou seja: O quiz será construido com base na seleção na tela inicial, onde pedirá a dificuldade. De acordo com a dificuldade, o strategy referente é chamado...
# Tudo tem que estar bem separadinho pois é um trabalho e precisa ser simples de entender.

from flask import Flask, render_template, request, jsonify
from services.pergunta_factory import PerguntaFactory
from services.quiz_builder import QuizBuilder
from services.quiz_strategy import (
    QuizFacilStrategy,
    QuizMedioStrategy,
    QuizDificilStrategy,
    QuizMistoStrategy
)

app = Flask(__name__)

factory = PerguntaFactory()
todas_perguntas = factory.criar_perguntas_do_json('perguntas.json')


estrategias = {
    'facil': QuizFacilStrategy(),
    'medio': QuizMedioStrategy(),
    'dificil': QuizDificilStrategy(),
    'misto': QuizMistoStrategy()
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/criar_quiz', methods=['POST'])
def criar_quiz():
    dificuldade = request.form.get('dificuldade', 'facil')
    
    # Seleciona a estratégia apropriada
    estrategia = estrategias.get(dificuldade)
    if not estrategia:
        return jsonify({'erro': 'Dificuldade inválida'}), 400
    
    # Seleciona as perguntas usando a estratégia
    perguntas_selecionadas = estrategia.selecionar_perguntas(todas_perguntas)
    
    # Constrói o quiz usando o builder
    quiz = QuizBuilder()\
        .set_dificuldade(dificuldade)\
        .adicionar_perguntas(perguntas_selecionadas)\
        .build()
    
    # Converte as perguntas para formato JSON
    perguntas_json = [
        {
            'texto': p.texto,
            'tema': p.tema,
            'alternativas': p.alternativas,
            'dificuldade': p.dificuldade,
            'resposta_correta': p.resposta_correta
        }
        for p in quiz.perguntas
    ]
    
    return jsonify(perguntas_json)

if __name__ == '__main__':
    app.run(debug=True)
