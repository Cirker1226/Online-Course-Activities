import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
print("⚠ Esse prompt foi feito apenas para Numeros Inteiros! \n")

numero = int(input("Porfavor, digite um número: "))
multiplicador = 1

print("")

while multiplicador <= 10:
    tabuada = numero * multiplicador
    print(numero,"x",multiplicador,"=",tabuada)
    multiplicador = multiplicador + 1

print("")
print('-'*80)