import sys
sys.path.append('../const.py')
import pygame.mixer

from components.Button import HandleButton
from const import FONDO_PLAYING1, SCREEN_WIDTH, SCREEN_HEIGHT
from configuration import SoundManager

sound_manager = SoundManager()

class PlayingState:
    def __init__(self, game, configuration):
        self.game = game
        self.configuration = configuration
        self.configuration.register_observer(self)

        self.sound_menu = sound_manager
        self.background = FONDO_PLAYING1(self.game.pygame)
        self.background_width = self.background.get_width()
        self.background_height = self.background.get_height()
        self.background_x = 0
        self.background_y = 0
        self.x_relative = 0

        self.keys = self.game.pygame.key.get_pressed()


        if(self.configuration.sound_enabled):
            self.sound_menu.load_sound('menu-sound', 'assets/sounds/playing_theme.mp3')
            self.sound_menu.play_sound('menu-sound', -1)

       

    def handle_events(self, events):
        self.keys = self.game.pygame.key.get_pressed()
        for event in events:
            if event.type == self.game.pygame.KEYDOWN:
                pass
                # if event.key == self.game.pygame.K_SPACE:
                #     self.game.change_state("playing")  

       

    def configuration_changed(self):
        pass

    def update(self):
        pass

    def render(self):
        self.game.screen.fill((0,0,0))
        self.x_relative = self.background_x % self.background_width
        self.game.screen.blit(self.background, (self.x_relative - self.background_width, self.background_y))

        if self.keys[self.configuration.move_left]:
            self.background_x += 3
        if self.keys[self.configuration.move_right]:
            self.background_x -= 3
        
        if(self.x_relative < SCREEN_WIDTH(self.game.pygame)):
            self.game.screen.blit(self.background, (self.x_relative, self.background_y))




    def cleanup(self):
        self.sound_menu.stop_sound('menu-sound')
        self.sound_menu.unload_sound('menu-sound')