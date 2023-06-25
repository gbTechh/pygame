class Weapon:
    def __init__(self):
        self.damage = 0
        self.level = 1

    def upgrade(self):
        self.level += 1
        self.damage += 10 * self.level



class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 20

class Gun(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 15

class Staff(Weapon):
    def __init__(self):
        super().__init__()
        self.damage = 25