import pygame
import sys
sys.path.append('../const.py')

from components.Button import HandleButton
from const import FONDO_OPTIONS, SCREEN_WIDTH, SCREEN_HEIGHT
from configuration import SoundManager

sound_manager = SoundManager()



class OptionsState:
    def __init__(self, game, configuration):
        self.game = game
        self.configuration = configuration
        self.configuration.register_observer(self)
        self.sound_menu = sound_manager

        if(self.configuration.sound_enabled):
            self.button_sound = HandleButton('assets/btn_sound_on.png', pygame, sound_manager, 'assets/sounds/button-click.mp3', 'button-sound')
            self.sound_menu.load_sound('menu-sound', 'assets/sounds/options_screen.mp3')
            self.sound_menu.play_sound('menu-sound', -1)
        else:
            self.button_sound = HandleButton('assets/btn_sound_off.png', pygame, sound_manager, 'assets/sounds/button-click.mp3', 'button-sound')
            self.sound_menu.stop_sound('menu-sound')
            self.sound_menu.unload_sound('menu-sound')

       
        
        self.button_back = HandleButton('assets/btn_back.png', pygame, sound_manager, 'assets/sounds/button-click.mp3', 'button-back')
        
        
        

        self.gap_y = 20

       

    def update(self, fps):
        pass

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.change_state("menu")

            if self.button_sound.handle_event(event, self.configuration.sound_enabled):
                self.set_sound_enabled(not self.configuration.sound_enabled)
           
            if self.button_back.handle_event(event, self.configuration.sound_enabled):
                self.game.change_state("menu")
         
    def set_sound_enabled(self, enabled):
        self.configuration.set_sound_enabled(enabled)

    def configuration_changed(self):
        if self.configuration.sound_enabled:
            self.cleanup()
            self.button_sound = HandleButton('assets/btn_sound_on.png', pygame, sound_manager, 'assets/sounds/button-click.mp3', 'button-sound')
            self.sound_menu.load_sound('menu-sound', 'assets/sounds/options_screen.mp3')
            self.sound_menu.play_sound('menu-sound')
        else:
            self.button_sound = HandleButton('assets/btn_sound_off.png', pygame, sound_manager, 'assets/sounds/button-click.mp3', 'button-sound')
            self.sound_menu.stop_sound('menu-sound')
            self.sound_menu.unload_sound('menu-sound')

    def update_sound_enabled(self, enabled):
        self.configuration.set_sound_enabled(enabled)

    def update_jump_key(self, key):
        self.configuration.set_jump_key(key)

    def update_move_key(self, key):
        self.configuration.set_move_key(key)

    def render(self):
        self.game.screen.blit(FONDO_OPTIONS(pygame), (0, 0))

        button_sound_x = (SCREEN_WIDTH(pygame) // 2) - (self.button_sound.width // 2)
        button_sound_y = (SCREEN_HEIGHT(pygame) // 2) - (self.button_sound.height // 2)
        self.button_sound.render(self.game.screen, button_sound_x, button_sound_y)

        button_back_x = 100
        button_back_y = 100
        self.button_back.render(self.game.screen, button_back_x, button_back_y)

       

        pygame.display.flip()

    def cleanup(self):
        self.sound_menu.stop_sound('menu-sound')
        self.sound_menu.unload_sound('menu-sound')

     