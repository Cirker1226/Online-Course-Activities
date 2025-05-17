import os, time
os.system('cls' if os.name == 'nt' else 'clear')

print('-'*80)
print("")
frase = str(input("Porfavor digite uma frase: "))
print("")

frase = frase.upper() # Coloca a frase toda em maiúsculo.

print(f"A letra A aparece {frase.count("A")} vezes na frase!") # Count conta quantas vezes a letra A aparece na frase.
time.sleep(1)
print(f"A primeira letra A aparece na posição {frase.find("A")+1}!") # Find retorna a posição da primeira letra A na frase.
time.sleep(1)
print(f"A última letra A aparece na posição {frase.rfind("A")+1}!") # Rfind retorna a posição da última letra A na frase.

print("")
print('-'*80)