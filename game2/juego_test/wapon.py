import pygame
import constantes
import math

def getImgArco(): 
    img = pygame.image.load("assets/images/wapons/arco.png")
    return img

def getImgFlecha(): 
    img = pygame.image.load("assets/images/bullets/flecha.png")
    return img

class Wapons():
    def __init__(self) -> None:
        self.image_original = getImgArco()
        self.angulo = 0
        self.flip = False
        self.image = pygame.transform.rotozoom(self.image_original,self.angulo, constantes.ESCALA_ARMA)
        self.forma = self.image.get_rect()
        self.disparo = False
        self.ultimo_disparo = pygame.time.get_ticks()


    def update(self, jugador):
        self.flip = jugador.flip
        self.forma.center = jugador.forma.center
        self.forma.x += (-20 if self.flip else 20)
        

    def dibujar(self, interface):
        pygame.draw.rect(interface, (0,255,0), self.forma, width=1)
        image = pygame.transform.flip(self.image, self.flip, False)
        image = pygame.transform.rotate(self.image, self.angulo)
        interface.blit(image, self.forma)

    def mover_arma(self, mouse_pos, mouse_click):
        flecha = None
        
        distancia_x = (mouse_pos[0] - self.forma.centerx)
        if self.flip == False and distancia_x<0:
            distancia_x = 0
        elif self.flip == True and distancia_x>0:
            distancia_x = 0
        
        distancia_y = -(mouse_pos[1] - self.forma.centery)
        angulo_calculado = math.degrees(math.atan2(distancia_y,distancia_x))

        self.angulo = angulo_calculado

        disparo_coolDown = 500

        if mouse_click and self.disparo == False and (pygame.time.get_ticks()-self.ultimo_disparo >= disparo_coolDown ) :
            flecha = Bullet( self.forma.centerx, self.forma.centery, self.angulo)
            self.disparo = True
            self.ultimo_disparo = pygame.time.get_ticks()
        if mouse_click == False:
            self.disparo = False

        return flecha



        
        

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = getImgFlecha()
        self.angle = angle
        self.image = pygame.transform.rotozoom(self.image_original, self.angle,constantes.ESCALA_FLECHA)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.disparo = False
        self.delta_x = math.cos(math.radians(self.angle)) * constantes.VELOCIDAD_FLECHA
        self.delta_y = -math.sin(math.radians(self.angle)) * constantes.VELOCIDAD_FLECHA

    def dibujar(self, interface):
        interface.blit(self.image, (self.rect.centerx, self.rect.centery))

    def update(self):
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y

        if self.rect.right < 0 or self.rect.left > constantes.ANCHO_VENTANA or self.rect.top > constantes.ALTO_VENTANA or self.rect.bottom<0:
            self.kill()
