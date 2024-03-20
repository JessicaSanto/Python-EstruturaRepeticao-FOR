# - Faça um programa que receba a idade de 15 pessoas e que calcule e mostre:
#
# a) A quantidade de pessoas em cada faixa etária;
#
# b) A percentagem de pessoas na primeira e na última faixa etária, com relação ao total de pessoas:
#
# - Até 15 anos
# - De 16 a 30 anos
# - De 31 a 45 anos
# - De 46 a 60 anos
# - Acima de 61 anos

ate15 = 0  # Inicializa a contagem de pessoas até 15 anos como zero
de16a30 = 0  # Inicializa a contagem de pessoas de 16 a 30 anos como zero
de31a45 = 0  # Inicializa a contagem de pessoas de 31 a 45 anos como zero
de46a60 = 0  # Inicializa a contagem de pessoas de 46 a 60 anos como zero
mais60 = 0  # Inicializa a contagem de pessoas com mais de 60 anos como zero

for pessoa in range(15):  # Loop que itera sobre 15 pessoas
    idade = int(input(f"Digite a idade da pessoa {pessoa+1}: "))  # Solicita ao usuário que insira a idade da pessoa e a converte para inteiro
    if idade <= 15:  # Verifica se a idade da pessoa é menor ou igual a 15 anos
        ate15 += 1  # Incrementa a contagem de pessoas até 15 anos
    elif 16 <= idade <= 30:  # Verifica se a idade da pessoa está entre 16 e 30 anos (inclusive)
        de16a30 += 1  # Incrementa a contagem de pessoas de 16 a 30 anos
    elif 31 <= idade <= 45:  # Verifica se a idade da pessoa está entre 31 e 45 anos (inclusive)
        de31a45 += 1  # Incrementa a contagem de pessoas de 31 a 45 anos
    elif 46 <= idade <= 60:  # Verifica se a idade da pessoa está entre 46 e 60 anos (inclusive)
        de46a60 += 1  # Incrementa a contagem de pessoas de 46 a 60 anos
    else:  # Se a idade da pessoa for maior que 60 anos
        mais60 += 1  # Incrementa a contagem de pessoas com mais de 60 anos

# Imprime a quantidade de pessoas por faixa etária
print(f"Quantidade de pessoas por faixa etária\nAté 15 anos: {ate15} pessoas\nDe 16 a 30 anos: {de16a30} pessoas\nDe 31 a 45 anos: {de31a45} pessoas\nDe 46 a 60 anos: {de46a60} pessoas\n{((100 * ate15)/15):.2f}% das pessoas têm até 15 anos\n{((100 * mais60) / 15):.2f}% das pessoas têm mais de 60 anos")