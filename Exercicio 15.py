#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Digite o valor base: "))  # Solicita ao usuário que insira o valor base e o converte para inteiro
expoente = int(input("Digite o expoente: "))  # Solicita ao usuário que insira o expoente e o converte para inteiro
result = 1  # Inicializa o resultado como 1

for i in range(expoente):  # Loop que itera sobre o intervalo de 0 a expoente - 1
    if base == 1:  # Verifica se a base é igual a 1
        result = base  # Se sim, o resultado recebe o valor da base
    else:
        result *= base  # Se não, multiplica o resultado pela base (eleva a base ao expoente)

print(f"Resultado {result}")  # Imprime o resultado da operação de exponenciação