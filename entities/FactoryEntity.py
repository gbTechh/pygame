import pygame
from entities.Character import Character
from entities.Weapon import Sword, Gun, Staff
from entities.Enemy import Enemy, Fly, Earth

class CharacterFactory:
    def create_character(self, weapon_type, speed):
        weapon = self.create_weapon(weapon_type)
        return Character(weapon, weapon_type, speed)

    def create_weapon(self, weapon_type):
        if weapon_type == "sword":
            return Sword()
        elif weapon_type == "gun":
            return Gun()
        elif weapon_type == "staff":
            return Staff()
        else:
            return Sword()

class EnemyFactory:    
    def __init__(self):
        pass
    def create_enemy(self, enemy_type, delta, subtype, screen, counter):
        
        enemy = self.create_enemy_instance(enemy_type, subtype)
        enemy.set_attributes()
        sprites = enemy.sprites
        enemy.movementCharacter(delta, sprites )
        enemy.update_movement(screen, counter)
        return enemy

   
    def create_enemy_instance(self, enemy_type, subtype):
        if enemy_type == 'fly':
            return Fly(subtype)
        elif enemy_type == 'earth':
            return Earth(subtype)
        else:
            return Earth(subtype)
    
    
    
  