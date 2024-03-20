#12. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

for i in range(999):  # Loop que itera até 999 vezes
    nota = int(input('Digite uma nota entre 0 e 10: '))  # Solicita ao usuário que insira uma nota e a converte para inteiro
    if nota >= 0 and nota <= 10:  # Verifica se a nota está dentro do intervalo de 0 a 10
        break  # Se a nota for válida, sai do loop
    else:
        print('\nValor é inválido.')  # Se a nota for inválida, imprime uma mensagem informando que o valor é inválido
