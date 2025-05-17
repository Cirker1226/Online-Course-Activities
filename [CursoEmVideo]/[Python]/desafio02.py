import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

dia = input("Qual é o dia que voce nasceu? ")
mes = input("Qual é o mes (NOME DO MES) que voce nasceu? ")
ano = input("Qual ano voce nasceu? ")

print("")

# print('Voce nasceu no dia',dia,'de',mes,'de',ano,'! Correto?')

print('Voce nasceu no dia {} de {} de {}, Correto?'.format(dia, mes, ano))
print("")
print('-' * 80)