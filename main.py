import pygame, sys
from pygame.locals import *

pygame.init()

screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)

TEXT_COLOR = (255,255,255)

HC74225 = (199,66,37)
H61CD35 = (97,205,53)

pygame.display.set_caption('Mi primer juego')
FONDO =  pygame.image.load("src/assets/bg.jpg").convert()
FONDO = pygame.transform.scale(FONDO,(SCREEN_WIDTH, SCREEN_HEIGHT))
# SCREEN.blit(FONDO, (0,0))

background_x = 0
font = pygame.font.SysFont("arialblack", 40)

def draw_text(text, font, text_col, x,y):
  img = font.render(text, True, text_col),
  SCREEN.blit(img, (x,y))

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  draw_text("Press Space to pause", font, TEXT_COLOR,400, 600)

  keys = pygame.key.get_pressed()

  # if keys[pygame.K_RIGHT]:
  #   background_x -= 10
  # if keys[pygame.K_LEFT]:
  #   background_x += 1

  # SCREEN.blit(FONDO, (background_x, 0))
  # SCREEN.blit(FONDO, (background_x + SCREEN_WIDTH, 0))

  # if(background_x <= -SCREEN_WIDTH):
  #   background_x = 0
  
  pygame.display.flip()
  
  pygame.display.update()