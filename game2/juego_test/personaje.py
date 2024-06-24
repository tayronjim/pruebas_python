import pygame
import constantes

def animacion_horizontal()->list:
    animaciones = []
    for i in range(7):
        img = pygame.image.load(f"assets/images/characters/player/player_run_{i}.png")
        animaciones.append(img)
    return animaciones

def animacion_espera()->list:
    animaciones = []
    for i in range(7):
        img = pygame.image.load(f"assets/images/characters/player/player_wait_{i}.png")
        animaciones.append(img)
    return animaciones

class Personaje():
    def __init__(self,x,y) -> None:
       # self.forma = pygame.Rect(0,0,constantes.AREA_PERSONAJE_WIDTH,constantes.AREA_PERSONAJE_HEIGHT) # x, y, width, height
        self.x = x
        self.y = y
        self.flip = False
        self.update_time = pygame.time.get_ticks()
        self.animaciones = animacion_horizontal()
        self.frame_index = 0
        self.image = self.animaciones[self.frame_index]
        self.forma = self.image.get_rect()

    def dibujar(self, interface):
        pygame.draw.rect(interface, (255,255,0), self.forma, width=1)
        image = pygame.transform.flip(self.image, self.flip, False)
        interface.blit(image, self.forma)
    
    def movimiento(self, delta_x, delta_y):
        limite_ancho = constantes.ANCHO_VENTANA - constantes.AREA_PERSONAJE_WIDTH
        limite_alto = constantes.ALTO_VENTANA - constantes.AREA_PERSONAJE_HEIGHT

        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False
        
        if self.forma.x >= 0 and self.forma.x <= limite_ancho:
            self.forma.x += delta_x
            self.x +=  delta_x
            if self.forma.x <= 0: self.forma.x = 1
            if self.forma.x > limite_ancho: self.forma.x = limite_ancho

        if self.forma.y >= 0 and self.forma.y <= limite_alto:
            self.forma.y += delta_y
            self.y +=  delta_y
            if self.forma.y < 0: self.forma.y = 1
            if self.forma.y > limite_alto: self.forma.y = limite_alto

    def update(self):
        coolDown_animation = 100
        self.image = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= coolDown_animation:
            self.frame_index += 1
            if self.frame_index >= len(self.animaciones): self.frame_index = 0
            self.update_time = pygame.time.get_ticks()