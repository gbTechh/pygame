class Character:
    def __init__(self):
        self.position = (0, 0)
        self.health = 100
        self.weapon = None

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