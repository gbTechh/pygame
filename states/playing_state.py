import sys
sys.path.append('../const.py')
import pygame.mixer

from components.Button import HandleButton
from const import FONDO_PLAYING1, SCREEN_WIDTH, SCREEN_HEIGHT
from configuration import SoundManager
from entities.Character import Character
from entities.FactoryEntity import CharacterFactory


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


        #Character
        self.character_factory = CharacterFactory()
        self.character = self.character_factory.create_character("sword", self.configuration.speed_character)
        self.K_move_right = self.configuration.move_right
        self.K_move_left = self.configuration.move_left
        self.K_jump = self.configuration.jump_key

        self.right_is_pressed = False
        self.left_is_pressed = False
        self.right_is_unpressed = True
        self.left_is_unpressed = True
        self.jump_is_pressed = False
        self.jump_is_unpressed = True

        self.position_character = 0

    def handle_events(self, events):
        self.keys = self.game.pygame.key.get_pressed()
        for event in events:
            if event.type == self.game.pygame.KEYDOWN:
                if event.key == self.configuration.sound_enabled:
                    self.configuration.sound_enabled
                if event.key == self.K_move_right:
                    self.right_is_pressed = True
                    self.left_is_pressed = False
                    self.left_is_unpressed = False
                    
                    
                if event.key == self.K_move_left:
                    self.left_is_pressed = True
                    self.right_is_pressed = False 
                    self.right_is_unpressed = False 
                   
                if event.key == self.K_jump:
                    self.jump_is_pressed = True 
                    self.jump_is_unpressed = False
                 

            if event.type == self.game.pygame.KEYUP:
                if event.key == self.K_move_right:
                    self.right_is_pressed = False 
                    self.right_is_unpressed = True 
                if event.key == self.K_move_left:
                    self.left_is_pressed = False 
                    self.left_is_unpressed = True 
                if event.key == self.K_jump:
                    self.jump_is_pressed = False
                    self.jump_is_unpressed = True
                    # self.character.update_jumping(False)
                    

       

    def configuration_changed(self):
        pass

    def update(self):
        pass

    def render(self):
        self.game.screen.fill((0,0,0))
        self.x_relative = self.background_x % self.background_width
        self.game.screen.blit(self.background, (self.x_relative - self.background_width, self.background_y))

        self.position_character = self.character.get_character_x_position()

        if self.keys[self.configuration.move_left]:
            if self.position_character <= 200:
                self.background_x += 3

        if self.keys[self.configuration.move_right]:
            if self.position_character >= (SCREEN_WIDTH(pygame) // 2):
                self.background_x -= 3
        
        if(self.x_relative < SCREEN_WIDTH(self.game.pygame)):
            self.game.screen.blit(self.background, (self.x_relative, self.background_y))

        #render character
        if self.left_is_pressed:
            self.character.start_movement("left")
            self.character.movementCharacter(self.game.delta_time)  

            if self.jump_is_pressed:
                self.character.start_movement("jump", 'left')
                self.character.movementCharacter(self.game.delta_time)

        elif self.right_is_pressed:
            self.character.start_movement("right")
            self.character.movementCharacter(self.game.delta_time)

            if self.jump_is_pressed:
                self.character.start_movement("jump", 'right')
                self.character.movementCharacter(self.game.delta_time)


        elif self.right_is_unpressed:
            self.character.quiet_right()

        elif self.left_is_unpressed:
            self.character.quiet_left()

        if self.jump_is_pressed:           
            self.character.start_movement("jump")
            if self.right_is_pressed: 
                self.character.start_movement("jump", 'right')
            if self.left_is_pressed:
                self.character.start_movement("jump", 'left')
            self.character.is_jumping()
            
            self.character.movementCharacter(self.game.delta_time)

        # if self.jump_is_unpressed:
        #     self.character.jump_end()
        self.character.renderCharacter(self.game.screen)


    def cleanup(self):
        self.sound_menu.stop_sound('menu-sound')
        self.sound_menu.unload_sound('menu-sound')