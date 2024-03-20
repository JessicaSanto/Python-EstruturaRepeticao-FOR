#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

n = int(input("Digite um número: "))  # Solicita ao usuário que insira um número e o converte para inteiro

for numeroTestado in range(1, n+1):  # Loop que itera de 1 até o número inserido pelo usuário (inclusive)
    for numeroDivisor in range(numeroTestado):  # Loop que itera de 0 até o número testado (exclusive)
        print(f"{numeroTestado} / {numeroDivisor+1} = {numeroTestado /(numeroDivisor+1)} com o resto {numeroTestado%(numeroDivisor+1)}")
        # Imprime a divisão e o resto da divisão entre o número testado e o número divisor + 1
        if numeroTestado % (numeroDivisor+1) == 0:  # Verifica se o número testado é divisível pelo número divisor + 1
            if 1 != numeroDivisor+1 != numeroTestado:  # Verifica se o número divisor + 1 é diferente de 1 e do número testado
                print("não é primo\n")  # Se sim, imprime que o número não é primo e quebra o loop interno
                break
            elif numeroDivisor+1 == numeroTestado:  # Se o número divisor + 1 for igual ao número testado
                print("número é primo\n")  # Imprime que o número é primo
