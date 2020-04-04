import random


def play():
    welcome_text()
    load_random_keyword()
    game_rules()

    print("Fim de Jogo.")


def welcome_text():
    print("*********************************")
    print("***Bem vindo ao jogo de forca!***")
    print("*********************************\n")


def load_random_keyword():
    file = open("palavras.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    index = random.randrange(0, len(words))
    random_keyword = words[index].upper()
    return random_keyword


def game_rules():
    keyword = load_random_keyword()
    correct_letters = ["_" for letter in keyword]
    print(correct_letters)

    win = False
    lose = False
    misses = 0

    while not lose and not win:
        shot = input("Qual letra você escolhe?")
        shot = shot.strip().upper()

        if shot in keyword:
            index = 0
            for letter in keyword:
                if shot == letter:
                    correct_letters[index] = letter
                    index += 1
                else:
                    index += 1
        else:
            misses += 1
            draw_gallows(misses)

        lose = misses == 7
        win = "_" not in correct_letters
        print(correct_letters)

    if win:
        win_text()
    else:
        lose_text(keyword)


def draw_gallows(misses):
    print("  _______     ")
    print(" |/      |    ")

    if misses == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if misses == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if misses == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if misses == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if misses == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(misses == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (misses == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def win_text():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def lose_text(keyword):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(keyword))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == "__main__":
    play()
