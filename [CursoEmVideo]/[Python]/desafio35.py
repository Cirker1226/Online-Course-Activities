import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

print("⚠ Esse prompt foi feito apenas para Numeros Inteiros!")
print("")

lado1 = int(input("Qual é o valor do primeiro Lado? "))
lado2 = int(input("Qual é o valor do segundo Lado? "))
lado3 = int(input("Qual é o valor do terceiro Lado? "))

print("")

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Os lados informados formam um triângulo!")
else:
    print("Os lados informados não formam um triângulo!")

print("")
print('-' * 80)

