import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
print("⚠ Esse prompt foi feito apenas para Numeros Inteiros! \n")

numero = int(input("Digite um número: "))

dobro = numero * 2 # Multiplicação por 2.
triplo = numero * 3 # Multiplicação por 3.
raiz = numero ** (1/2) # Raiz quadrada do número.

print("")
print("O número informado é {}.\n\nO seu dobro vale {}, triplo {} e sua raiz quadrada vale {}".format(numero,dobro,triplo,raiz))
print("")
print('-'*80)