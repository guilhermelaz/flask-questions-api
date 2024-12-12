import json
from classes.pergunta import Pergunta

# 1: Factory

# Tirar o _instance (tirar o singleton)
# Deixar o método de criar perguntas estático

class PerguntaFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.perguntas = []
            self.initialized = True

    def criar_perguntas_do_json(self, arquivo_json):
        if not self.perguntas:  # Só carrega se ainda não tiver carregado
            with open(arquivo_json, 'r', encoding='utf-8') as file:
                dados = json.load(file)
                for item in dados:
                    pergunta = Pergunta(
                        pergunta=item['pergunta'],
                        tema=item['tema'],
                        alternativas=item['alternativas'],
                        resposta_correta=item['resposta_correta'],
                        dificuldade=item['dificuldade']
                    )
                    self.perguntas.append(pergunta)
        return self.perguntas


