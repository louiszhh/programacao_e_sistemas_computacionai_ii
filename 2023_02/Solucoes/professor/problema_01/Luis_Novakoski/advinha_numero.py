# O programa pensa num numero de N digitos e o usuario deve advinhar
# o numero em 10 tentativas

import random

NUM_DIGITOS = 4
NUM_TENTATIVAS = 10

def main():
    numero_usuario = str(int(input('Digite um numero com {} digitos! '.format(NUM_DIGITOS))))
    
    numero_aleatorio = pensa_numero_aleatorio()

    if numero_usuario == numero_aleatorio:
        print("Voce venceu!")

def pensa_numero_aleatorio():
    possiveis_numeros = list('0123456789')
    random.shuffle(possiveis_numeros)
    lista_numeros = possiveis_numeros[0:NUM_DIGITOS]

    numero_aleatorio = ''

    for numero in lista_numeros:
        numero_aleatorio += str(numero)

    return numero_aleatorio
       
    
if __name__ == '__main__':
    main()    