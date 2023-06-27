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

        self.fps = 0.0
        self.sound_menu = sound_manager
        self.background = FONDO_PLAYING1(self.game.pygame)
        self.background_width = self.background.get_width()
        self.background_height = self.background.get_height()
        self.background_x = 0
        self.background_y = 0
        self.x_relative = 0

        self.keys = self.game.pygame.key.get_pressed()

        if(self.configuration.sound_enabled):
            self.sound_menu.load_sound('menu-sound', 'assets/sounds/ambiental-playing.mp3')
            self.sound_menu.play_sound('menu-sound', -1)


        #Character
        self.character_factory = CharacterFactory()
        self.character = self.character_factory.create_character("sword", self.configuration.speed_character)
        self.K_move_right = self.configuration.move_right
        self.K_move_left = self.configuration.move_left
        self.K_jump = self.configuration.jump_key
        self.K_attack = self.configuration.attack_key
        self.K_unattack = self.configuration.unattack_key

        self.right_is_pressed = False
        self.left_is_pressed = False
        self.right_is_unpressed = True
        self.left_is_unpressed = True
        self.jump_is_pressed = False
        self.jump_is_unpressed = True
        self.attack_is_pressed = False
        self.attack_is_unpressed = True

        self.is_quiet = True
        self.position_character = 0
        # Transparent window
        self.transparent_window = None
        self.paused_pressed = False

        #buttons pause:
        # self.button_return_menu = HandleButton('assets/btn_back.png', pygame, sound_manager, 'assets/sounds/button-click.mp3', 'button-back-menu')
        # self.button_unpased = HandleButton('assets/btn_back.png', pygame, sound_manager, 'assets/sounds/button-click.mp3', 'button-back')

    def handle_events(self, events):
        self.keys = self.game.pygame.key.get_pressed()
        for event in events:
            if event.type == self.game.pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused_pressed = True                    
                    self.show_transparent_window()  # Muestra la ventana transparente
                    
                if event.key == self.configuration.sound_enabled:
                    self.configuration.sound_enabled

                if event.key == self.K_move_right:
                    self.left_is_pressed = False
                    self.left_is_unpressed = False
                    self.right_is_pressed = True 
                    self.sound_menu.stop_sound('running-step-l')
                    self.sound_menu.unload_sound('running-step-l')
                    self.sound_menu.load_sound('running-step-r', 'assets/sounds/running-step.mp3')
                    self.sound_menu.play_sound('running-step-r', -1)
                    self.is_quiet = False
                    
                if event.key == self.K_move_left:
                    self.left_is_pressed = True
                    self.right_is_pressed = False 
                    self.right_is_unpressed = False 
                    self.sound_menu.load_sound('running-step-l', 'assets/sounds/running-step.mp3')
                    self.sound_menu.play_sound('running-step-l', -1)
                    self.sound_menu.stop_sound('running-step-r')
                    self.sound_menu.unload_sound('running-step-r')
                    self.is_quiet = False

                if event.key == self.K_jump:
                    self.jump_is_pressed = True 
                    self.jump_is_unpressed = False
                    self.sound_menu.stop_sound('running-step-r')
                    self.sound_menu.unload_sound('running-step-r')
                    self.sound_menu.stop_sound('running-step-l')
                    self.sound_menu.unload_sound('running-step-l')
                    self.sound_menu.load_sound('jumping', 'assets/sounds/jumping.mp3')
                    self.sound_menu.play_sound('jumping')
                
               

            if event.type == self.game.pygame.KEYUP:

                if event.key == self.K_move_right:                    
                    self.right_is_pressed = False 
                    self.right_is_unpressed = True 
                    self.sound_menu.stop_sound('running-step-r')
                    self.sound_menu.unload_sound('running-step-r')
                    self.is_quiet = True
                   
                if event.key == self.K_move_left:
                    self.left_is_pressed = False 
                    self.left_is_unpressed = True 
                    self.sound_menu.stop_sound('running-step-l')
                    self.sound_menu.unload_sound('running-step-l')
                    self.is_quiet = True
                 
                if event.key == self.K_jump:
                    self.jump_is_pressed = False
                    self.jump_is_unpressed = True
                    
                    if self.right_is_pressed:
                        self.sound_menu.load_sound('running-step-r', 'assets/sounds/running-step.mp3')
                        self.sound_menu.play_sound('running-step-r', -1)
                    if self.left_is_pressed:
                        self.sound_menu.load_sound('running-step-l', 'assets/sounds/running-step.mp3')
                        self.sound_menu.play_sound('running-step-l', -1)
                  
            if event.type == self.K_attack:
                if event.button == 1:
                    self.attack_is_pressed = True  
                    self.attack_is_unpressed = True  
                    self.sound_menu.load_sound('attack', 'assets/sounds/sword.mp3')
                    self.sound_menu.play_sound('attack')
            if event.type == self.K_unattack:
                if event.button == 1:
                    self.attack_is_pressed = False 
                    self.attack_is_unpressed = True 

    def configuration_changed(self):
        pass
   
    def update(self, fps):
        delta = self.game.delta_time
        self.fps = fps
        self.character.update(delta, fps)
        
    def show_transparent_window(self):
        self.transparent_window = pygame.Surface((SCREEN_WIDTH(self.game.pygame), SCREEN_HEIGHT(self.game.pygame)), self.game.pygame.SRCALPHA)
        self.transparent_window.fill((0, 0, 0, 128))    
    

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

        if self.transparent_window is not None:
            self.transparent_window_position = (0 , self.background_y)
            self.game.screen.blit(self.transparent_window,  self.transparent_window_position)

        if self.left_is_pressed:
            self.is_quiet = False
        if self.right_is_pressed:           
            self.is_quiet = False
     
      
      
        if self.left_is_pressed:
            self.character.start_movement("left", self.is_quiet)
            self.character.movementCharacter(self.game.delta_time)  
        elif self.right_is_pressed:
            self.character.start_movement("right", self.is_quiet)
            self.character.movementCharacter(self.game.delta_time)
        elif self.right_is_unpressed:
            self.character.quiet_right()
        elif self.left_is_unpressed:
            self.character.quiet_left()

        if self.jump_is_pressed and not self.character.get_jumping():
            self.character.is_jumping()              
            
            direction = '' 
            if self.left_is_pressed:
                direction = 'left'
            if self.right_is_pressed:
                direction = 'right'
                
            if self.right_is_unpressed and self.left_is_unpressed:
                self.character.set_quiet(True)
         
            self.character.start_movement("jump", self.is_quiet,direction)
            if self.character.get_jumping():
                self.jump_is_pressed = False
                # self.sound_menu.stop_sound('jumping')
                # self.sound_menu.unload_sound('jumping')

        
        if self.attack_is_pressed and not self.character.get_attacking():
            self.character.is_attacking(self.fps) 
            direction = '' 
            if self.left_is_pressed or self.left_is_unpressed:
                direction = 'left'
            if self.right_is_pressed or self.right_is_unpressed:
                direction = 'right'
            
            self.character.start_movement("attack", self.is_quiet, direction)
            if self.character.get_attacking():
                self.attack_is_pressed = False

            self.character.movementCharacter(self.game.delta_time)

        # if self.jump_is_unpressed:
        #     self.character.jump_end()
        self.character.renderCharacter(self.game.screen)

    def cleanSound(self, name):
        self.sound_menu.stop_sound(name)
        self.sound_menu.unload_sound(name)
    def cleanup(self):
        self.sound_menu.stop_sound('menu-sound')
        self.sound_menu.unload_sound('menu-sound')