import os
import random

tentativas = 0
numeroSorteado = random.randrange(0, 100)
letras = "abcdefghijklmnopqrstuvxz"

os.system("CLS")
print("Jogo de Adivinhação\n")

nome = input("Primeiro, nos diga seu nome: ")

print(nome + " estamos sorteando o número... Número sorteado!!!")

numeroDigitado = input(
    "Digite um número para tentar adivinhar qual número foi sorteado por nossa máquina: ")
while numeroDigitado in letras:
    numeroDigitado = input(
        "Digite um número para tentar adivinhar qual número foi sorteado por nossa máquina: ")

numeroDigitado = int(numeroDigitado)

while numeroDigitado != numeroSorteado:
    os.system("cls")
    if numeroSorteado > numeroDigitado:
        print("\tO número sorteado é maior...")
    elif numeroSorteado < numeroDigitado:
        print("\tO número sorteado é menor...")
    tentativas += 1
    numeroDigitado = int(input("Digite outro número: \n"))

print("\nNúmero: " + str(numeroDigitado) + ", você precisou de " +
      str(tentativas + 1) + " tentativas.")
