from entities.Character import Character
from entities.Weapon import Sword, Gun, Staff

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
            raise ValueError(f"Invalid weapon type: {weapon_type}")