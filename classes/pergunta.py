class Pergunta:
    def __init__(self, pergunta: str, tema: str, alternativas: list, resposta_correta: str, dificuldade: str):
        self.texto = pergunta 
        self.tema = tema
        self.alternativas = alternativas.copy()  # Faz uma cópia para não modificar a lista original
        self.resposta_correta = resposta_correta
        self.dificuldade = dificuldade
        
    def embaralhar_alternativas(self):
        import random
        # Cria uma cópia das alternativas para embaralhar
        alternativas = self.alternativas.copy()
        # Embaralha as alternativas
        random.shuffle(alternativas)
        # Atualiza as alternativas embaralhadas
        self.alternativas = alternativas
