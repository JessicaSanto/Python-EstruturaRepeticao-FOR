#8. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Digite um número: "))  # Solicita ao usuário que insira um número e o converte para inteiro
n2 = int(input("Digite outro número: "))  # Solicita ao usuário que insira outro número e o converte para inteiro

for i in range(n1 + 1, n2):  # Loop que itera sobre os números no intervalo entre n1 + 1 e n2
    print(i)  # Imprime cada número no intervalo

for i in range(n2 + 1, n1):  # Loop que itera sobre os números no intervalo entre n2 + 1 e n1
    print(i)  # Imprime cada número no intervalo
