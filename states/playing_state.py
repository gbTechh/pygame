import sys
sys.path.append('../const.py')
import pygame.mixer

from components.Button import HandleButton
from const import FONDO_PLAYING1, SCREEN_WIDTH, SCREEN_HEIGHT
from configuration import SoundManager
from entities.Character import Character
from entities.FactoryEntity import CharacterFactory, EnemyFactory
from utils.time import convert_time

sound_manager = SoundManager()

class PlayingState:
    def __init__(self, game, configuration):
        self.game = game
        self.configuration = configuration
        self.configuration.register_observer(self)


        self.start_game = False
        self.fps = 0.0
        self.sound_menu = sound_manager
        self.sound_menu.reset_sounds()
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

        #Weapons
        self.K_weapon1 = self.configuration.change_weapon_1
        self.K_weapon2 = self.configuration.change_weapon_2
        self.K_weapon3 = self.configuration.change_weapon_3
        self.weapon_activate = 'sword'
        
        #Character
        self.character_factory = CharacterFactory()
        self.character = self.character_factory.create_character(self.weapon_activate, self.configuration.speed_character)
        
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
        
        self.button_return_menu = HandleButton('assets/btn_back.png', self.game.pygame, sound_manager, 'assets/sounds/button-click.mp3', 'button-back-menu')
        self.button_unpaused = HandleButton('assets/btn_play.png', self.game.pygame, sound_manager, 'assets/sounds/button-click.mp3', 'button-back')
        self.button_reset = HandleButton('assets/btn_reset.png', self.game.pygame, sound_manager, 'assets/sounds/button-click.mp3', 'button-reset')

         # Counter
        self.counter = 0

        # Health bar
        self.health = 100
        self.max_health = 100
        self.health_bar_width = 200
        self.health_bar_height = 20

        #Enemies
        self.levels = Levels()
        self.all_levels = self.levels.levels
        self.enemy_factory = EnemyFactory()
        self.current_level = 1

    def handle_events(self, events):
        self.keys = self.game.pygame.key.get_pressed()
        for event in events:
                  
            if event.type == self.game.pygame.KEYDOWN:
                if event.key == self.K_weapon1:                    
                    self.weapon_activate = 'sword'
                    self.character.update_weapon(self.weapon_activate)
                if event.key == self.K_weapon2:                    
                    self.weapon_activate = 'gun'
                    self.character.update_weapon(self.weapon_activate)
                if event.key == self.game.pygame.K_ESCAPE:
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
                    self.sound_menu.load_sound('jumping', 'assets/sounds/jumping.mp3')
                    self.sound_menu.play_sound('jumping')
                   

            if self.paused_pressed:
                self.paused_actions(event)     
               

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
                  
            if event.type == self.K_attack:
                if event.button == 1:
                    self.attack_is_pressed = True  
                    self.attack_is_unpressed = True  
                    if self.weapon_activate == 'sword':
                        self.sound_menu.load_sound('attack', 'assets/sounds/sword.mp3')
                        self.sound_menu.play_sound('attack')
                        
                    if self.weapon_activate == 'gun':
                        self.sound_menu.load_sound('attack', 'assets/sounds/shoot.mp3')
                        self.sound_menu.play_sound('attack')
            if event.type == self.K_unattack:
                if event.button == 1:
                    self.attack_is_pressed = False 
                    self.attack_is_unpressed = True 

    def paused_actions(self, event):
        if self.button_return_menu.handle_event(event, self.configuration.sound_enabled):
            self.game.change_state("menu")
        if self.button_reset.handle_event(event, self.configuration.sound_enabled):
            self.game.change_state("playing")
        if self.button_unpaused.handle_event(event, self.configuration.sound_enabled):
            self.paused_pressed = False 

    def configuration_changed(self):
        pass
    
        
    
    def update(self, fps):
        delta = self.game.delta_time
        self.fps = fps
        self.character.update(delta, fps)
        self.counter += delta  # Incrementa el contador en cada frame
        
    def show_transparent_window(self):
        self.transparent_window = pygame.Surface((SCREEN_WIDTH(self.game.pygame), SCREEN_HEIGHT(self.game.pygame)), self.game.pygame.SRCALPHA)
        self.transparent_window.fill((0, 0, 0, 128))    
    
    def start_level(self, counter, delta, screen, timer):
        timer = timer // 1
        for level, level_data in self.all_levels.items():
            for enemy_data in level_data['enemies']:
                enemy_type = enemy_data['type']
                total = 0
                for subtype, subtype_data in enemy_data['suptye'].items():
                    total = subtype_data['total']
                    interval_time = subtype_data['interval_time']

        if(timer % 2 == 0):
            self.enemy_factory.create_enemy('fly', delta, 1, screen, counter)
            self.enemy_factory.create_enemy('earth', delta, 1, screen, counter)
        if(timer % 10 == 0):
            self.enemy_factory.create_enemy('fly', delta, 1, screen, counter)
            self.enemy_factory.create_enemy('earth', delta, 1, screen, counter)
        
        if(timer % 15 == 0):
            self.enemy_factory.create_enemy('fly', delta, 1, screen, counter)
            self.enemy_factory.create_enemy('fly', delta, 1, screen, counter)
                        
                        
        

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

        if self.transparent_window is not None and self.paused_pressed:
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

        ##redner buttons pause
        if self.paused_pressed:
            button_return_menu_x = 100
            button_return_menu_y = 100
            self.button_return_menu.render(self.game.screen, button_return_menu_x, button_return_menu_y)

            button_reset_x = (SCREEN_WIDTH(self.game.pygame) // 2) - (self.button_reset.width // 2)
            button_reset_y = SCREEN_HEIGHT(self.game.pygame) // 2
            self.button_reset.render(self.game.screen, button_reset_x, button_reset_y)

            button_unpaused_x = (SCREEN_WIDTH(self.game.pygame) // 2) - (self.button_unpaused.width // 2)
            button_unpaused_y = (SCREEN_HEIGHT(self.game.pygame) // 2) + (self.button_reset.height)
            self.button_unpaused.render(self.game.screen, button_unpaused_x, button_unpaused_y)
        
        # Renderizar contador en la parte superior de la pantalla
        counter_font = pygame.font.Font(None, 36)
        counter_text = counter_font.render(f"Tiempo: {convert_time(int(self.counter))}", True, (255, 255, 255))
        counter_rect = counter_text.get_rect()
        counter_rect.center = (SCREEN_WIDTH(self.game.pygame) // 2, 50)
        self.game.screen.blit(counter_text, counter_rect)

        
        
        if(self.game.counter_time > 1):
            self.start_level(self.game.counter_time, self.game.delta_time, self.game.screen, self.counter)

    def cleanSound(self, name):
        self.sound_menu.stop_sound(name)
        self.sound_menu.unload_sound(name)
    def cleanup(self):
        self.sound_menu.stop_sound('menu-sound')
        self.sound_menu.unload_sound('menu-sound')
    
    def render_enemies(self):
        pass
    # Función para disminuir la vida
    def decrease_health(self, damage):
        self.character.decrease_health(damage)
        if self.character.is_dead():
            # Realizar acciones cuando el personaje muere
            pass

class Levels():
    def __init__(self):
        self.levels = {
            1: {     
                'weapons': ['sword'],    
                'time': 120,    
                'enemies': [
                    {
                        'type': 'earth',
                        'suptye': {
                            1: {
                                'total': 100,
                                'interval_time': 3
                            },                            
                        },
                        
                    },
                    {
                        'type': 'fly',
                        'suptye': {
                            1: {
                                'total': 100,
                                'interval_time': 3
                            },
                            2: {
                                'total': 40,
                                'interval_time': 5
                            }
                        },
                        
                    },
                    
                ]
            },
            2: {     
                'weapons': ['sword', 'gun'],    
                'time': 120,     
                'enemies': [
                    {
                        'type': 'earth',
                        'suptye': {
                            1: {
                                'total': 200,
                                'interval_time': 3
                            },                            
                        },
                        
                    },
                    {
                        'type': 'fly',
                        'suptye': {
                            1: {
                                'total': 120,
                                'interval_time': 4
                            },
                            2: {
                                'total': 50,
                                'interval_time': 5
                            }
                        },
                        
                    },
                    
                ]
            }, 
        }

    def get_level_configs(self, level):
        return level[level]


    
