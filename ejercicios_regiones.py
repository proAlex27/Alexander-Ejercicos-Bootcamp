from cmu_graphics import *

app.fondo = 'blancoAntiguo'
Circulo(140,195,115, borde = 'black',anchuraDeBorde = 1.5)
población_total = 7600
Rotulo('PORCENTAJE DE POBLACIONES Y SUS REGIONES',200,50 , negrito= True)
# Religiones y su población
población_cristiana = 2300
población_islamica = 1900
población_hindú = 1200
población_budista = 520
población_tradicional_china = 394
población_afroamericana = 100
población_mundana = 1200

def hacerCalculo(muestra_de_población):
    calculo_1 = muestra_de_población/población_total
    calculo_2 = calculo_1 * 100
    end_angle = (calculo_2 / 100) * 360
    return end_angle

_1 = hacerCalculo(población_cristiana)
_2 = hacerCalculo(población_islamica)
_3 = hacerCalculo(población_hindú)
_4 = hacerCalculo(población_budista)
_5 = hacerCalculo(población_tradicional_china)
_6 = hacerCalculo(población_afroamericana)
_7 = hacerCalculo(población_mundana)

def crearPorciónDeGrafica(start_angle, end_angle, relleno):
    Arco(140,195,230,230,start_angle,end_angle, relleno=relleno)

crearPorciónDeGrafica(0, _1, 'verde')
Rotulo('30%', 190, 160)
crearPorciónDeGrafica(109, _2, 'rojo')
Rotulo('25%', 165, 255)
crearPorciónDeGrafica(199, _3, 'azul')
Rotulo('16%', 85, 245)
crearPorciónDeGrafica(256, _4, 'tomate')
Rotulo('7%', 50, 200)
crearPorciónDeGrafica(280, _5, 'naranja')
Rotulo('5%', 60, 165)
crearPorciónDeGrafica(299, _6, 'violetaRojoMedio')
Rotulo('1%', 30, 130)
crearPorciónDeGrafica(304, _7, 'amarillo')
Rotulo('16%', 100, 130)

def dibujarDatos(inicio_x, inicio_y, población, color):
    Rect(270, inicio_y-12.5, 25, 25, relleno=color)
    Rótulo(población ,inicio_x, inicio_y, relleno=color, borde=color, anchuraDeBorde=1)

dibujarDatos(330, 130, 'Cristianos', 'verdeOscuro')
dibujarDatos(330, 160, 'Islamicos', 'rojo')
dibujarDatos(330, 190, 'Hindúes', 'azul')
dibujarDatos(330, 220, 'Budistas', 'tomate')
dibujarDatos(335, 250, 'Chinos Tra', 'naranja')
dibujarDatos(340, 280, 'Afroreligiosos', 'violetaRojoMedio')
dibujarDatos(340, 310, 'No religiosos', 'amarillo')


Rotulo('Los valores son: 2.300 , 1.900 , 1.200 ',200,365, negrito = True)
Rotulo('520 , 394 , 100  y 1.200 .',200,380, negrito = True)

cmu_graphics.run()