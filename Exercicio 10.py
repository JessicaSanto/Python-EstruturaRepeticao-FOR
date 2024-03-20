#10. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

numeros_pares = 0  # Inicializa a contagem de números pares como zero
numeros_impares = 0  # Inicializa a contagem de números ímpares como zero

for i in range(1, 11):  # Loop que itera de 1 a 10
    numero = int(input(f"Digite o {i} numero inteiro: "))  # Solicita ao usuário que insira um número inteiro

    if numero % 2 == 0:  # Verifica se o número é par (se o resto da divisão por 2 é zero)
        numeros_pares += 1  # Se for par, incrementa a contagem de números pares
    else:
        numeros_impares += 1  # Se não for par (ou seja, for ímpar), incrementa a contagem de números ímpares

print(f"A quantidade de numeros pares é {numeros_pares} e a quantidade de impares é {numeros_impares}")  # Imprime a quantidade de números pares e ímpares
