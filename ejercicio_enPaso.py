from cmu_graphics import *

def onMouseMove(x, y):
    

    app.fondo = 'negro'

Rótulo('*No a escala', 340, 370, relleno='blanco', tamaño=16)

sol = Estrella(200, 200, 35, 400, relleno=gradiente('naranja', 'amarillo', 'rojoNaranja'))

jupiter = Grupo(
    Círculo(200, 200, 150, relleno=None, borde='grisOscuro'),
    Círculo(200, 50, 15, relleno=gradiente('naranja','gris','naranja', inicio ='superior'))
    )
marte = Grupo(
    Círculo(200, 200, 125, relleno=None, borde='grisOscuro'),
    Círculo(200, 75, 10, relleno='rojoOscuro')
    )
tierra = Grupo(
    Círculo(200, 200, 100, relleno=None, borde='grisOscuro'),
    Círculo(200, 100, 10, relleno=gradiente('verde', 'azulReal', inicio='izquierda-superior'))
    )
venus = Grupo(
    Círculo(200, 200, 75, relleno=None, borde='grisOscuro'),
    Círculo(200, 125, 10, relleno='naranjaOscuro')
    )
mercurio = Grupo(
    Círculo(200, 200, 50, relleno=None, borde='grisOscuro'),
    Círculo(200, 150, 10, relleno='azulOscuro', borde = 'azul')
    )
tierra.dirección = 'sentido-horario'

def enTeclaPresionada(tecla):
    # Cambie la dirección basado en la tecla.
    if (tecla == 'derecha'):
        tierra.dirección = 'sentido-horario'
    elif (tecla == 'izquierda'):
        tierra.dirección = 'sentido-antihorario'

def enPaso():
    # Si la dirección de la tierra es en sentido horario, agregue 3 al rotarÁngulo.
    # Si no, reste 3.
    if (tierra.dirección == 'sentido-horario'):
        tierra.rotarÁngulo += 2
        marte.rotarAngulo += 1.5
        mercurio.rotarAngulo += 3
        venus.rotarAngulo += 2.5
        jupiter.rotarAngulo += 1
    else:
        tierra.rotarÁngulo -= 2
        marte.rotarAngulo -= 1.5
        mercurio.rotarAngulo -= 3
        venus.rotarAngulo = 2.5
        jupiter.rotarAngulo -= 1

    # Incremente el número de puntos del sol por 1.
    sol.puntos += 1

cmu_graphics.run()