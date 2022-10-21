def run ():
    
    #EJEMPLO CONTADOR 1

   # for contador in range(1000):
   #     if contador % 2 != 0:
   #         continue
   #     print(contador)
    
    #EJEMPLO CONTADOR 2, CON PALABRA BREAK

    #for i in range(10000):
    #    print(i)
    #    if i == 5678:
    #        break

    texto = input('Escribe un texto: ')
    for letra in texto: 
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()