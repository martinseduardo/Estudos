import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************\n")

    escopo()

    print("Fim de jogo!")

def escopo():
    tentativas = int(input("Quantas tentativas deseja?"))
    numero_secreto = random.randrange(1, 101)

    for rodada in range(1, tentativas + 1):
        print("Rodada {} de {}.\n".format(rodada, tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

    correto = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    turno = rodada + 1

    if(correto):
        print("Voce acertou!")
        break
    else:
        if (maior):
            print("O numero secreto e menor!\n")
            rodada = turno
        elif (menor):
            print("O numero secreto e maior!\n")
            rodada = turno
        else:
            print("Numero invalido.\n")
            rodada = turno

if(__name__ == "__main__"):
    jogar()