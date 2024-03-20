#5. Faça um programa que mostre as tabuadas dos números de 1 a 10 usando laços de repetição.

# mostrar tabuadas
# tabuadas de 1 a 10
# usar laço de repetição

for num in range(1,11): #Laço de 1 a 10
  for i in range(1,11): #Laço para a multiplicação de 1 a 10
    print(f"{num} X {i} = {num * i}") # Imprime a expressão da tabuada no formato "num X i = resultado"
