import random as rand

def jogar():
    print("#############################")
    print("### Bem vindo ao JOGO!!! ###")
    print("#############################")

    numero_secreto = round(rand.randrange(1, 101))
    tentativas = 0
    pontos = 500

    nivel = int(input("Qual o nível de dificuldade?\n(1) Fácil (2) Médio (3) Difícil\n"))

    if nivel == 1:
        tentativas = 15
    elif nivel == 2:
        tentativas = 7
    elif nivel == 3:
        tentativas = 5

    for rodada in range(1, tentativas+1):
        print("Rodada {} de {}".format(rodada, tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou", chute)
        if chute > 100 or chute < 1:
            print("Você deve digitar um número entre 1 e 100")
            continue
        if chute == numero_secreto:         # ACERTOU
            print("VOCÊ ACERTOU!!! Você fez {} pontos\n".format(pontos))
            break
        else:
            if chute < numero_secreto:      # MENOR
                print("Seu número foi menor")
            elif chute > numero_secreto:    # MAIOR
                print("Seu número foi maior")
            elif chute != numero_secreto:   # PERDEU O JOGO
                print("Você perdeu, o número era: {}".format(numero_secreto))
            pontos -= abs(numero_secreto - chute)

    print("Fim do jogo")