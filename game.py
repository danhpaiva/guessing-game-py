import os
import random
# link for styles https://fsymbols.com/generators/carty/


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
    print(input("Primeiro, nos diga seu nome: ") +
          " estamos sorteando o número... Número sorteado!!!")


def getTipAboutSelectedNumber(randomNumber, selectedNumber):
    if randomNumber > selectedNumber:
        print("\tO número sorteado é maior...")
    elif randomNumber < selectedNumber:
        print("\tO número sorteado é menor...")


def searchNumber():
    attemps = 1

    randomNumber = random.randrange(0, 100)

    selectedNumber = int(input(
        "\nDigite um número para tentar adivinhar qual número foi sorteado por nossa máquina: "))

    while selectedNumber != randomNumber:
        os.system("cls")
        getTipAboutSelectedNumber(randomNumber, int(selectedNumber))
        selectedNumber = int(input("Digite outro número: \n"))
        attemps += 1

    os.system('cls')
    print("\nNúmero: " + str(selectedNumber) +
          ", você precisou de " + str(attemps) + " tentativas.")

    retry = int(input('\nGostaria de sortear um novo número: [1]Sim [2]Não: '))
    if retry == 1:
        searchNumber()
    else:
        print('\nAté a próxima!')


def main():
    introducePlayer()
    searchNumber()


if __name__ == "__main__":
    main()
