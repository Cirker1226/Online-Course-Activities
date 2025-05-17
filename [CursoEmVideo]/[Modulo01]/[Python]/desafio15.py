import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
print("⚠ Esse prompt foi feito apenas para Numeros Inteiros! \n")

temp = int(input("Qual é a temperatura em CELSIUS a ser convertida? "))

formula = (temp * 9/5) + 32

print("")
print("O valor de {}°C em fahrenheit é de {}°F".format(temp,formula))
print("")
print('-'*80)

# OBS Formula retirada do google! A TC/5 = TF - 32/9 não funcionou!