import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
print("⚠ Esse prompt foi feito apenas para Numeros Inteiros! \n")

metro = int(input("Porfavor digite um valor em Metros: "))

cm = metro * 100
mm = metro * 1000

print("")
print("O valor de {} metro(s) corresponde a {} centímetros e {} milímetros.".format(metro,cm,mm))
print("")
print('-'*80)