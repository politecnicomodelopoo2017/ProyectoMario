import pygame
from pygame.locals import *
import _thread
import time

ancho = 1360
alto = 768

ListaSpritesDer=["imagenes/mario/mariocorreder1.png", "imagenes/mario/mariocorreder2.png"]
ListaSpritesIzq=["imagenes/mario/mariocorreizq1.png", "imagenes/mario/mariocorreizqr2.png"]

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("imagenes/mario/marioder.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = ancho-1300
        self.rect.y = 600

    def mover(self, keys, muevePantalla, Activos, Pisos):

        self.image=pygame.image.load("imagenes/mario/marioder.png")
        self.image = pygame.transform.scale(self.image, (100, 100))

        #if pygame.sprite.spritecollideany(self, Pisos, collided=None) == None or\
        #      pygame.sprite.spritecollideany(self, Activos, collided=None) == None:
        #    _thread.start_new_thread(self.caerGravedad, (Activos,Pisos,))

        if self.rect.x<680:
                        muevePantalla=False

                        if keys[K_UP]:
                            _thread.start_new_thread(self.saltoDerecha, (Activos, Pisos,))

                        if keys[K_DOWN]: #NO EXISTE, PRUEBA
                            self.rect.y += 30

                        if keys[K_RIGHT]:
                            self.image = pygame.image.load("imagenes/mario/mariocorreder2.png")
                            self.image = pygame.transform.scale(self.image, (100, 100))
                            self.rect.x += 300

                        if self.rect.left >= 0:
                            if keys[K_LEFT]:
                                self.image = pygame.image.load("imagenes/mario/mariocorreizqr2.png")
                                self.image = pygame.transform.scale(self.image,(100, 100))
                                self.rect.x -= 300

        else:
                    self.image = pygame.image.load("imagenes/mario/marioder.png")
                    self.image = pygame.transform.scale(self.image, (100, 100))
                    muevePantalla = False
                    if keys[K_RIGHT]:
                        self.image = pygame.image.load("imagenes/mario/mariocorreder2.png")
                        self.image = pygame.transform.scale(self.image, (100, 100))
                        muevePantalla=True

                    if keys[K_LEFT]:
                        self.image = pygame.image.load( "imagenes/mario/mariocorreizqr2.png")
                        self.image = pygame.transform.scale(self.image, (100, 100))
                        self.rect.x -= 300

                    if keys[K_UP]:
                        _thread.start_new_thread(self.saltoDerecha, (Activos, Pisos,))

                    if keys[K_DOWN]: #NO EXISTE, PRUEBA
                        self.rect.y += 30

        return muevePantalla

    def saltoDerecha(self, Activos, Pisos):
        if self.rect.x < 1100:
            self.image = pygame.image.load("imagenes/mario/mariosalta.png")
            self.rect.y -= 30
            self.rect.x += 12.5
            time.sleep(0.01)
            self.rect.y -= 30
            self.rect.x += 12.5
            time.sleep(0.01)
            while pygame.sprite.spritecollideany(self, Pisos, collided = None) == None:
                self.rect.y += 30
                self.rect.x += 12.5
                time.sleep(0.01)

    def saltoIzquierda(self, Activos, Pisos):
        if self.rect.x < 1100:
            self.image = pygame.image.load("imagenes/mario/mariosalta.png")
            self.rect.y -= 37.5
            self.rect.x -= 12.5
            time.sleep(0.00001)
            self.rect.y -= 37.5
            self.rect.x -= 12.5
            time.sleep(0.00001)
            while pygame.sprite.spritecollideany(self, Pisos, collided = None) == None:
                self.rect.y += 25
                self.rect.x -= 12.5
                time.sleep(0000.1)

    def caerGravedad(self):
        self.rect.y += 10
        time.sleep(0.0001)