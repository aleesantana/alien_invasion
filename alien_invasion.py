import sys
import pygame
from settings import Settings 
from ship import Ship

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamento do jogo."""

    def __init__(self):
        """Inicializa o jogo e cria recursos do jogo."""
        pygame.init()
        self.clock = pygame.time.Clock() # Inicializa o relógio do Pygame
        self.settings = Settings()

        #  Cria uma nova janela de jogo com a largura e altura especificadas
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        # Define o título da janela do jogo
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Inicia o loop principal do jogo."""
        while True:
            self._check_events()
            self._update_screen()
            # Controla a taxa de frames
            self.clock.tick(60) # Limita a 60 frames por segundo

    def _check_events(self):
        """Responde as teclas pressionadas e a eventos de mouse."""
        # verifica se o tipo de evento é pygame.QUIT, para sair do jogo
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        # Atualiza as imagens na tela e muda para a nova tela
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme() # Desenha a espaçonave

    # Deixa a tela desenhada mais recente visível
    pygame.display.flip()

if __name__ == '__main__':
    # Cria uma instância do jogo e execute o jogo.
    ai = AlienInvasion()
    ai.run_game()