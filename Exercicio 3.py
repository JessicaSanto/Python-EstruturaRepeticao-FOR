#3. Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0  # Inicializa a variável 'soma' com zero

# Loop para iterar sobre os 5 números
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))  # Solicita ao usuário que insira o número
    soma += numero  # Adiciona o número à variável 'soma'

media = soma / 5  # Calcula a média dos números dividindo a soma pelo número de elementos (5)

print(f"A soma dos números é: {soma}")  # Imprime a soma dos números
print(f"A média dos números é: {media}")  # Imprime a média dos números
