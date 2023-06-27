import pygame
from const import sprite_enemy_earth_type1, sprite_enemy_fly_type1
class Enemy:
    def __init__(self, enemy):
        self.position = (0, 0)
        self.health = 100
        self.damage = 10

        self.animation_speed = 0.1
        self.animation_timer = 0.0
        self.current_image_index = 0

        self.movement_sprites = ''

    def render_enemy(self, screen):
        if self.animation_timer >= self.animation_speed:
            self.current_image_index += 1
            self.animation_timer = 0.0    
        current_image = self.movement_sprites[self.current_image_index]
        screen.blit(current_image, (self.x, self.y))
    
    def movementCharacter(self, delta):    
        self.animation_timer += delta   

        if self.animation_timer >= self.animation_speed:
            self.current_image_index += 1
            self.animation_timer = 0.0   
        self.current_image_index %= len(self.movement_sprites)

    def move(self):
        # Implementar el movimiento del monstruo
        pass

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
        super().__init__(health=100, attack=20, damage=10)
        self.subtype = subtype
        self.sprites = []

    def create_enemy(self):
        if int(self.subtype) == 1:
            sprites = sprite_enemy_earth_type1(pygame)
    
class Earth(Enemy):
    def __init__(self):
        super().__init__(health=100, attack=20, damage=10)
        
        self.sprites = []

    def create_enemy(self, subtype):
        if int(subtype) == 1:
            sprites = sprite_enemy_earth_type1(pygame)
    
    


class Fly(Enemy):
    def __init__(self):
        super().__init__(health=500, attack=50, damage=20)
        self.subtype = subtype
        self.sprites = []

    def create_enemy(self):
        if int(self.subtype) == 1:
            sprites = sprite_enemy_fly_type1(pygame)


class Spider(Enemy):
    def __init__(self):
        super().__init__(health=50, attack=10, damage=5)


