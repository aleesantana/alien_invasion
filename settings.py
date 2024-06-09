class Settings:
    """Classe para armazenar as configurações do Jogo Invasão Alienígena."""

    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configurações da espaçonave
        self.ship_speed = 1.5 # Define que a posição da espaçonave se ajusta
                              # em 1.5 pixels em cada passagem do loop. O padrão
                              # é 1 pixel.        