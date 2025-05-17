import os, time
os.system('cls' if os.name == 'nt' else 'clear')

distancia = int(input("Qual é a distância percorrida da sua viagem em Km? "))

print("-"*80)
print("")
print("⚠ Esse prompt foi feito apenas para Numeros Inteiros! \n")
print("Calculando o valor da sua passagem...", "\n")
time.sleep(3)

if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45

print(f"O valor da sua passagem é R${valor:.2f}!") #.2f arredonda o numero para duas casas decimais.
print("")
print("Tenha uma boa viagem!")
print("")
print("-"*80)