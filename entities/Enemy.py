import pygame
from const import sprite_enemy_earth_type1, sprite_enemy_fly_type1, SCREEN_WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy):
        self.position = (0, 0)
        self.health = 100
        self.damage = 10

        self.animation_speed = 0.1
        self.animation_timer = 0.0
        self.current_image_index = 0

      

    def render_enemy(self, screen, movement_sprites,x ,y):
        if(x > 0):
            if self.animation_timer >= self.animation_speed:
                self.current_image_index += 1
                self.animation_timer = 0.0    
            current_image = movement_sprites[self.current_image_index]
            
            screen.blit(current_image, (x, y))
            
        

    
    def movementCharacter(self, delta, movement_sprites):    
        self.animation_timer += delta   
        
        if self.animation_timer >= self.animation_speed:
            self.current_image_index += 1
            self.animation_timer = 0.0   
        self.current_image_index %= len(movement_sprites)



    def attack(self):
        # Implementar el ataque del monstruo
        pass

    def equip_weapon(self, slot, weapon):
        self.weapons[slot] = weapon

    def upgrade_weapon(self, slot):
        if self.weapons[slot]:
            self.weapons[slot].upgrade()


class Earth(Enemy):
    def __init__(self, subtype):
        super().__init__(subtype)
        self.subtype = subtype
        
        self.health = 20
        self.attack = 10
        self.resistance = 10
        self.sprites = []
        self.x = SCREEN_WIDTH(pygame)
        self.y = 740
        self.count = 0
        self.speed = 10

    def set_attributes(self):
        if int(self.subtype) == 1:
            self.sprites = sprite_enemy_earth_type1(pygame)
            self.health = 20
            self.attack = 10
            self.resistance = 10 
            self.speed = 10

    def update_movement(self, screen, time):
       
        x = self.x
        x -= time * self.speed

        self.render_enemy(screen, self.sprites, x, self.y)

    def reset_x(self):
        self.x = SCREEN_WIDTH(pygame)
    


class Fly(Enemy):
    def __init__(self, subtype):
        super().__init__(subtype)
        self.subtype = subtype
        
        self.health = 20
        self.attack = 10
        self.resistance = 10
        self.sprites = []
        self.x = SCREEN_WIDTH(pygame)
        self.y = 100
        self.count = 0
        self.speed = 10

    def set_attributes(self):
        if int(self.subtype) == 1:
            self.sprites = sprite_enemy_fly_type1(pygame)
            self.health = 20
            self.attack = 10
            self.resistance = 10 
            self.speed = 10

    def update_movement(self, screen, time):
       
        x = self.x
        x -= time * self.speed
        x = x // 1
        
        self.render_enemy(screen, self.sprites, x, self.y)

    def reset_x(self):
        self.x = SCREEN_WIDTH(pygame)   
        
        
class Spider(Enemy):
    def __init__(self):
        super().__init__(health=50, attack=10, damage=5)


