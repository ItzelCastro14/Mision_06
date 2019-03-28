#Autor: Itzel Yanabany Castro Becerril
# Hacer fujuras geometricas basadas en circulos
import math

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul


# Estructura básica de un programa que usa pygame para dibujar
#def dibujarCirculo(ventana):
    #radio= 100
    #for angulo in range (0,360+1,1):
        #a=math.radians(angulo)
        #x=int(radio*math.cos(a))
        #y=int(radio*math.sin(a))
        #pygame.draw.circle(ventana,ROJO,(x+ANCHO//2 ,y+ALTO//2),1)

def dibujarCirculos(ventana,radio,R,L):
    anguloTheta=radio//math.gcd(radio,R)
    k=radio/R

    for angulo in range(0,361*anguloTheta,1):
        a=math.radians(angulo)
        x=R*((1-k)*math.cos(a)+L*k*math.cos((1-k)/k*a))
        y=R*((1-k)*math.sin(a)-L*k*math.sin((1-k)/k*a))
        pygame.draw.circle(ventana,ROJO,(int(x)+ANCHO//2,int(y)+ALTO//2),1)



def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        #dibujarCirculo(ventana)
        dibujarCirculos(ventana,65,220,0.8)



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()