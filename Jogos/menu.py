import adivinhacao
import forca

print("*********************************")
print("***Bem vindo ao menu de jogos!***")
print("*********************************\n")

print("Escolha um jogo!")
escolha = int(input("(1) forca (2) adivinhacao:"))

if(escolha == 1):
    forca.jogar()
elif(escolha == 2):
    adivinhacao.jogar()
