import time

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
print("⚠ Esse prompt foi feito apenas para Numeros Inteiros! \n")
numero = int(input("Porfavor digite um número: "))
print("")

print("Identifiacndo se o número é par ou ímpar...", "\n")
time.sleep(3)

if numero % 2 == 0:
    print(f"O número {numero} é par!")
else:
    print(f"O número {numero} é ímpar!")

print("")
print('-'*80)