#9. Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja foi superior a loja B (faturamento = 54000). Se o faturamento atingir esse valor mostre na tela uma mensagem contendo em quanto foi superado o faturamento.

lojaB = 54000  # Definição do faturamento da loja B como R$ 54.000
lojaA = 0      # Inicialização do faturamento da loja A como zero

for cliente in range(5):  # Loop para iterar sobre 5 clientes
    gasto = float(input(f"Digite o gasto do cliente {cliente+1}: "))  # Solicitação do valor gasto pelo cliente e converte para float
    lojaA += gasto  # Adiciona o valor gasto pelo cliente ao faturamento total da loja A

if lojaA > lojaB:  # Verifica se o faturamento da loja A é maior que o da loja B
    print(f"A loja A superou o faturamento da loja B com um valor arrecadado maior de R${lojaA - lojaB}")  # Se sim, imprime a diferença entre os faturamentos
elif lojaB > lojaA:  # Verifica se o faturamento da loja B é maior que o da loja A
    print(f"A loja B superou o faturamento da loja A com um valor arrecadado maior de R${lojaB - lojaA}")  # Se sim, imprime a diferença entre os faturamentos
else:  # Se os faturamentos forem iguais
    print(f"As duas lojas arrecadaram o mesmo valor de R${lojaA}")  # Imprime que ambas as lojas arrecadaram o mesmo valor
