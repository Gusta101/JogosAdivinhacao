import forca
import adivinhacao

print("#######################")
print("### Escolha um JOGO ###")
print("#######################")

jogo = int(input("Qual jogo?\n(1) Forca (2) Adivinhacao\n"))

if jogo == 1:
    print("Jogando FORCA")
    forca.jogar()
elif jogo == 2:
    print("Jogando Adivinhação")
    adivinhacao.jogar()