# Importar as bibliotecas

# Definição de uma função main

def main():
    # O programa fica aqui dentro
    
    peso = float(input("Digite o seu peso : "))
    altura = float(input("Digite a sua altura : "))

    imc = calcula_imc(peso,altura)

    print(imc)

# Nossas próprias funções
def calcula_imc(peso, altura):
    imc = peso / pow(altura, 2)
    return imc 

if __name__ == '__name__':
    main()