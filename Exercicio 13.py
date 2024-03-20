#13. - Uma loja tem tem uma política de descontos de acordo com o valor da compra do cliente. Os descontos começam acima dos R$500. A cada 100 reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até 25%.
#Por exemplo: R$500 = 1% || R$600,00 = 2% … etc…
#Faça um programa que exiba essa tabela de descontos no seguinte formato:
#Valordacompra – porcentagem de desconto – valor final

valor = float(input('Digite o valor da compra: R$'))  # Solicita ao usuário que insira o valor da compra e o converte para float
contagem = 1  # Inicializa a variável de contagem com o valor 1

if valor >= 600 and contagem:  # Verifica se o valor da compra é maior ou igual a R$ 600 e se a contagem é diferente de zero (o que sempre será verdadeiro, pois contagem é inicializado com 1)
    reduzido = valor - 500  # Calcula o valor reduzido subtraindo R$ 500 do valor da compra
    if reduzido >= 100 or contagem <= 24:  # Verifica se o valor reduzido é maior ou igual a R$ 100 ou se a contagem é menor ou igual a 24
        for x in range(999):  # Loop que itera até 999 vezes
            contagem += 1  # Incrementa a contagem
            reduzido -= 100  # Reduz o valor reduzido em R$ 100
            if reduzido < 100 or contagem == 24:  # Verifica se o valor reduzido é menor que R$ 100 ou se a contagem é igual a 24
                break  # Se uma das condições for verdadeira, sai do loop

porcentagem = contagem / 100  # Calcula a porcentagem com base na contagem
desconto = valor * porcentagem  # Calcula o valor do desconto multiplicando o valor da compra pela porcentagem
final = valor - desconto  # Calcula o valor final da compra subtraindo o desconto do valor original
print(f'O produto de R${valor:.2f} ficará a partir de R${final:.2f} com {contagem:.0f}% de desconto.')  # Imprime o valor final da compra com desconto