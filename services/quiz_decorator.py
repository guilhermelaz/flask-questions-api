from abc import ABC, abstractmethod
from datetime import datetime

class QuizDecorator(ABC):
    def __init__(self, quiz):
        self._quiz = quiz

    @abstractmethod
    def calcular_pontuacao(self, respostas_corretas, dificuldade, tempo_total=None):
        pass

class TimeMultiplierDecorator(QuizDecorator):
    def calcular_pontuacao(self, respostas_corretas, dificuldade, tempo_total=None):
        pontuacao_base = self._quiz.calcular_pontuacao(respostas_corretas, dificuldade, tempo_total)
        
        if tempo_total is None:
            return pontuacao_base
            
        # Bônus por velocidade (quanto mais rápido, maior o multiplicador)
        if tempo_total < 30:  # Menos de 30 segundos
            return pontuacao_base * 1.5
        elif tempo_total < 60:  # Menos de 1 minuto
            return pontuacao_base * 1.25
        else:
            return pontuacao_base

class DifficultyMultiplierDecorator(QuizDecorator):
    def calcular_pontuacao(self, respostas_corretas, dificuldade, tempo_total=None):
        pontuacao_base = self._quiz.calcular_pontuacao(respostas_corretas, dificuldade, tempo_total)
        
        # Multiplicador baseado na dificuldade
        multiplicadores = {
            'fácil': 1.0,
            'médio': 1.2,
            'difícil': 1.5
        }
        
        return pontuacao_base * multiplicadores.get(dificuldade.lower(), 1.0)

class ConsecutiveCorrectDecorator(QuizDecorator):
    def calcular_pontuacao(self, respostas_corretas, dificuldade, tempo_total=None):
        pontuacao_base = self._quiz.calcular_pontuacao(respostas_corretas, dificuldade, tempo_total)
        
        # Bônus por respostas consecutivas corretas
        if respostas_corretas >= 5:  # Todas as 5 perguntas corretas
            return pontuacao_base * 2.0
        elif respostas_corretas >= 3:  # 3 ou mais perguntas corretas
            return pontuacao_base * 1.5
            
        return pontuacao_base
