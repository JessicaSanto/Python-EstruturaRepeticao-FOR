#2. Faça um programa que verifique e mostre os números entre 1.000 e 2.000 (inclusive) que, quando divididos por 11 produzam resto igual a 2.

# verificar numeros
# mostrar numeros
# entre 1000 e 2000 INCLUSIVE
# quando divididos por 11, precisam ter o resto IGUAL a 2

for numero in range(1000, 2001):  # Loop que itera sobre os números de 1000 a 2000 (inclusive)
    if numero % 11 == 2:  # Verifica se o número dividido por 11 deixa um resto igual a 2
        print(numero)  # Se a condição for verdadeira, imprime o número