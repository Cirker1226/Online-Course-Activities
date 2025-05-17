import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")

nota = float(input("Porfavor digite a primeira Nota: ").replace(',','.'))
nota2 = float(input("Porfavor digite a segunda Nota: ").replace(',','.'))

media = (nota + nota2) / 2

print("")
print("A Média de suas nota é {}".format(media))
print("")
print('-'*80)

