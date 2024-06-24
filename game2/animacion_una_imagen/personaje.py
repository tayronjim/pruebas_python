import pygame
import constantes

class Personaje():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.flip = False
        self.frame_index = 0
        self.imagen = pygame.image.load("assets/images/characters/player/walking.png").convert_alpha()
        self.ancho_imagen = self.imagen.get_width() // 7
        self.alto_imagen = self.imagen.get_height()
        self.frames = [self.imagen.subsurface(pygame.Rect(i * self.ancho_imagen, 0, self.ancho_imagen, self.alto_imagen)) for i in range(7)]
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.velocidad = 5
        self.animar_contador = 0
    
    def animar(self):
        self.animar_contador += 1
        if self.animar_contador >= 5:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]
            self.animar_contador = 0

    def dibujar(self, interface):
        image = pygame.transform.flip(self.image, self.flip, False)
        interface.blit(image, (self.x, self.y))
    
    def movimiento(self, delta_x, delta_y):
        limite_ancho = constantes.ANCHO_VENTANA-40
        limite_alto = constantes.ALTO_VENTANA-40

        if delta_x < 0:
            self.flip = True
        if delta_x > 0:
            self.flip = False
        
        if self.x >= 0 and self.x <= limite_ancho:
            self.x +=  delta_x
            if self.x <= 0: self.x = 1
            if self.x > limite_ancho: self.x = limite_ancho

        if self.y >= 0 and self.y <= limite_alto:
            self.y +=  delta_y
            if self.y < 0: self.y = 1
            if self.y > limite_alto: self.y = limite_alto

   