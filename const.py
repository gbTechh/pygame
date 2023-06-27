
#obtiene la medida de la pantalla del monitor

def SCREEN_WIDTH(py):
  screen_info = py.display.Info()
  return screen_info.current_w
  
def SCREEN_HEIGHT(py):
  screen_info = py.display.Info()
  return screen_info.current_h


FPS = 60

# Otros valores constantes
SPEED_CHARACTER = 4
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

#CORRER CON ARMA
def sprite_character_weapon1_left(py):
  return [py.image.load("assets/sprites/personaje/mazo_izquierda/mazo_izquierda_1.png"),
          py.image.load("assets/sprites/personaje/mazo_izquierda/mazo_izquierda_2.png"),]

def sprite_character_weapon1_right(py):
  return [py.image.load("assets/sprites/personaje/mazo_derecha/mazo_derecha_1.png"),
          py.image.load("assets/sprites/personaje/mazo_derecha/mazo_derecha_2.png"),]

def sprite_character_weapon2_left(py):
  return [py.image.load("assets/sprites/personaje/pistola_izquierda/pistola_izquierda_1.png"),
          py.image.load("assets/sprites/personaje/pistola_izquierda/pistola_izquierda_2.png"),]

def sprite_character_weapon2_right(py):
  return [py.image.load("assets/sprites/personaje/pistola_derecha/pistola_derecha_1.png"),
          py.image.load("assets/sprites/personaje/pistola_derecha/pistola_derecha_2.png"),]

#ATACAR CON ARMA
def sprite_character_weapon1_attack_right(py):
  return [py.image.load("assets/sprites/personaje/attacks/sword/run_attack_sword_derecha_1.png"),
          py.image.load("assets/sprites/personaje/attacks/sword/run_attack_sword_derecha_2.png"),
          py.image.load("assets/sprites/personaje/attacks/sword/run_attack_sword_derecha_3.png"),]
def sprite_character_weapon1_attack_left(py):
  return [py.image.load("assets/sprites/personaje/attacks/sword/run_attack_sword_izquierda_1.png"),
          py.image.load("assets/sprites/personaje/attacks/sword/run_attack_sword_izquierda_2.png"),
          py.image.load("assets/sprites/personaje/attacks/sword/run_attack_sword_izquierda_3.png"),]

def sprite_character_weapon2_attack_right(py):
  return [py.image.load("assets/sprites/personaje/attacks/pistola/run/attacking_run_weapon2_derecha_1.png"),
          py.image.load("assets/sprites/personaje/attacks/pistola/run/attacking_run_weapon2_derecha_2.png"),
          py.image.load("assets/sprites/personaje/attacks/pistola/run/attacking_run_weapon2_derecha_3.png"),]
def sprite_character_weapon2_attack_left(py):
  return [py.image.load("assets/sprites/personaje/attacks/pistola/run/attacking_run_weapon2_izquierda_1.png"),
          py.image.load("assets/sprites/personaje/attacks/pistola/run/attacking_run_weapon2_izquierda_2.png"),
          py.image.load("assets/sprites/personaje/attacks/pistola/run/attacking_run_weapon2_izquierda_3.png"),]

#ATACAR CON ARMA QUIETO
def sprite_character_weapon1_attack_quiet_right(py):
  return [py.image.load("assets/sprites/personaje/attacks/sword/quiet_attack_sword_derecha_1.png"),
          py.image.load("assets/sprites/personaje/attacks/sword/quiet_attack_sword_derecha_2.png"),
          py.image.load("assets/sprites/personaje/attacks/sword/quiet_attack_sword_derecha_3.png"),
          py.image.load("assets/sprites/personaje/attacks/sword/quiet_attack_sword_derecha_4.png"),]
def sprite_character_weapon1_attack_quiet_left(py):
  return [py.image.load("assets/sprites/personaje/attacks/sword/quiet_attack_sword_izquierda_1.png"),
          py.image.load("assets/sprites/personaje/attacks/sword/quiet_attack_sword_izquierda_2.png"),
          py.image.load("assets/sprites/personaje/attacks/sword/quiet_attack_sword_izquierda_3.png"),
          py.image.load("assets/sprites/personaje/attacks/sword/quiet_attack_sword_izquierda_3.png"),]

