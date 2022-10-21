import random
from string import octdigits

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elije un numero del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('busca un número más grande')
        else:
            print('Busca un número más pequeño')
        numero_elegido = int(input('Elije otro número:'))
        print('¡Ganaste!')



if __name__ == "__main__":
    run()