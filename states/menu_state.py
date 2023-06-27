import pygame
import sys
sys.path.append('../const.py')
import pygame.mixer

from components.Button import HandleButton
from const import FONDO_MENU, SCREEN_WIDTH, SCREEN_HEIGHT
from configuration import SoundManager

sound_manager = SoundManager()

class MenuState:
    def __init__(self, game, configuration):
        self.game = game
        self.configuration = configuration
        self.configuration.register_observer(self)

        self.sound_menu = sound_manager
        self.button_play = HandleButton('assets/btn_start.png', pygame, sound_manager, 'assets/sounds/start_button.mp3', 'button-play')
        self.button_options = HandleButton('assets/btn_options.png', pygame, sound_manager, 'assets/sounds/button-click.mp3', 'button-options')
        self.button_exit = HandleButton('assets/btn_exit.png', pygame, sound_manager, 'assets/sounds/button-click.mp3', 'button-exit')

        if(self.configuration.sound_enabled):
            self.sound_menu.load_sound('menu-sound', 'assets/sounds/life-and-technology.mp3')
            self.sound_menu.play_sound('menu-sound', -1)

        self.gap_y = 20

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.change_state("playing")

            if self.button_play.handle_event(event, self.configuration.sound_enabled):
                self.game.change_state("playing")
            if self.button_options.handle_event(event, self.configuration.sound_enabled):
                self.game.change_state("options")
            if self.button_exit.handle_event(event, self.configuration.sound_enabled):
                self.game.change_state("exit")
    
    
    def configuration_changed(self):
        pass

    def update(self, fps):
        pass

    def render(self):
        self.game.screen.blit(FONDO_MENU(pygame), (0, 0))

        button_play_x = (SCREEN_WIDTH(pygame) // 2) - (self.button_play.width // 2)
        button_play_y = (SCREEN_HEIGHT(pygame) // 2) - (self.button_play.height // 2)
        self.button_play.render(self.game.screen, button_play_x, button_play_y)

        button_options_x = (SCREEN_WIDTH(pygame) // 2) - (self.button_options.width // 2)
        button_options_y = (SCREEN_HEIGHT(pygame) // 2) - (self.button_options.height // 2) + (self.button_play.height // 2) + self.gap_y
        self.button_options.render(self.game.screen, button_options_x, button_options_y)

        button_exit_x = (SCREEN_WIDTH(pygame) // 2) - (self.button_exit.width // 2)
        button_exit_y = (SCREEN_HEIGHT(pygame) // 2) - (self.button_exit.height // 2) + ((self.button_play.height // 2) + (self.button_options.height // 2)) + self.gap_y
        self.button_exit.render(self.game.screen, button_exit_x, button_exit_y)

        pygame.display.flip()

    def cleanup(self):
        self.sound_menu.stop_sound('menu-sound')
        self.sound_menu.unload_sound('menu-sound')