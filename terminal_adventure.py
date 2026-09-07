import time
import sys


vida = 100
ubicacion = "inicio"
jugando = True

#ESTO ES PARA ESCRIBIR EL TEXTO CARACTER POR CARACTER 
def escribir(texto, velocidad=0.03):
    for caracter in texto:
        sys.stdout.write(caracter) #escribe el caracter sin agregar salto automatico como print()
        sys.stdout.flush() #flush fuerza a que se muestre caracter por caracter
        time.sleep(velocidad) #Pausa entre cada letra
    print()



#Jueguito

escribir('Estas perdido en un terreno desconocido en busca de un tesoro. ')

escribir('\nTu unico objetivo de momento es buscar una salida.')

while jugando == True:
    if vida <= 0:
        print('Has muerto. Fin del juego')
        jugando = False
        
    elif ubicacion == "inicio":
        escribir('\nLogras visibilizar un camino con dos rutas')
        print('1. Ir al bosque')
        print('2. Ir a la montaña')
        opcion = int(input('introduce el numero de tu respuesta: '))

        if opcion == 1:
            ubicacion = "bosque"
        elif opcion == 2:
            ubicacion = "montaña"
        else:
            escribir("Opcion invalida. Intenta de nuevo")

    elif ubicacion == "bosque":
        escribir('Caminas a traves de la vegetacion cuando de repente escuchas ruido en los arbustos. \nEs escuchas unos gruñidos... terminan por salir una jauria de lobos')
        escribir('\nTienes dos alternativas: ')

        print('1. Pelear')
        print('2. Huír')
        opcion = int(input('Introduce el numero de tu respuesta: '))

        if opcion == 1:
            vida = vida -30
            escribir('El lobo te ha mordido. \nPierdes 30 puntos de vida.')
            print(f'ahora tienes: {vida} puntos de vida.')
            ubicacion = "cueva"
        elif opcion == 2:
            escribir('Huyes de vuelta al inicio')
            ubicacion = "inicio"
        else:
            escribir("Opcion invalida. Intenta de nuevo.")

    elif ubicacion == "montaña":
        escribir('Encuentas un cofre en la montaña')
        print('1. Abrirlo')
        print('2. Ignorarlo y seguir subiendo')
        opcion = int(input('Introduce el numero de tu respuesta: '))

        if opcion == 1:
            escribir('Encontaste un tesoro eres rico')
            jugando = False
            print('Fin del juego.')

        elif opcion == 2:
            ubicacion = "cima"
        else:
            escribir("Opcion invalida. Intenta de nuevo.")

    elif ubicacion == "cueva":
        escribir("Encuentas la salida y sales sano y salvo")
        print('FIn de la aventua')
        jugando = False

    elif ubicacion == "cima":
        escribir('Has llegado a la cima y ves un hermoso amanecer... De igual forma puedes ver el camino de vuelta a casa')
        print('Has completado la aventura')
        jugando = False

