import os
os.system('cls' if os.name == 'nt' else 'clear')

print("")
print('-'*80, "\n")
print("⚠ Esse prompt foi feito apenas para Numeros Inteiros! \n")

primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))
terceiro_valor = int(input("Digite o terceiro valor: "))

print("")

# Verifica o menor valor entre os três números

if primeiro_valor < segundo_valor and primeiro_valor < terceiro_valor:
    menor = primeiro_valor
elif segundo_valor < primeiro_valor and segundo_valor < terceiro_valor:
    menor = segundo_valor
else:
    menor = terceiro_valor

# Verifica o maior valor entre os três números

if primeiro_valor > segundo_valor and primeiro_valor > terceiro_valor:
    maior = primeiro_valor
elif segundo_valor > primeiro_valor and segundo_valor > terceiro_valor:
    maior = segundo_valor
else:
    maior = terceiro_valor

print(f"O menor valor é {menor} e o maior valor é {maior}!")
print("")
print('-'*80)
