import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
print("⚠ Esse prompt foi feito apenas para Numeros Inteiros! \n")

largura = int(input("Porfavor digite a largura da parede em metros: "))
altura = int(input("Porfavor digite a altura da parede em metros: "))

area = largura * altura

tinta = area / 2

print("")
print("A área da parede é de {} metros quadrados e você precisará de {} litros de tinta para pintá-la.".format(area,tinta))
print("")   
print('-'*80)