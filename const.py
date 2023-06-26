
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

def sprite_character_weapon1_left(py):
  return [py.image.load("assets/sprites/personaje/mazo_izquierda/mazo_izquierda_2.png"),
          py.image.load("assets/sprites/personaje/mazo_izquierda/mazo_izquierda_1.png"),
          py.image.load("assets/sprites/personaje/mazo_izquierda/mazo_izquierda_3.png"),]

def sprite_character_weapon1_right(py):
  return [py.image.load("assets/sprites/personaje/mazo_derecha/mazo_derecha_2.png"),
          py.image.load("assets/sprites/personaje/mazo_derecha/mazo_derecha_1.png"),
          py.image.load("assets/sprites/personaje/mazo_derecha/mazo_derecha_3.png"),]

def sprite_character_jump_right(py):
  return [py.image.load("assets/sprites/personaje/jump/jump_mazo/jump_mazo_derecha_1.png"),
          py.image.load("assets/sprites/personaje/jump/jump_mazo/jump_mazo_derecha_2.png"),]
def sprite_character_jump_left(py):
  return [py.image.load("assets/sprites/personaje/jump/jump_mazo/jump_mazo_izquierda_1.png"),
          py.image.load("assets/sprites/personaje/jump/jump_mazo/jump_mazo_izquierda_2.png"),]

def sprite_character_quiet_right(py):
  return [py.image.load("assets/sprites/personaje/quieto/quieto_mazo_derecha.png"),]
def sprite_character_quiet_left(py):
  return [py.image.load("assets/sprites/personaje/quieto/quieto_mazo_izquierda.png"),]
