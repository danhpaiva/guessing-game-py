import os
import random

numeroSorteado = random.randrange(0, 100)

def introducePlayer():
    os.system("cls")
    print("Jogo de Adivinhação\n")
    nome = input("Primeiro, nos diga seu nome: ")
    print(nome + " estamos sorteando o número... Número sorteado!!!")

def getTipAboutSelectedNumber(numeroSorteado, numeroDigitado):
    if numeroSorteado > numeroDigitado:
        print("\tO número sorteado é maior...")
    elif numeroSorteado < numeroDigitado:
        print("\tO número sorteado é menor...")

def searchNumber(numeroDigitado):
    tentativas = 0

    while numeroDigitado != numeroSorteado:
        os.system("cls")
        if not numeroDigitado.isnumeric():
            numeroDigitado = input("Digite um número para tentar adivinhar qual número foi sorteado por nossa máquina: ")

        getTipAboutSelectedNumber(numeroSorteado, int(numeroDigitado))
        numeroDigitado = input("Digite outro número: \n")
        tentativas += 1

    print("\nNúmero: " + str(numeroDigitado) + ", você precisou de " + str(tentativas + 1) + " tentativas.")

introducePlayer()
searchNumber(input("Digite um número para tentar adivinhar qual número foi sorteado por nossa máquina: "))


