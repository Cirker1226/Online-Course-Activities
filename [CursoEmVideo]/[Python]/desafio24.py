import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
cidade = str(input("Digite o nome da sua cidade: ")).strip() # Strip meio que ignora os espaços!
print("")

print("Começa com SANTO?", cidade[:5].upper() == "SANTO") # Verifica se os 5 primeiros caracteres da string são iguais a "SANTO".
print("")
print('-'*80)