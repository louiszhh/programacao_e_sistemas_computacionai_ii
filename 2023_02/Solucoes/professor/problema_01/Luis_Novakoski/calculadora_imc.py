def main (): #O escopo do programa está dentro da main
    print("oi")

    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura em cm: "))

    # Chamo no programa
    calcula_imc(peso, altura)
    


def calcula_imc(aviao, predio):
    imc = aviao / predio ** 2

    return imc

if __name__ == '__main__':              
    main()