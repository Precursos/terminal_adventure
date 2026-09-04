import time
import sys


vida = 100
ubicación = "inicio"
jugando = True

def escribir(texto, velocidad=0.03):
    for caracter in texto:
        sys.stdout.write(caracter) #escribe el caracter sin agregar salto automatico como print()
        sys.stdout.flush() #flush fuerza a que se muestre caracter por caracter
        time.sleep(velocidad) #Pausa entre cada letra
    print()




escribir('Por fin has despertado, no sabes como llegaste a este lugar pero parece que te encuentras en lo que parece ser un bosque.')

escribir('\nTu unico objetivo de momento es buscar una salida.')

while jugando == True:
    if vida <= 0:
        print('Has muerto. Fin del juego')
        jugando = False
        
    elif ubicación == "inicio":
        print('\nLogras visibilizar un camino con dos rutas')
        print('1. Ir a la izquierda')
        print('2. Ir a la derecha')
        opcion = int(input('introduce el numero de tu respuesta: '))

        if opcion == 1:
            ubicación = "Arbusto"
        elif opcion == 2:
            ubicación = "Rio"
        else:
            escribir("Opcion invalida. Intenta de nuevo")

    

