from abc import ABC, abstractmethod
from services.quiz_strategy import GameModeStrategy, UntimedModeStrategy

class QuizTemplate(ABC):
    def __init__(self):
        self.game_mode: GameModeStrategy = UntimedModeStrategy()
        self.tempo_inicio = None
        self.perguntas = []
        self.respostas = []
        self.pontuacao = 0

    def executar_quiz(self):
        """Template method que define o algoritmo do quiz"""
        self.carregar_perguntas()
        self.iniciar_modo_jogo()
        self.apresentar_perguntas()
        self.finalizar_modo_jogo()
        self.calcular_resultado()
        return self.pontuacao

    @abstractmethod
    def carregar_perguntas(self):
        """Método abstrato para carregar perguntas"""
        pass

    def iniciar_modo_jogo(self):
        """Hook method que pode ser sobrescrito"""
        self.tempo_inicio = self.game_mode.iniciar_quiz()

    @abstractmethod
    def apresentar_perguntas(self):
        """Método abstrato para apresentar perguntas"""
        pass

    def finalizar_modo_jogo(self):
        """Hook method que pode ser sobrescrito"""
        return self.game_mode.finalizar_quiz(self.tempo_inicio)

    @abstractmethod
    def calcular_resultado(self):
        """Método abstrato para calcular o resultado"""
        pass

class QuizPadrao(QuizTemplate):
    def __init__(self, strategy, perguntas):
        super().__init__()
        self.strategy = strategy
        self.todas_perguntas = perguntas
        self.respostas_corretas = 0

    def carregar_perguntas(self):
        self.perguntas = self.strategy.selecionar_perguntas(self.todas_perguntas)

    def apresentar_perguntas(self):
        # Esse está no WEB
        pass

    def calcular_resultado(self):
        tempo_total = self.finalizar_modo_jogo()
        self.pontuacao = self.strategy.calcular_pontuacao(
            self.respostas_corretas,
            self.perguntas[0].dificuldade if self.perguntas else 'médio',
            tempo_total
        )
