
#7. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

for i in range(1, 51):  # Inicia um loop que vai de 1 a 50
    if i % 2 != 0:  # Verifica se o número atual (i) é ímpar, ou seja, se o resto da divisão por 2 é diferente de zero
	    print(i)  # Imprime o número ímpar
