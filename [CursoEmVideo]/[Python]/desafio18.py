from math import sqrt

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
print("⚠ Esse prompt foi feito apenas para Numeros Inteiros! \n")

oposto = int(input("Porfavor digite o valor do cateto oposto: "))
adjacente = int(input("Porfavor digite o valor do cateto adjacente: "))
print("")

hipotenusa = (oposto**2 + adjacente**2)
hipotenusa = sqrt(hipotenusa)

# Outra opção de fazer a hipotenusa
# hipotenusa = math.hypot(oposto, adjacente)

print(f"A hipotenusa é igual a aproximadamente {hipotenusa:.2f}")
print("")
print('-'*80)