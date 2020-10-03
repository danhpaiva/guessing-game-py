import os
import random


def introducePlayer(playerName):
    os.system("cls")
    print("Jogo de Adivinhação\n")
    print(playerName + " estamos sorteando o número... Número sorteado!!!")

def getTipAboutSelectedNumber(randomNumber, selectedNumber):
    if randomNumber > selectedNumber:
        print("\tO número sorteado é maior...")
    elif randomNumber < selectedNumber:
        print("\tO número sorteado é menor...")

def searchNumber():
    attemps = 1
    selectedNumber = input("Digite um número para tentar adivinhar qual número foi sorteado por nossa máquina: ")
    randomNumber = random.randrange(0, 100)

    while selectedNumber != randomNumber:
        os.system("cls")
        if not selectedNumber.isnumeric():
            selectedNumber = input("Digite um número para tentar adivinhar qual número foi sorteado por nossa máquina: ")
        getTipAboutSelectedNumber(randomNumber, int(selectedNumber))
        selectedNumber = input("Digite outro número: \n")
        attemps += 1
    print("\nNúmero: " + str(selectedNumber) + ", você precisou de " + str(attemps) + " tentativas.")

def main():
    introducePlayer(input("Primeiro, nos diga seu nome: "))
    searchNumber()

if __name__ == "__main__":
    main()


