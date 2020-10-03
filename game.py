import os
import random
# https://fsymbols.com/generators/carty/

def introducePlayer():
    os.system("cls")
    print(r"""
    ░██████╗░██╗░░░██╗███████╗███████╗░██████╗██╗███╗░░██╗░██████╗░  ░██████╗░░█████╗░███╗░░░███╗███████╗
    ██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝██║████╗░██║██╔════╝░  ██╔════╝░██╔══██╗████╗░████║██╔════╝
    ██║░░██╗░██║░░░██║█████╗░░█████╗░░╚█████╗░██║██╔██╗██║██║░░██╗░  ██║░░██╗░███████║██╔████╔██║█████╗░░
    ██║░░╚██╗██║░░░██║██╔══╝░░██╔══╝░░░╚═══██╗██║██║╚████║██║░░╚██╗  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
    ╚██████╔╝╚██████╔╝███████╗███████╗██████╔╝██║██║░╚███║╚██████╔╝  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
    ░╚═════╝░░╚═════╝░╚══════╝╚══════╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝
    """)
    print(input("Primeiro, nos diga seu nome: ") + " estamos sorteando o número... Número sorteado!!!")

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
    introducePlayer()
    searchNumber()

if __name__ == "__main__":
    main()


