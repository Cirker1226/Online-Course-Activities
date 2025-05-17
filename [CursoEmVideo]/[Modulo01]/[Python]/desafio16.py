import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
print("⚠ Esse prompt foi feito apenas para Numeros Inteiros! \n")

km = int(input("Quantos Km(s) foram percorridos? "))
dias = int(input("Quantos dias alugados? "))

preço_dia = dias * 60
preço_km = km * 0.15

valor_total = preço_dia + preço_km

print("")
print("O valor total a ser pago é R${}".format(valor_total))
print("")
print('-'*80)

# OBS: poderia ter juntado as formulas direto:
# valor_total = (dias * 60) + (km * 0.15)