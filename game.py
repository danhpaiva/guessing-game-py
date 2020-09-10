import os
import random

tentativas = 0
numeroSorteado = random.randrange(0, 100)
letras = "abcdefghijklmnopqrstuvxz"

print("Jogo de Adivinhação\n")
print("Sorteando número... Número sorteado!!!")

numeroDigitado = input("Digite seu número para tentar adivinhar qual número foi sorteado: ")
while numeroDigitado not in numeros:
    numeroDigitado = input("Digite seu número para tentar adivinhar qual número foi sorteado: ")


while numeroDigitado != numeroSorteado:
    os.system("cls")
    if numeroSorteado > numeroDigitado:
        print("O número sorteado é maior...")
    elif numeroSorteado < numeroDigitado:
        print("O número sorteado é menor...")
    tentativas += 1
    numeroDigitado = int(input("Digite seu número: \n"))

print("Número: " + str(numeroDigitado) + ", você precisou de " +
      str(tentativas + 1) + " tentativas.")
