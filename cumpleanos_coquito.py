import time
import sys

NOMBRE_AMIGO = "COQUITO"      
EDAD = 25                  
DE_PARTE_DE = "PREPUCIO"   


vida = 100
ubicacion = "inicio"
jugando = True
inventario = []


#ESTO ES PARA ESCRIBIR EL TEXTO CARACTER POR CARACTER 
def escribir(texto, velocidad=0.03):
    for caracter in texto:
        sys.stdout.write(caracter) #escribe el caracter sin agregar salto automatico como print()
        sys.stdout.flush() #flush fuerza a que se muestre caracter por caracter
        time.sleep(velocidad) #Pausa entre cada letra
    print()


def pedir_opcion(opciones):
    """Muestra las opciones y devuelve el numero elegido (sin romperse si escriben otra cosa)."""
    print()
    for i, texto in enumerate(opciones, start=1):
        print(f'{i}. {texto}')
    while True:
        respuesta = input('\nIntroduce el numero de tu respuesta: ').strip()
        if respuesta.isdigit() and 1 <= int(respuesta) <= len(opciones):
            return int(respuesta)
        escribir('Opcion invalida. Intenta de nuevo.')


def estado():
    objetos = ', '.join(inventario) if inventario else 'nada'
    print(f'\n[ Vida: {vida} | Inventario: {objetos} ]')


def pastel():
    print(r"""
            ) ) )
           ( ( (
          i i i i
        .-i-i-i-i-.
        |^^^^^^^^^|
        | FELIZ   |
        |  CUMPLE |
      __|_________|__
     |~~~~~~~~~~~~~~~|
     |_______________|
    """)


# ================= INTRO =================
print('=' * 55)
print(f'   LA AVENTURA DE {NOMBRE_AMIGO.upper()}  -  Edicion Cumpleanos #{EDAD}')
print('=' * 55)
input('\nPresiona ENTER para comenzar...')

escribir(f'\n{NOMBRE_AMIGO}, hoy es un dia especial... pero parece que alguien te ha tendido una trampa.')
escribir('Estas perdido en un terreno desconocido en busca de un tesoro. ')
escribir('\nTu unico objetivo de momento es buscar una salida.')

