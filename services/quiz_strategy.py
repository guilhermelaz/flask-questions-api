from abc import ABC, abstractmethod
import random

# Strategy
# 2 tipos de jogos - Com tempo, sem tempo
# Calcular quanto ele tirou no final com base na dificuldade do quiz. com base na dificuldade

# Template - Carregar, Layout, 
# Carregar, apresentar, corrigir
# Carregarm apresentar, abstrata - corrigir (estratégia)

class QuizStrategy(ABC):
    @abstractmethod
    def selecionar_perguntas(self, todas_perguntas, quantidade=5):
        pass

class QuizFacilStrategy(QuizStrategy):
    def selecionar_perguntas(self, todas_perguntas, quantidade=5):
        perguntas_faceis = [p for p in todas_perguntas if p.dificuldade.lower() == 'fácil']
        if len(perguntas_faceis) < quantidade:
            quantidade = len(perguntas_faceis)
        return random.sample(perguntas_faceis, quantidade) if perguntas_faceis else []

class QuizMedioStrategy(QuizStrategy):
    def selecionar_perguntas(self, todas_perguntas, quantidade=5):
        perguntas_medias = [p for p in todas_perguntas if p.dificuldade.lower() == 'médio']
        if len(perguntas_medias) < quantidade:
            quantidade = len(perguntas_medias)
        return random.sample(perguntas_medias, quantidade) if perguntas_medias else []

class QuizDificilStrategy(QuizStrategy):
    def selecionar_perguntas(self, todas_perguntas, quantidade=5):
        perguntas_dificeis = [p for p in todas_perguntas if p.dificuldade.lower() == 'difícil']
        if len(perguntas_dificeis) < quantidade:
            quantidade = len(perguntas_dificeis)
        return random.sample(perguntas_dificeis, quantidade) if perguntas_dificeis else []

class QuizMistoStrategy(QuizStrategy):
    def selecionar_perguntas(self, todas_perguntas, quantidade=5):
        if len(todas_perguntas) < quantidade:
            quantidade = len(todas_perguntas)
        return random.sample(todas_perguntas, quantidade) if todas_perguntas else []
