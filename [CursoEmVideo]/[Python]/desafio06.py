
import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
print("⚠ Esse prompt foi feito apenas para Numeros Inteiros! \n")

numero = int(input("Digite um número Inteiro: "))

print("")
print("O número informado é {}. Seu antecessor é {} e seu sucessor é {}".format(numero,numero - 1, numero + 1))
print("")
print('-'*80)

