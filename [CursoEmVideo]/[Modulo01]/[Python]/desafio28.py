import os
os.system('cls' if os.name == 'nt' else 'clear')

import time
from random import randint

computador = randint(0,10) # Número aleatório entre 0 e 10
print('-'*80, "\n")
print("Vou pensar em um número entre 0 e 10. Tente adivinhar... \n")
print('-'*80, "\n")

jogador = int(input("Qual número eu pensei? "))

print("Processando Informações... \n")
time.sleep(3)

if jogador == computador:
    print("Parabéns! Você acertou!")
else:
    print(f"Você errou! O número que eu pensei foi {computador}!")

print("")
print('-'*80)