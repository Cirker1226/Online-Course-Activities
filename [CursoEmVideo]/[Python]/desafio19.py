import math

import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
print("⚠ Esse prompt foi feito apenas para Numeros Inteiros! \n")

angulo = int(input("Porfavor digite o ângulo que você deseja: "))
print("")

angulo_rad = math.radians(angulo)  # Converte o ângulo de graus para radianos

# Radianos são uma unidade de medida para ângulos, dividem um círculo em 360 partes, 
# os radianos baseiam-se no comprimento do arco de um círculo.

seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print(f"O ângulo de {angulo}° tem o seno de {seno:.2f}, o cosseno de {cosseno:.2f} e a tangente de {tangente:.2f}")
print("")
print('-'*80)
