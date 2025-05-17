import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")

dinheiro = float(input("Quantos R$ voce tem em sua carteira? ").replace(',','.'))

money = dinheiro * 5.68 # Valor do dollar hoje em maio de 2025

print("")
print("A Conversão de R${} em dollar equivale a ${:.2f}".format(dinheiro,money))
print("")
print('-'*80)

# {:.2f} formata o valor para duas casas decimais flutuantes.
