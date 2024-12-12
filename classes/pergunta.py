class Pergunta:
    def __init__(self, pergunta: str, tema: str, alternativas: list, resposta_correta: str, dificuldade: str):
        self.texto = pergunta 
        self.tema = tema
        self.alternativas = alternativas
        self.resposta_correta = resposta_correta
        self.dificuldade = dificuldade
