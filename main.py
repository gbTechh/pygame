import pygame, sys
from pygame.locals import *

pygame.init()

screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h
PANTALLA = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BLANCO = (255,255,255)
NEGRO = (0,0,0)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)

HC74225 = (199,66,37)
H61CD35 = (97,205,53)

pygame.display.set_caption('Mi primer juego')
FONDO =  pygame.image.load("src/assets/bg.jpg").convert()
FONDO = pygame.transform.scale(FONDO,(SCREEN_WIDTH, SCREEN_HEIGHT))
PANTALLA.blit(FONDO, (0,0))

background_x = 0

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  background_x -= 1

  keys = pygame.key.get_pressed()

  if(keys[pygame.key.get_pressed()])

  PANTALLA.blit(FONDO, (background_x, 0))
  PANTALLA.blit(FONDO, (background_x + SCREEN_WIDTH, 0))

  if(background_x <= -SCREEN_WIDTH):
    background_x = 0
  
  pygame.display.flip()
  
  pygame.display.update()