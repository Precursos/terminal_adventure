import time
import sys


vida = 100

ubicación = "inicio"

def escribir(texto, velocidad=0.03):
    for caracter in texto:
        sys.stdout.write(caracter) #escribe el caracter sin agregar salto automatico como print()
        sys.stdout.flush() #flush fuerza a que se muestre caracter por caracter
        time.sleep(velocidad) #Pausa entre cada letra
    print()




escribir('Por fin has despertado, no sabes como llegaste a este lugar pero parece que te encuentras en lo que parece ser un bosque.')

escribir('\nTu unico objetivo de momento es buscar una salida. \nLogras visibilizar un camino con dos rutas')
