import random

NUM_DIGITS = 3
MAX_GUESSES = 10 
NUM = 145 #Exemplo mais simples

def main():
    print(''' 
          Número Secreto é um jogo de Adivinhação!
          
          Estou pensando em um número com {} dígitos com números não repetidos. 
          Tente adivinhar qual é o número. Aqui vão algumas dicas:
          Quando eu digo:   Isso significa:
          Pico              Um dígito está correto mas na posição errada
          Fermi             Um dígito está correto e na posição correta
          Bagels            Nenhum dígito está correto

          Por exemplo, se o número secreto for 248 e seu chute for 843, a dica será
          Fermi Pico.'''.format(NUM_DIGITS))

    controle_de_execucao = 0

    while True:
            numero_do_usuario = str(input("Digite um numero com tres digitos"))
            
            controle_de_execucao != 1

            if verifica_numero_valido(numero_do_usuario):
                verificao_igualdade(numero_do_usuario)
        
            if controle_de_execucao > MAX_GUESSES:
                break
        
        # Como verificar as posicoes dos numeros do usuario com o numero para advinhar?

# defino minhas funcoes
def verifica_numero_valido(numero):
        if len(numero) == 3:
            print("O numero eh valido")            
        else:
            print("O numero nao eh valido")

if __name__ == '__main__':
    main()