def sprite_character_weapon2_attack_quiet_right(py):
  return [py.image.load("assets/sprites/personaje/attacks/pistola/quiet/attacking_quiet_weapon2_derecha_1.png"),
          py.image.load("assets/sprites/personaje/attacks/pistola/quiet/attacking_quiet_weapon2_derecha_2.png"),
          py.image.load("assets/sprites/personaje/attacks/pistola/quiet/attacking_quiet_weapon2_derecha_3.png"),]
def sprite_character_weapon2_attack_quiet_left(py):
  return [py.image.load("assets/sprites/personaje/attacks/pistola/quiet/attacking_quiet_weapon2_izquierda_1.png"),
          py.image.load("assets/sprites/personaje/attacks/pistola/quiet/attacking_quiet_weapon2_izquierda_2.png"),
          py.image.load("assets/sprites/personaje/attacks/pistola/quiet/attacking_quiet_weapon2_izquierda_3.png"),]

#ATACAR CON ARMA SALTANDO
def sprite_character_weapon1_attack_jump_right(py):
  return [py.image.load("assets/sprites/personaje/attacks/sword/jump_attack_weapon_1_derecha_1.png"),
          py.image.load("assets/sprites/personaje/attacks/sword/jump_attack_weapon_1_derecha_2.png"),]
def sprite_character_weapon1_attack_jump_left(py):
  return [py.image.load("assets/sprites/personaje/attacks/sword/jump_attack_weapon_1_izquierda_1.png"),
          py.image.load("assets/sprites/personaje/attacks/sword/jump_attack_weapon_1_izquierda_2.png"),]

def sprite_character_weapon2_attack_jump_right(py):
  return [py.image.load("assets/sprites/personaje/attacks/pistola/jump/attacking_jump_weapon2_derecha_1.png"),
          py.image.load("assets/sprites/personaje/attacks/pistola/jump/attacking_jump_weapon2_derecha_2.png"),]
def sprite_character_weapon2_attack_jump_left(py):
  return [py.image.load("assets/sprites/personaje/attacks/pistola/jump/attacking_jump_weapon2_derecha_1.png"),
          py.image.load("assets/sprites/personaje/attacks/pistola/jump/attacking_jump_weapon2_derecha_2.png"),]



#SALTAR
def sprite_character_jump_right(py):
  return [py.image.load("assets/sprites/personaje/jump/jump_mazo/jump_mazo_derecha_1.png"),
          py.image.load("assets/sprites/personaje/jump/jump_mazo/jump_mazo_derecha_2.png"),]
def sprite_character_jump_left(py):
  return [py.image.load("assets/sprites/personaje/jump/jump_mazo/jump_mazo_izquierda_1.png"),
          py.image.load("assets/sprites/personaje/jump/jump_mazo/jump_mazo_izquierda_2.png"),]

def sprite_character_weapon2_jump_right(py):
  return [py.image.load("assets/sprites/personaje/jump/jump_pistola/jump_weapon2_derecha_1.png"),
          py.image.load("assets/sprites/personaje/jump/jump_pistola/jump_weapon2_derecha_2.png"),]
def sprite_character_weapon2_jump_left(py):
  return [py.image.load("assets/sprites/personaje/jump/jump_pistola/jump_weapon2_izquierda_1.png"),
          py.image.load("assets/sprites/personaje/jump/jump_pistola/jump_weapon2_izquierda_2.png"),]

#QUIETO
def sprite_character_quiet_right(py):
  return [py.image.load("assets/sprites/personaje/quieto/quieto_mazo_derecha.png"),]
def sprite_character_quiet_left(py):
  return [py.image.load("assets/sprites/personaje/quieto/quieto_mazo_izquierda.png"),]

def sprite_character_quiet_weapon2_right(py):
  return [py.image.load("assets/sprites/personaje/quieto/quieto_weapon2_derecha.png"),]
def sprite_character_quiet_weapon2_left(py):
  return [py.image.load("assets/sprites/personaje/quieto/quieto_weapon2_izquierda.png"),]

#######Enemies
def sprite_enemy_earth_type1(py):
  return [py.image.load("assets/sprites/enemies/eart_type1_1.png"),py.image.load("assets/sprites/enemies/eart_type1_2.png")]
  
def sprite_enemy_fly_type1(py):
  return [py.image.load("assets/sprites/enemies/eart_fly1_1.png"),py.image.load("assets/sprites/enemies/eart_fly1_2.png")]
