import pygame
from const import sprite_character_run_left, sprite_character_run_right, SCREEN_WIDTH

class Character(pygame.sprite.Sprite):
    def __init__(self, weapon, weapon_type, speed):
        super().__init__()
       
       
        self.movement_sprites = sprite_character_run_right(pygame)

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
        self.x = 200
        self.y = 680

        #JUMP
        self.jumping = False
        self.jump_count = 10
        self.jump_height = 200
        self.gravity = 1.0

    def movementCharacter(self, delta):
        
        self.animation_timer += delta

        if self.animation_timer >= self.animation_speed:
            self.current_image_index += 1
            animation_timer = 0.0        
        
        self.current_image_index %= len(self.movement_sprites)
    

    def renderCharacter(self, screen):
        current_image = self.movement_sprites[self.current_image_index]
        screen.blit(current_image, (self.x, self.y))

    def start_movement(self, movement):
        if(movement == 'right'):
            self.right_movement = True
            self.movement_sprites = sprite_character_run_right(pygame)
            self.left_movement = False

            if(self.x <= (SCREEN_WIDTH(pygame) // 2)):
                self.x += self.speed
        elif(movement == 'left'):
            self.left_movement = True    
            self.right_movement = False
            self.movement_sprites = sprite_character_run_left(pygame)
            if(self.x >= 200):
                self.x -= self.speed

    def update_animation_timer(self, delta):
        self.animation_timer += delta

    def get_animation_timer(self):
        return self.animation_timer
        
    def get_animation_speed(self):
        return self.animation_speed

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