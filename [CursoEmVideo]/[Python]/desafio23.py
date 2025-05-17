import time

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
numero = int(input("Digite um numero até 9999: "))
print("")

print('-'*80, "\n")

print(f"Analisando o número {numero}...", "\n")
time.sleep(5)

print(f"Unidade: {numero // 1 % 10}") # Divide o número por 1 e pega o resto da divisão; (% = resto)
print(f"Dezena: {numero // 10 % 10}") # Divide o número por 10 e pega o resto da divisão; (% = resto)
print(f"Centena: {numero // 100 % 10}") # Divide o número por 100 e pega o resto da divisão; (% = resto)
print(f"Milhar: {numero // 1000 % 10}") # Divide o número por 1000 e pega o resto da divisão. (% = resto)

print("\n", '-'*80)