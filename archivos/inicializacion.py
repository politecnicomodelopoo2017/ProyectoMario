from clases import *
from clases.control.Corazon import Corazon
from clases.control.Letra import Letra

def inicializacion(mario):

    x = 0

    for i in range(45):
        piso = Piso(x,695)
        x += 72

    x = 3528

    for i in range(20):
        piso = Piso(x,695)
        x += 72

    mario.inicializar_vidas()
    m = Mastil(1000)

    #LETRAS

    P = Letra(400, 300, "imagenes/letras/P.png")
    A = Letra(500, 300, "imagenes/letras/A.png")
    U = Letra(600, 300, "imagenes/letras/U.png")
    S = Letra(700, 300, "imagenes/letras/S.png")
    A = Letra(800, 300, "imagenes/letras/A.png")
'''
    l = Ladrillo(500, 450, False)
    l = Ladrillo(580, 450, True)
    s = Signo(660, 450)
    s = Ladrillo(820, 450, False)
    l = Ladrillo(740, 450, True)
    m = Moneda(675, 340, False)
    l = Ladrillo(500, 200, False)
    l = Ladrillo(580, 200, True)
    l = Signo(660, 200)
    l = Ladrillo(740, 200, True)
    l = Ladrillo(820, 200, False)
    t = Tuberia(1000, 2)
    t = Tuberia(1600, 3)
    g = Goomba(1300, 630)
    g = Goomba(1800, 630)
    s = Signo(1300, 350)
'''