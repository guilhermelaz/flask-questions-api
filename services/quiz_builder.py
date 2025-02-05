from classes.quiz import Quiz
import random

# Adicionar opções de limitar quantidade de perguntas
# Adicionar opção de embaralhar perguntas
# Em vez de embaralhar por padrão, embaralhar no builder

class QuizBuilder:
    def __init__(self):
        self.quiz = Quiz()
        self.max_perguntas = None
        self.embaralhar = False

    def set_dificuldade(self, dificuldade):
        self.quiz.dificuldade = dificuldade
        return self

    def set_max_perguntas(self, quantidade):
        self.max_perguntas = quantidade
        return self

    def set_embaralhar(self, embaralhar=True):
        self.embaralhar = embaralhar
        return self

    def adicionar_perguntas(self, perguntas):
        perguntas = list(perguntas)
        
        if self.embaralhar:
            random.shuffle(perguntas)
        
        if self.max_perguntas and len(perguntas) > self.max_perguntas:
            perguntas = perguntas[:self.max_perguntas]
        
        for pergunta in perguntas:
            pergunta.embaralhar_alternativas()
            self.quiz.adicionar_pergunta(pergunta)
            
        return self

    def build(self):
        return self.quiz
