
class Settings():
    '''Uma classe para armazenar tadas as configurações da Invasão Alienígena.'''

    def __init__(self):
        """Incializando as configurações do jogo."""
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 680
        self.bg_color = (255, 255, 255)

        #Configurações dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0


        # Configuração da espaçonave
        self.ship_speed_factor = 1.5
