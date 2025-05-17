
import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")
print("⚠ Esse prompt foi feito apenas para Numeros Inteiros! \n")

primeiro_valor = int(input("Qual é o primeiro valor? "))
segundo_valor = int(input("Qual é o segundo valor? "))
terceiro_valor = int(input("Qual é o terceiro valor? "))

somatorio = primeiro_valor + segundo_valor + terceiro_valor

print("")
print("O Valor do somatorio dos tres valores ditos anteriormente é: {}".format(somatorio))
print("")
print('-' * 80)