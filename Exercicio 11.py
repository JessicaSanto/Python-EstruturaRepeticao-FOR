#11. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
#- Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
#- Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
#- A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

# recebe aumento anualmente
# foi contratado em 1995
# salario inicial de 1.000
# em 1996 recebeu 1,5%
# 97 inclusive dobro do ano anterior %

salario = float(input("Digite o salario inicial do funcionario:"))  # Solicita ao usuário que insira o salário inicial do funcionário e converte para float
percentual = 0.015  # Define o percentual de aumento inicial como 1,5%

for i in range(1996, 2025):  # Loop que itera de 1996 a 2024 (inclusive)
    aumento = salario * percentual  # Calcula o aumento salarial multiplicando o salário pelo percentual de aumento
    salario += aumento  # Adiciona o aumento ao salário
    percentual *= 2  # Dobra o percentual de aumento para o próximo ano
    print(f"Salario em {i} = {salario:.2f} ")  # Imprime o salário para o ano atual com duas casas decimais