# ================= JUEGO =================
while jugando:
    if vida <= 0:
        escribir('\nTus fuerzas se agotan y todo se vuelve oscuro...')
        print('Has muerto. Fin del juego')
        escribir(f'(Tranquilo {NOMBRE_AMIGO}, ni en la muerte se acaba tu cumpleanos. Vuelve a intentarlo.)')
        jugando = False

    elif ubicacion == "inicio":
        estado()
        escribir('\nLogras visibilizar un camino con tres rutas. Se escucha agua a lo lejos...')
        opcion = pedir_opcion(['Ir al bosque', 'Ir a la montaña', 'Seguir el sonido del rio'])

        if opcion == 1:
            ubicacion = "bosque"
        elif opcion == 2:
            ubicacion = "montaña"
        else:
            ubicacion = "rio"

    elif ubicacion == "rio":
        if 'antorcha' not in inventario:
            escribir('\nLlegas a un rio de aguas cristalinas. En la orilla hay una antorcha abandonada, aun util.')
            opcion = pedir_opcion(['Tomar la antorcha', 'Beber agua y volver al inicio'])
            if opcion == 1:
                inventario.append('antorcha')
                escribir('Guardas la antorcha. Quien sabe, quiza te sirva mas adelante.')
            else:
                vida = min(100, vida + 10)
                escribir('El agua fresca te revitaliza. Ganas 10 puntos de vida.')
            ubicacion = "inicio"
        else:
            escribir('\nEl rio sigue murmurando tranquilo. Ya no hay nada mas por aqui.')
            ubicacion = "inicio"

    elif ubicacion == "bosque":
        estado()
        escribir('\nCaminas a traves de la vegetacion cuando de repente escuchas ruido en los arbustos. \nEscuchas unos gruñidos... terminan por salir una jauria de lobos')
        escribir('\nTienes varias alternativas: ')

        opciones = ['Pelear', 'Huir']
        if 'antorcha' in inventario:
            opciones.append('Agitar la antorcha')
        opcion = pedir_opcion(opciones)

        if opcion == 1:
            vida = vida - 30
            escribir('El lobo te ha mordido. \nPierdes 30 puntos de vida.')
            print(f'Ahora tienes: {vida} puntos de vida.')
            if vida > 0:
                escribir('Logras abrirte paso entre la jauria y corres hacia una cueva...')
                ubicacion = "cueva"
        elif opcion == 2:
            escribir('Huyes de vuelta al inicio')
            ubicacion = "inicio"
        else:
            escribir('Agitas la antorcha frente a los lobos. Retroceden asustados y huyen entre los arboles.')
            escribir('Sin un solo rasguño, descubres la entrada de una cueva al fondo del sendero.')
            ubicacion = "cueva"

    elif ubicacion == "montaña":
        estado()
        escribir('\nEncuentras un cofre en la montaña')
        opcion = pedir_opcion(['Abrirlo', 'Ignorarlo y seguir subiendo'])

        if opcion == 1:
            if 'llave dorada' in inventario:
                escribir('El cofre ya esta vacio. Solo queda polvo y silencio.')
                ubicacion = "cima"
            else:
                escribir('Dentro del cofre no hay oro... solo una llave dorada con una nota:')
                escribir('"El verdadero tesoro esta detras de una puerta en la oscuridad."')
                inventario.append('llave dorada')
                escribir('\nGuardas la llave y decides seguir subiendo.')
                ubicacion = "cima"
        else:
            ubicacion = "cima"

    elif ubicacion == "cueva":
        estado()
        if 'llave dorada' in inventario and 'antorcha' in inventario:
            escribir('\nEntras a la cueva. Tu antorcha ilumina una enorme puerta de madera con una cerradura dorada.')
            escribir('Sacas la llave... encaja perfecto.')
            escribir('\nLa puerta se abre lentamente...')
            time.sleep(1)
            escribir('\n¡SORPRESA!', 0.08)
            pastel()
            escribir(f'¡FELIZ CUMPLEAÑOS {NOMBRE_AMIGO.upper()}! Hoy cumples {EDAD} y el verdadero tesoro eran tus amigos.', 0.04)
            escribir('Esta aventura fue hecha especialmente para ti.')
            escribir(f'\n  - Con cariño, {DE_PARTE_DE}')
            print('\n*** FINAL SECRETO: EL TESORO DEL CUMPLEAÑERO ***')
        elif 'llave dorada' in inventario:
            escribir('\nEntras a la cueva, pero esta demasiado oscura. Tocas una puerta con la mano, pero sin luz no puedes ver la cerradura.')
            escribir('Regresas a tientas hasta la salida. (Quiza necesites algo para iluminar el camino...)')
            ubicacion = "inicio"
        else:
            escribir('\nEncuentras la salida y sales sano y salvo')
            print('Fin de la aventura')
            escribir('(Pero algo te dice que te perdiste de algo mas grande...)')
            jugando = False
        if ubicacion == "cueva":
            jugando = False

    elif ubicacion == "cima":
        estado()
        escribir('\nHas llegado a la cima y ves un hermoso amanecer... De igual forma puedes ver el camino de vuelta a casa')
        opcion = pedir_opcion(['Quedarte a disfrutar el amanecer', 'Bajar y seguir buscando el tesoro'])
        if opcion == 1:
            print('\nHas completado la aventura')
            escribir('(Pero... ¿y si el tesoro seguia por ahi abajo?)')
            jugando = False
        else:
            escribir('Bajas de la montaña con nuevas fuerzas.')
            ubicacion = "inicio"