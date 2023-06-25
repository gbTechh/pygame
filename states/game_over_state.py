import pygame

class GameOverState:
    def __init__(self, game, configuration):
        self.game = game

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.change_state("menu")

    def update(self):
        pass

    def render(self):
        self.game.screen.fill((0, 0, 255))
        # Render game over elements
        pygame.display.flip()

    def cleanup(self):
        pass