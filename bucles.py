#contador = 0 
#print('2 elevado a ' + str(contador) + ' es igual: ' + str(2**contador))

#contador = 1 
#print('2 elevado a ' + str(contador) + ' es igual: ' + str(2**contador))

#Utilizacion de memoria

def run():
    LIMITE = 1000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE: 
        print('2 elevado a ' + str(contador) + 
                ' es igual: ' + str(potencia_2))
        #Infinity Loop / Evitar bucle infinito
        contador = contador + 1
        potencia_2 = 2**contador



if __name__ == '__main__':
    run()