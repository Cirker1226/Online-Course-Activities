import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")

salario = float(input("Qual é o valor do seu salário? "))

aumento = (salario * 15) / 100
salario_final = salario + aumento

print("")
print("O seu novo salário com o aumento de 15% sera de R${:.2f}".format(salario_final))
print("")
print('-'*80)

# {:.2f} formata o valor para duas casas decimais flutuantes.