import sys
import pygame
from settings import Settings 
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Classe geral para gerenciar ativos e comportamento do jogo."""

    def __init__(self):
        """Inicializa o jogo e cria recursos do jogo."""
        pygame.init()
        self.clock = pygame.time.Clock() # Inicializa o relógio do Pygame
        self.settings = Settings()
        # Configura a janela do jogo para o modo fullscreen.
        # 0,0 indica que o Pygame deve usar a resolução nativa do monitor
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # get_rect() retorna um objeto Rect que representa as dimensões da tela
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        #  Cria uma nova janela de jogo com a largura e altura especificadas
        #self.screen = pygame.display.set_mode(
         #   (self.settings.screen_width, self.settings.screen_height))
        
        # Define o título da janela do jogo
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self) # Passa a instância atual de AlienInvasion para Ship
        self.bullets = pygame.sprite.Group() # grupo que armazena projéteis


    def run_game(self):
        """Inicia o loop principal do jogo."""
        while True:
            self._check_events()
            self.ship.update() # Atualiza a posição da espaçonave
            self._update_bullets()
            self._update_screen() # Redesenha a tela do jogo
            # Controla a taxa de frames
            self.clock.tick(60) # Limita a 60 frames por segundo

    def _check_events(self):
        """Responde as teclas pressionadas e a eventos de mouse."""
        # verifica se o tipo de evento é pygame.QUIT, para sair do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: # detecta tecla pressionada
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responde a teclas pressionadas"""
        if event.key == pygame.K_RIGHT: # tecla ->
            # Move a espaçonave para a direita
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):        
        """Responde a teclas soltas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self): # É chamado ao apertar espaço
        """Cria um novo projétil e o adiciona ao grupo projéteis."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Atualiza a posição dos projéteis e descarta os projéteis antigos."""
        # Atualiza a posição dos projéteis
        self.bullets.update()

        # Descarta os projéteis que desaparecem na tela
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _update_screen(self):
        # Atualiza as imagens na tela e muda para a nova tela
        self.screen.fill(self.settings.bg_color)

        # retorna uma lista de todos os sprites na lista bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.ship.blitme() # Desenha a espaçonave
        # Deixa a tela desenhada mais recente visível
        pygame.display.flip()

if __name__ == '__main__':
    # Cria uma instância do jogo e execute o jogo.
    ai = AlienInvasion()
    ai.run_game()