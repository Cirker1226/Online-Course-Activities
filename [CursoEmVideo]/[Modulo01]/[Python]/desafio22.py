import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
nome = str(input("Digite seu nome completo: "))
print("")

print('-'*80)
print("")

print(f"Seu nome em Letras maiúsculas é: {nome.upper()} \n") # Upper Converte o nome para letras maiúsculas

print(f"Seu nome em Letras minúsculas é: {nome.lower()} \n") # Lower Converte o nome para letras minúsculas

print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras \n") # O len conta o número de caracteres e subtrai pelo
                                                                       # nome.count(' ') que conta o número de espaços

print(f"Seu primeiro nome tem {nome.find(' ')} letras \n")

print('-'*80)