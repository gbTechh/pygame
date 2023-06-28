
import pygame
from const import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, FONDO_MENU

from states.menu_state import MenuState
from states.playing_state import PlayingState
from states.options_state import OptionsState
from states.game_over_state import GameOverState
from configuration import Configuration, SoundManager

config = Configuration()
sound_manager = SoundManager()
class Game:
    def __init__(self):
        pygame.init()    
        self.pygame = pygame
        self.screen = self.pygame.display.set_mode((SCREEN_WIDTH(pygame), SCREEN_HEIGHT(pygame)))
        # crea un objeto Clock de pygame que se utiliza para controlar la velocidad de actualización del juego. El objeto Clock permite limitar el número de fotogramas por segundo (FPS) a los que se actualiza el juego
        self.clock = self.pygame.time.Clock()
        self.get_fps = self.clock.get_fps()
        self.paygame_time = self.pygame.time.get_ticks()
        ##self.current_state almacenara el estado del juego, se inicializa como None
        self.current_state = None
        self.running = True
        self.delta_time = self.clock.tick(FPS) / 1000.0
        
        self.counter_time = 0

   

    def change_state(self, new_state):
        if self.current_state:
            self.current_state.cleanup()

        if new_state == "menu":             
            self.current_state = MenuState(self, config)
        elif new_state == "playing":
            self.counter_time = 0
            self.current_state = PlayingState(self, config)
        elif new_state == "options":
            self.current_state = OptionsState(self, config)
        elif new_state == "game_over":
            self.current_state = GameOverState(self, config)
        elif new_state == "exit":
            self.running = False 

    def run(self):
        self.change_state("menu")
        
        
        while self.running:
            events = self.pygame.event.get()
            self.counter_time += 1
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.get_fps += 1
            self.current_state.handle_events(events)
            self.current_state.update(self.get_fps)
            self.screen.fill((0, 0, 0))
            self.screen.blit(FONDO_MENU(pygame), (0, 0))
            self.current_state.render()
            self.pygame.display.flip()
            self.pygame.display.update()

            self.clock.tick(FPS)

        self.pygame.quit()