#4. Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.

numero = int(input("Digite um número para ver sua tabuada: "))  # Solicita ao usuário que insira um número e o converte para inteiro

print(f"Tabuada de {numero}:")  # Imprime o cabeçalho da tabuada indicando qual número está sendo usado

for contador in range(1, 11):  # Loop que itera de 1 a 10
    resultado = numero * i  # Multiplica o número digitado pelo valor de i (um erro, deveria ser 'contador' em vez de 'i')
    print(f"{numero} x {contador} = {resultado}")  # Imprime a expressão da tabuada no formato "número x contador = resultado"
