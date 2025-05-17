import os
os.system('cls' if os.name == 'nt' else 'clear')

print("")
print('-'*80, "\n")

salario = float(input("Digite o salário do funcionário: R$"))

if salario >= 1250:
    aumento = salario * (10 / 100)
else:
    aumento = salario * (15 / 100)

novo_salario = salario + aumento

print(f"O novo salário do funcionário é R${novo_salario:.2f}!")
print("")
print('-'*80)
