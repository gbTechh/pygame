class Enemy:
    def __init__(self):
        self.position = (0, 0)
        self.health = 100
        self.damage = 10

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


class Monster(Enemy):
    def __init__(self):
        super().__init__(health=100, attack=20, damage=10)

class Boss(Enemy):
    def __init__(self):
        super().__init__(health=500, attack=50, damage=20)

class Minion(Enemy):
    def __init__(self):
        super().__init__(health=50, attack=10, damage=5)