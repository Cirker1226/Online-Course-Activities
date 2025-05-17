from math import floor, trunc # Importando a função floor da biblioteca math

# O floor arredonda o número para baixo, ou seja, para o inteiro mais próximo

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)

print("")
numero = float(input("Porfavor digite um número decimal: ").replace(",","."))
print("")

print(f"O número {numero} tem a parte inteira {floor(numero)}") # O Certo era usar a função trunc de acordo com o curso!

# print(f"O número {numero} tem a parte inteira {trunc(numero)}") # Forma correta de acordo com o curso!

print("")
print('-'*80)

