import pygame
import time
from const import sprite_character_run_left, sprite_character_weapon1_right, sprite_character_jump_right, sprite_character_jump_left,sprite_character_quiet_right,sprite_character_quiet_left, sprite_character_weapon1_left,sprite_character_weapon1_attack_right,sprite_character_weapon1_attack_left, sprite_character_weapon1_attack_quiet_right, sprite_character_weapon1_attack_quiet_left, sprite_character_weapon1_attack_jump_right, sprite_character_weapon1_attack_jump_left, SCREEN_WIDTH
from configuration import SoundManager

sound_manager = SoundManager()
clock = pygame.time.Clock()

class Character(pygame.sprite.Sprite):
    def __init__(self, weapon, weapon_type, speed):
        super().__init__()
       
        self.sound_menu = sound_manager
        self.movement_sprites = sprite_character_weapon1_right(pygame)

        self.position = (0, 0)
        self.health = 100
        self.weapon = weapon

        self.weapon_type = weapon_type
        self.cuenta_pasos = 0
        self.right_movement = False
        self.left_movement = False

        self.animation_speed = 0.1
        self.animation_timer = 0.0
        self.current_image_index = 0

        self.speed = speed
        self.x = 400
        self.y = 710

        #MOVING
        self.is_moving = False
        self.is_quiet = True
        #JUMP
        self.jumping = False
        self.jump_count = 12
        self.jump_height = 200
        self.gravity = 1.0
        self.jump_timer = 0
        self.position_jump = 0
        self.end_jump = False

        #ATTACK
        self.attacking = False
        self.attack_duration = 4.0
        self.attack_start_time = time.time()

    def movementCharacter(self, delta):    
       
        
        if self.right_movement or self.left_movement:
            self.animation_timer += delta   

            if self.animation_timer >= self.animation_speed:
                self.current_image_index += 1
                self.animation_timer = 0.0        
    
        if self.attacking :
            self.animation_timer += delta   

            if self.animation_timer >= self.animation_speed:
                self.current_image_index += 1
                self.animation_timer = 0.0    

        print(self.current_image_index)
        self.current_image_index %= len(self.movement_sprites)



    def renderCharacter(self, screen):
        if self.animation_timer >= self.animation_speed:
            self.current_image_index += 1
            self.animation_timer = 0.0    
        current_image = self.movement_sprites[self.current_image_index]
        screen.blit(current_image, (self.x, self.y))

    def start_movement(self, movement, quiet, direction = ''):
        self.is_quiet = quiet
        if(movement == 'right'):
            self.is_quiet = False
            self.right_movement = True
            self.left_movement = False
            if(not self.jumping and not self.attacking):
                self.movement_sprites = sprite_character_weapon1_right(pygame)
            if(self.attacking):
                print('attack right')
                self.movement_sprites = sprite_character_weapon1_attack_right(pygame)
            if(self.x <= (SCREEN_WIDTH(pygame) // 2)):
                self.x += self.speed
            

        elif(movement == 'left'):  
            self.is_quiet = False          
            self.left_movement = True    
            self.right_movement = False
            if(not self.jumping and not self.attacking):
                self.movement_sprites = sprite_character_weapon1_left(pygame)
            if(self.attacking):
                self.movement_sprites = sprite_character_weapon1_attack_left(pygame)
            if(self.x >= 200):
                self.x -= self.speed

        elif(movement == 'jump'):  

            if direction == 'left' : 
                self.left_movement = True
                self.right_movement = False
                self.movement_sprites = sprite_character_jump_left(pygame)
                
            if direction == 'right' : 
                self.left_movement = False
                self.right_movement = True
                self.movement_sprites = sprite_character_jump_right(pygame)
                
                
            
            self.animation_timer = 0.0
            self.current_image_index %= len(self.movement_sprites)
            
            
        elif(movement == 'attack'):
            if direction == 'left' : 
                self.left_movement = True
                self.right_movement = False
                
                if quiet:
                    self.movement_sprites = sprite_character_weapon1_attack_quiet_left(pygame)
                if self.jumping:
                    self.movement_sprites = sprite_character_weapon1_attack_jump_left(pygame)

            if direction == 'right' : 
                self.left_movement = False
                self.right_movement = True

                if quiet:
                    self.movement_sprites = sprite_character_weapon1_attack_quiet_right(pygame)    
                if self.jumping:
                    self.movement_sprites = sprite_character_weapon1_attack_jump_right(pygame)
            self.animation_timer = 0.0
            # self.current_image_index = 0
            self.current_image_index %= len(self.movement_sprites)

   

    def update(self, delta, fps):
        if self.jumping:
            self.jump()
        if self.attacking:
            self.attack(fps)
        if self.is_moving:
            pass

            
    def get_animation_timer(self):
        return self.animation_timer
        
    def get_animation_speed(self):
        return self.animation_speed

    def get_character_x_position(self):
        return self.x
    def set_quiet(self, value):
        self.is_quiet = value
    def quiet_right(self):
        self.current_image_index = 0
        self.movement_sprites = sprite_character_quiet_right(pygame)

    def quiet_left(self):
        self.current_image_index = 0
        self.movement_sprites = sprite_character_quiet_left(pygame)

  

    def jump(self):
    
        if self.jumping:          
            if self.jump_count >= -12:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.jumping = False
                self.end_jump = True
                self.jump_count = 12
        

    def get_jumping(self):
        return self.jumping

    def is_jumping(self):
        self.jumping = True

    def attack(self, fps):
        if self.attacking:
            self.current_image_index += 1
            if not(fps - self.attack_start_time < self.attack_duration):
                self.attacking = False   
                
          
             
               

    def is_attacking(self,fps):
        self.attacking = True
        self.attack_start_time = fps

    def set_attack_start_time(self, value):
        self.attack_start_time = value
    def get_attacking(self):
        return self.attacking

    

         
   


    

    def take_damage(self, amount):
        self.health -= amount