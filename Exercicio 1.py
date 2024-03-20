#1. Faça um programa que leia 5 números e informe o maior número.


#Leia 5 numeros
#Saber qual numero é o maior
#Informe o maior

maior_numero = float('-inf')  # Inicializa a variável 'maior_numero' com o menor valor possível

# Loop para iterar sobre os 5 números
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))  # Solicita ao usuário que insira o número
    if numero > maior_numero:  # Verifica se o número inserido é maior que o 'maior_numero' atual
        maior_numero = numero  # Se for maior, atualiza 'maior_numero' com o valor do número inserido

print(f"O maior número digitado é: {maior_numero}")  # Imprime o maior número após o término do loop












