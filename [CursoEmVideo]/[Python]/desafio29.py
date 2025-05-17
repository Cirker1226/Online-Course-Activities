import os, time
os.system('cls' if os.name == 'nt' else 'clear')

velocidade = float(input("Qual a velocidade do carro? ").replace(",", "."))

print("")
print('-'*80, "\n")

print("Analisando a velocidade do carro... \n")
print("")
time.sleep(3)

if velocidade > 80:
    print("Você está acima da velocidade limite permitida!")

    multa = (velocidade - 80) * 7
    print(f"Você deve pagar uma multa de R$ {multa:.2f}!") #.2f arredonda o numero para duas casas decimais.
    print("Dirija com cuidado!")
else:
    print("Você está dentro da velocidade limite permitida!")
    print("Continue assim e tenha um bom dia!")

print("")
print('-'*80)
