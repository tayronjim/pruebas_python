import pygame
import sys
import constantes

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("primer ventana")

run = True
while run == True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
sys.exit()