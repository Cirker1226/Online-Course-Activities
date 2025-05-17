import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
nome = str(input("Porfavor digite o seu nome Completo! "))
print("")

nome = nome.split() # Coloca em lista de palavras

print("Olá, muito prazer em te conhecer!")
print(f"Seu primeiro nome é {nome[0]}!") # Nome[0] = Primeiro nome
print(f"Seu último nome é {nome[-1]}!") # Nome[-1] = Último nome

# No Curso ele fez o ultimo nome com nome[len(nome)-1].

print("")
print('-'*80)

