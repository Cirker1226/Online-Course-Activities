
import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

primeiro_valor = int(input("Qual é o primeiro valor? "))
segundo_valor = int(input("Qual é o segundo valor? "))

somatorio = primeiro_valor + segundo_valor

print("")
print("O Somatorio dos dois valores é: {}".format(somatorio))
print("")
print("-" * 80)