import pygame

class ExitState:
    def __init__(self, game):
        self.game = game

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.change_state("menu")

    def update(self, fps):
        pass

    def render(self):
        self.game.screen.fill((0, 0, 255))
        # Render game over elements
        pygame.display.flip()

    def cleanup(self):
        pass