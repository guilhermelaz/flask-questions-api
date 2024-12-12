from classes.quiz import Quiz

# Adicionar opções de limitar quantidade de perguntas
# Adicionar opção de embaralhar perguntas
# Em vez de embaralhar por padrão, embaralhar no builder

class QuizBuilder:
    def __init__(self):
        self.quiz = Quiz()

    def set_dificuldade(self, dificuldade):
        self.quiz.dificuldade = dificuldade
        return self

    def adicionar_perguntas(self, perguntas):
        for pergunta in perguntas:
            self.quiz.adicionar_pergunta(pergunta)
        return self

    def build(self):
        return self.quiz

