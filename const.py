
#obtiene la medida de la pantalla del monitor

def SCREEN_WIDTH(py):
  screen_info = py.display.Info()
  return screen_info.current_w
  
def SCREEN_HEIGHT(py):
  screen_info = py.display.Info()
  return screen_info.current_h


FPS = 60

# Otros valores constantes
PLAYER_SPEED = 5
ENEMY_SPEED = 3

def FONDO_MENU(pygame):
  menu = pygame.image.load("assets/bg-menu.jpeg").convert()
  return pygame.transform.scale(menu,(SCREEN_WIDTH(pygame), SCREEN_HEIGHT(pygame)))

def FONDO_PLAYING1(pygame):
  return pygame.image.load("assets/bgplaying-1.jpg").convert()
 

def FONDO_OPTIONS(pygame):
  menu = pygame.image.load("assets/bgoptions.png").convert()
  return pygame.transform.scale(menu,(SCREEN_WIDTH(pygame), SCREEN_HEIGHT(pygame)))


##CONFIGURATIONS CONST
DEFAULT_SOUND_ENABLED = True