import pygame
from const import sprite_character_run_left, sprite_character_weapon1_right, sprite_character_jump_right, sprite_character_jump_left,sprite_character_quiet_right,sprite_character_quiet_left, sprite_character_weapon1_left, SCREEN_WIDTH

class Character(pygame.sprite.Sprite):
    def __init__(self, weapon, weapon_type, speed):
        super().__init__()
       
       
        self.movement_sprites = sprite_character_weapon1_right(pygame)

        self.position = (0, 0)
        self.health = 100
        self.weapon = weapon

        self.weapon_type = weapon_type
        self.cuenta_pasos = 0
        self.right_movement = False
        self.left_movement = False

        self.animation_speed = 0.5
        self.animation_timer = 0.0
        self.current_image_index = 0

        self.speed = speed
        self.x = 400
        self.y = 710

        #JUMP
        self.jumping = False
        self.jump_count = 5
        self.jump_height = 200
        self.gravity = 1.0
        self.jump_timer = 0
        self.position_jump = 0

    def movementCharacter(self, delta):
        
        self.animation_timer += delta

        if self.animation_timer >= self.animation_speed:
            self.current_image_index += 1
            animation_timer = 0.0        
        
        

        if self.jumping:
            self.current_image_index += 1
            animation_timer = 0.0    

        self.current_image_index %= len(self.movement_sprites)


    def renderCharacter(self, screen):
        current_image = self.movement_sprites[self.current_image_index]
        screen.blit(current_image, (self.x, self.y))

    def start_movement(self, movement, jump_direction = 'right'):
        if(movement == 'right'):
            self.right_movement = True
            self.movement_sprites = sprite_character_weapon1_right(pygame)
            self.left_movement = False

            if(self.x <= (SCREEN_WIDTH(pygame) // 2)):
                self.x += self.speed
        elif(movement == 'left'):
            self.left_movement = True    
            self.right_movement = False
            self.movement_sprites = sprite_character_weapon1_left(pygame)
            if(self.x >= 200):
                self.x -= self.speed
        elif(movement == 'jump'):
            if jump_direction == 'left' : 
                self.left_movement = True
                self.right_movement = False
                self.movement_sprites = sprite_character_jump_left(pygame)

            if jump_direction == 'right' : 
                self.left_movement = False
                self.right_movement = True
                self.movement_sprites = sprite_character_jump_right(pygame)

        
           
            self.current_image_index = 0

            self.jump()

            
   

    def update_animation_timer(self, delta):
        self.animation_timer += delta

    def get_animation_timer(self):
        return self.animation_timer
        
    def get_animation_speed(self):
        return self.animation_speed

    def get_character_x_position(self):
        return self.x

    def quiet_right(self):
        self.current_image_index = 0
        self.movement_sprites = sprite_character_quiet_right(pygame)

    def quiet_left(self):
        self.current_image_index = 0
        self.movement_sprites = sprite_character_quiet_left(pygame)

    def jump_end(self):
        self.y = 710
        self.jump_timer = 0
        # self.jumping = False

    def jump(self):
        neg = 1
        
        while self.jump_count < 60:
            self.jump_timer += 1    
            
            if self.jump_timer < 60:
                if self.jumping: 
                    if self.jump_timer <= 20:
                        
                        self.y -= (self.jump_timer ** 2) * 0.1

                    if self.jump_timer > 20 and self.jump_timer < 40:
                        
                        if self.y < 700:
                            self.y += self.jump_timer
                        else:
                            
                            self.jumping = False
                            self.jump_end()
            else:             
                self.jumping = False
                
           

    def is_jumping(self):
        self.jumping = True
    def update_jumping(self, value):
        self.jumping = value

    def get_jumping(self):
        return self.jumping

    def move_up(self):
        # Implementar el movimiento hacia arriba del personaje
        pass

    def move_down(self):
        # Implementar el movimiento hacia abajo del personaje
        pass

    def move_left(self):
        # Implementar el movimiento hacia la izquierda del personaje
        pass

    def move_right(self):
        # Implementar el movimiento hacia la derecha del personaje
        pass

    def attack(self):
        # Implementar el ataque del personaje
        pass

    def take_damage(self, amount):
        self.health -= amount