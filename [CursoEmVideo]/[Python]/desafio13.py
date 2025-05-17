import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")

preço = float(input("Porfavor, digite o preço do produto: R$").replace(',','.'))

desconto = (preço * 5) / 100
valor = preço - desconto

print("")
print("O valor do produto com 5% de desconto é R${:.2f}".format(valor))
print("")
print('-'*80)

# {:.2f} formata o valor para duas casas decimais flutuantes.