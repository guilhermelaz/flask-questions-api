from abc import ABC, abstractmethod
import random
from datetime import datetime

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

    @abstractmethod
    def calcular_pontuacao(self, respostas_corretas, dificuldade, tempo_total=None):
        pass

class QuizFacilStrategy(QuizStrategy):
    def selecionar_perguntas(self, todas_perguntas, quantidade=5):
        perguntas_faceis = [p for p in todas_perguntas if p.dificuldade.lower() == 'fácil']
        if len(perguntas_faceis) < quantidade:
            quantidade = len(perguntas_faceis)
        return random.sample(perguntas_faceis, quantidade) if perguntas_faceis else []

    def calcular_pontuacao(self, respostas_corretas, dificuldade, tempo_total=None):
        pontos_base = respostas_corretas * 10
        return pontos_base

class QuizMedioStrategy(QuizStrategy):
    def selecionar_perguntas(self, todas_perguntas, quantidade=5):
        perguntas_medias = [p for p in todas_perguntas if p.dificuldade.lower() == 'médio']
        if len(perguntas_medias) < quantidade:
            quantidade = len(perguntas_medias)
        return random.sample(perguntas_medias, quantidade) if perguntas_medias else []

    def calcular_pontuacao(self, respostas_corretas, dificuldade, tempo_total=None):
        pontos_base = respostas_corretas * 20
        return pontos_base

class QuizDificilStrategy(QuizStrategy):
    def selecionar_perguntas(self, todas_perguntas, quantidade=5):
        perguntas_dificeis = [p for p in todas_perguntas if p.dificuldade.lower() == 'difícil']
        if len(perguntas_dificeis) < quantidade:
            quantidade = len(perguntas_dificeis)
        return random.sample(perguntas_dificeis, quantidade) if perguntas_dificeis else []

    def calcular_pontuacao(self, respostas_corretas, dificuldade, tempo_total=None):
        pontos_base = respostas_corretas * 30
        return pontos_base

class QuizMistoStrategy(QuizStrategy):
    def selecionar_perguntas(self, todas_perguntas, quantidade=5):
        if len(todas_perguntas) < quantidade:
            quantidade = len(todas_perguntas)
        return random.sample(todas_perguntas, quantidade) if todas_perguntas else []

    def calcular_pontuacao(self, respostas_corretas, dificuldade, tempo_total=None):
        pontos_por_dificuldade = {
            'fácil': 10,
            'médio': 20,
            'difícil': 30
        }
        return respostas_corretas * pontos_por_dificuldade.get(dificuldade.lower(), 20)

# Template Method
class GameModeStrategy(ABC):
    @abstractmethod
    def iniciar_quiz(self):
        pass

    @abstractmethod
    def finalizar_quiz(self, tempo_inicio=None):
        pass

# Concrete Strategy implementado com o template
#Tempo
class TimedModeStrategy(GameModeStrategy):
    def iniciar_quiz(self):
        return datetime.now()

    def finalizar_quiz(self, tempo_inicio):
        if tempo_inicio:
            tempo_total = (datetime.now() - tempo_inicio).total_seconds()
            return tempo_total
        return None

# Sem tempo
class UntimedModeStrategy(GameModeStrategy):
    def iniciar_quiz(self):
        return None

    def finalizar_quiz(self, tempo_inicio=None):
        return None
