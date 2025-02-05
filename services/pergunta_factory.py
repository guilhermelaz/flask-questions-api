import json
from classes.pergunta import Pergunta

# 1: Factory

# Tirar o _instance (tirar o singleton)
# Deixar o método de criar perguntas estático

class PerguntaFactory:
    @staticmethod
    def criar_perguntas_do_json(arquivo_json):
        perguntas = []
        with open(arquivo_json, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            for item in dados:
                pergunta = Pergunta(
                    pergunta=item['pergunta'],
                    tema=item['tema'],
                    alternativas=item['alternativas'],
                    resposta_correta=item['resposta_correta'],
                    dificuldade=item['dificuldade']
                )
                perguntas.append(pergunta)
        return perguntas
