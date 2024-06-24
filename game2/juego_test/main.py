import pygame
import sys
from personaje import Personaje
from wapon import Wapons, Bullet
import constantes

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))
pygame.display.set_caption("primer ventana")

jugador = Personaje(40,40)
arma = Wapons()
flecha = Bullet( 0, 0, 0)
grupo_flechas = pygame.sprite.Group()


run = True
while run:
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
        
    
    if key[pygame.K_LEFT] or key[pygame.K_a]:
        delta_x = -5
        flip_x = True
    elif key[pygame.K_RIGHT] or key[pygame.K_d]:
        delta_x = 5
        flip_x = False
    else: delta_x = 0

    if key[pygame.K_UP] or key[pygame.K_w]:
        delta_y = -5    
    elif key[pygame.K_DOWN] or key[pygame.K_s]:
        delta_y = 5
    else: delta_y = 0

    flecha = arma.mover_arma(mouse_pos,mouse_click[0])

    if flecha:
        grupo_flechas.add(flecha)
    for flecha in grupo_flechas:
        flecha.update()
            
    ventana.fill(constantes.COLOR_BG)
    jugador.dibujar(ventana)
    arma.dibujar(ventana)

    for flecha in grupo_flechas:
        flecha.dibujar(ventana)
    
    print(grupo_flechas)
    jugador.movimiento(delta_x,delta_y)
    if delta_x != 0 or delta_y != 0:
        jugador.update()
        arma.update(jugador)

    pygame.display.update()

pygame.quit()
sys.exit()