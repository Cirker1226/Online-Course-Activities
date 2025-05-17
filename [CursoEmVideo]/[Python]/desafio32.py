import os, time
os.system('cls' if os.name == 'nt' else 'clear')

from datetime import date

print('-'*80)
print("")
print("⚠ Esse prompt foi feito apenas para Numeros Inteiros! \n")
ano = int(input("Porfavor digite um ano para Analisar: "))
print("")

if ano == 0: # Se o usuário digitar 0 vamos pegar o ano atual do seu sistema.
    ano = date.today().year # Pega o ano atual do sistema.

print("Verificando se o ano é bissexto...", "\n")
time.sleep(3)

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # Um ano é bissexto se for divisível por 4, mas não por 100
                                                      # exceto se for divisível por 400.
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto!")

print("")
print('-'*80)