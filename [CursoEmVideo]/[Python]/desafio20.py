import math, time, random

import os
os.system('cls' if os.name == 'nt' else 'clear')


alunos = ["Ana Julia", "Matheus", "Paloma", "Antonio", "Luana", "Kaique", "Tomaz", "Isabelly", "Thayssa", "Pacheco", "Mariana"]

print('-'*80)
print("")
print(f" A lista de alunos é: {', '.join(alunos)}")  # Exibe os nomes separados por vírgula
print("")

print("Aguarde um momento, estamos sorteando um aluno...")
time.sleep(5)

sorteio = random.choice(alunos)  # Sorteia um aluno da lista
print("")
print(f"O aluno sorteado foi {sorteio}")
print("")
print('-'*80)
