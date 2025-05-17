
import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-' * 80)
print("")

algo = input("Oque voce deseja digitar? ")

print("")
print("O Tipo primitivo do que voce digitou na linguagem python é {}".format(type(algo)))
print("")

print("Só tem espaços? {}".format(algo.isspace()))
print("É numerico? {}".format(algo.isnumeric()))
print("É alfabetico? {}".format(algo.isalpha()))
print("É alfanumerico? {}".format(algo.isalnum()))
print("Está em Maiusculas? {}".format(algo.isupper()))
print("Está em Minusculas? {}".format(algo.islower()))
print("Está capitalizada? {}".format(algo.istitle()))

# isspace = Verifica se a string contém apenas espaços em branco
# isnumeric = Verifica se a string contém apenas números
# isalpha = Verifica se a string contém apenas letras do alfabeto (sem espaços ou números)
# isalnum = Verifica se a string contém apenas letras e/ou números (sem símbolos ou espaços)
# isupper = Verifica se a string contém apenas letras maiúsculas
# islower = Verifica se a string contém apenas letras minúsculas
# istitle = Verifica se a string está no formato de título (cada palavra começa com maiúscula)

print("")
print('-' * 80)