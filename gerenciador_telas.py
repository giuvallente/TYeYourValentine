# classe que irá gerenciar as telas do jogo
from .tela_inicial import Tela_inicial
import pygame

class Gerenciador_Telas():
    """
    Classe utilizada para gerenciar qual tela deverá ser desenhada em seguida. 
    """
    def __init__(self, window):
        self.window = window
        self.tela = Tela_inicial()
    
    def game_loop(self):
        """
        Método que contém o loop principal do jogo.
        """
        # loop que desenha cada tela enquanto o jogo for True
        jogo = True

        while jogo:
            jogo = self.tela_update()
            self.desenha()

    def tela_update(self):
        """
        Método que atualiza a tela do jogo de acordo com o estado atual.
        """
        # updata a tela que será desenhada
        proxima_tela = self.tela.atualiza_estado()
        if proxima_tela == -1:
            return False
        if proxima_tela == 'TELA_INICIAL':
            self.tela = Tela_inicial()
        return True

    def desenha(self):
        """
        Método que desenha a tela do jogo.
        """
        # irá desenhar a tela settada como 'self.tela'
        self.tela.desenha(self.window)
        pygame.display.update()