class Quiz:
    def __init__(self):
        self.perguntas = []
        self.dificuldade = None
        self.pontuacao = 0

    def adicionar_pergunta(self, pergunta):
        self.perguntas.append(pergunta)

    def set_dificuldade(self, dificuldade):
        self.dificuldade = dificuldade
