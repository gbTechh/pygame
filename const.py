
#obtiene la medida de la pantalla del monitor

def SCREEN_WIDTH(py):
  screen_info = py.display.Info()
  return screen_info.current_w
  
def SCREEN_HEIGHT(py):
  screen_info = py.display.Info()
  return screen_info.current_h


FPS = 30

# Otros valores constantes
SPEED_CHARACTER = 5
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

def sprite_character_run_left(py):
  return [py.image.load("assets/sprites/personaje/correr_izquierda/Pers_correr_izq_1.png"),
          py.image.load("assets/sprites/personaje/correr_izquierda/Pers_correr_izq_2.png"),
          py.image.load("assets/sprites/personaje/correr_izquierda/Pers_correr_izq_3.png"),
          py.image.load("assets/sprites/personaje/correr_izquierda/Pers_correr_izq_4.png"),
          py.image.load("assets/sprites/personaje/correr_izquierda/Pers_correr_izq_5.png"),
          py.image.load("assets/sprites/personaje/correr_izquierda/Pers_correr_izq_6.png")]

def sprite_character_run_right(py):
  return [py.image.load("assets/sprites/personaje/correr_derecha/Pers_correr_1.png"),
          py.image.load("assets/sprites/personaje/correr_derecha/Pers_correr_2.png"),
          py.image.load("assets/sprites/personaje/correr_derecha/Pers_correr_3.png"),
          py.image.load("assets/sprites/personaje/correr_derecha/Pers_correr_4.png"),
          py.image.load("assets/sprites/personaje/correr_derecha/Pers_correr_5.png"),
          py.image.load("assets/sprites/personaje/correr_derecha/Pers_correr_6.png")]
