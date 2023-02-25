import random


def jogar():

    print("############################")
    print("### Bem vindo à FORCA!!! ###")
    print("############################")

    palavra_secreta = carrega_palavra_secreta()
    lista_acertos = ["_" for l in palavra_secreta]              # Cria lista com _ para cada letra da palavra_secreta

    vidas = 7
    enforcou = False
    acertou = False

    print("A forca é", " ".join(lista_acertos))

    while not enforcou and not acertou:
        chute = input("Chute uma letra: ").strip().upper()      # Pede chute ao jogador

        if chute in palavra_secreta:
            lista_acertos = marca_acerto(chute, palavra_secreta, lista_acertos)
        else:
            vidas -= 1
            imprime_forca(vidas)

        acertou = "_" not in lista_acertos
        enforcou = vidas == 0

        print(" ".join(lista_acertos))

    if "_" not in lista_acertos:
        imprime_mensagem_vitoria()

    if vidas == 0:
        imprime_mensagem_derrota(palavra_secreta)

    print("Fim de jogo")

def carrega_palavra_secreta():
    with open("palavras.txt", "r") as arquivo:
        palavras = [linha.strip() for linha in arquivo]

    numero = random.randrange(0, len(palavras))
    return palavras[numero].upper()

def marca_acerto(chute, palavra_secreta, lista_acertos):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            lista_acertos[index] = letra
        index += 1
    return lista_acertos

def imprime_forca(vidas):
    print("  _______     ")
    print(" |/      |    ")

    if (vidas == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (vidas == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (vidas == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (vidas == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (vidas == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (vidas == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (vidas == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vitoria():
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

def imprime_mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________      ")
    print("   /               \     ")
    print("  /                 \    ")
    print("//                   \/\ ")
    print("\|   XXXX     XXXX   | / ")
    print(" |   XXXX     XXXX   |/  ")
    print(" |   XXX       XXX   |   ")
    print(" |                   |   ")
    print(" \__      XXX      __/   ")
    print("   |\     XXX     /|     ")
    print("   | |           | |     ")
    print("   | I I I I I I I |     ")
    print("   |  I I I I I I  |     ")
    print("   \_             _/     ")
    print("     \_         _/       ")
    print("       \_______/         ")

if __name__ == '__main__':
    jogar()
