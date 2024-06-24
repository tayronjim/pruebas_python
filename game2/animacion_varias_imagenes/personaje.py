import pygame
import constantes

def animacion_horizontal()->list:
    animaciones = []
    for i in range(7):
        img = pygame.image.load(f"assets/images/characters/player/player_{i}.png")
        animaciones.append(img)
    return animaciones

class Personaje():
    def __init__(self,x,y) -> None:
        self.forma = pygame.Rect(0,0,20,20) # x, y, width, height
        self.forma.center = (x,y)
        self.x = x
        self.y = y
        self.flip = False
        self.update_time = pygame.time.get_ticks()
        self.animaciones = animacion_horizontal()
        self.frame_index = 0
        self.image2 = self.animaciones[self.frame_index]

    def dibujar(self, interface):
        # pygame.draw.rect(interface, (255,255,0), self.forma)
        image2 = pygame.transform.flip(self.image2, self.flip, False)
        interface.blit(image2, (self.x, self.y) )
    
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

    def update(self):
        coolDown_animation = 100
        self.image2 = self.animaciones[self.frame_index]
        if pygame.time.get_ticks() - self.update_time >= coolDown_animation:
            self.frame_index += 1
            if self.frame_index >= len(self.animaciones): self.frame_index = 0
            self.update_time = pygame.time.get_ticks()