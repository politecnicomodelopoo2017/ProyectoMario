import pygame
from .Sprites import *
from .Fin import *
from .Palabras import *
import random

class Controlador(object):

    @classmethod
    def iniciar(cls):
        pygame.init()

    @classmethod
    def terminar(cls):
        pygame.quit()
        quit()

    @classmethod
    def configurar_pantalla(cls, ancho, alto):
        display = pygame.display.set_mode((ancho, alto))#, pygame.FULLSCREEN) #
        pygame.display.set_caption("Super Poli Bros")
        return display

    @classmethod
    def iniciar_reloj(cls):
        return pygame.time.Clock()

    @classmethod
    def set_fps(cls, reloj, frames):
        reloj.tick(frames)

    @classmethod
    def rellenar_pantalla(cls, ventana, colores):
        ventana.fill(colores["Negro"])

    @classmethod
    def buscar_eventos(cls, Colores):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cls.terminar()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    cls.terminar()
                if evento.key == pygame.K_BACKSPACE:
                    return Palabra(280, 280, Colores["Blanco"], " ", 100)
                if evento.key == pygame.K_a:
                    return Palabra(280, 280, Colores["Blanco"], "a", 100)
                if evento.key == pygame.K_b:
                    return Palabra(280, 280, Colores["Blanco"], "b", 100)
                if evento.key == pygame.K_c:
                    return Palabra(280, 280, Colores["Blanco"], "c", 100)
                if evento.key == pygame.K_d:
                    return Palabra(280, 280, Colores["Blanco"], "d", 100)
                if evento.key == pygame.K_e:
                    return Palabra(280, 280, Colores["Blanco"], "e", 100)
                if evento.key == pygame.K_f:
                    return Palabra(280, 280, Colores["Blanco"], "f", 100)
                if evento.key == pygame.K_g:
                    return Palabra(280, 280, Colores["Blanco"], "g", 100)
                if evento.key == pygame.K_h:
                    return Palabra(280, 280, Colores["Blanco"], "h", 100)
                if evento.key == pygame.K_i:
                    return Palabra(280, 280, Colores["Blanco"], "i", 100)
                if evento.key == pygame.K_j:
                    return Palabra(280, 280, Colores["Blanco"], "j", 100)
                if evento.key == pygame.K_k:
                    return Palabra(280, 280, Colores["Blanco"], "k", 100)
                if evento.key == pygame.K_l:
                    return Palabra(280, 280, Colores["Blanco"], "l", 100)
                if evento.key == pygame.K_m:
                    return Palabra(280, 280, Colores["Blanco"], "m", 100)
                if evento.key == pygame.K_n:
                    return Palabra(280, 280, Colores["Blanco"], "n", 100)
                if evento.key == pygame.K_o:
                    return Palabra(280, 280, Colores["Blanco"], "o", 100)
                if evento.key == pygame.K_p:
                    return Palabra(280, 280, Colores["Blanco"], "p", 100)
                if evento.key == pygame.K_q:
                    return Palabra(280, 280, Colores["Blanco"], "q", 100)
                if evento.key == pygame.K_r:
                    return Palabra(280, 280, Colores["Blanco"], "r", 100)
                if evento.key == pygame.K_s:
                    return Palabra(280, 280, Colores["Blanco"], "s", 100)
                if evento.key == pygame.K_t:
                    return Palabra(280, 280, Colores["Blanco"], "t", 100)
                if evento.key == pygame.K_u:
                    return Palabra(280, 280, Colores["Blanco"], "u", 100)
                if evento.key == pygame.K_v:
                    return Palabra(280, 280, Colores["Blanco"], "v", 100)
                if evento.key == pygame.K_w:
                    return Palabra(280, 280, Colores["Blanco"], "w", 100)
                if evento.key == pygame.K_x:
                    return Palabra(280, 280, Colores["Blanco"], "x", 100)
                if evento.key == pygame.K_y:
                    return Palabra(280, 280, Colores["Blanco"], "y", 100)
                if evento.key == pygame.K_z:
                    return Palabra(280, 280, Colores["Blanco"], "z", 100)
                if evento.key == pygame.K_SPACE:
                    return False
                return True

    @classmethod
    def Inicializacion_Final(cls):

        c1 = Final(0,0,340,184, "inicios/Transicion_Final/cuadroblanco.png")
        c2 = Final(340,0,340,184, "inicios/Transicion_Final/cuadroblanco.png")
        c3 = Final(680,0,340,184, "inicios/Transicion_Final/cuadroblanco.png")
        c4 = Final(1020,0,360,190, "inicios/Transicion_Final/cuadroblanco.png")
        c5 = Final(1020,184,360,184, "inicios/Transicion_Final/cuadroblanco.png")
        c6 = Final(1020,368,360,184, "inicios/Transicion_Final/cuadroblanco.png")
        c7 = Final(1020,552,360,190, "inicios/Transicion_Final/cuadroblanco.png")
        c8 = Final(680,552,340,190, "inicios/Transicion_Final/cuadroblanco.png")
        c9 = Final(340,552,340,190, "inicios/Transicion_Final/cuadroblanco.png")
        c10 = Final(0,552,340,190, "inicios/Transicion_Final/cuadroblanco.png")
        c11 = Final(0,368,340,184, "inicios/Transicion_Final/cuadroblanco.png")
        c12 = Final(0,184,340,184, "inicios/Transicion_Final/cuadroblanco.png")
        c13 = Final(340,184,340,184, "inicios/Transicion_Final/cuadroblanco.png")
        c14 = Final(680,184,340,184, "inicios/Transicion_Final/cuadroblanco.png")
        c15 = Final(1020,184,360,184, "inicios/Transicion_Final/cuadroblanco.png")
        c16 = Final(1020,368,360,184, "inicios/Transicion_Final/cuadroblanco.png")
        c17 = Final(680,368,340,184, "inicios/Transicion_Final/cuadroblanco.png")
        c18 = Final(340,368,340,184, "inicios/Transicion_Final/cuadroblanco.png")
