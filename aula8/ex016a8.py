# Crie um programa que leia im numero real qualquer pelo teclado e mostre na tela sua porção inteira
# ex: o número 6,153 tem como parte inteira 6

# #1a forma: Fazendo o import de math completo.

# import math 
# num = float(input("Digite o número: "))
# print("a parte inteira de {} é: {}".format(num,math.trunc(num)))


# #2a Forma: importanto apenas o necessário.

# from math import trunc, ceil, floor
# num = float(input("Insira o valor: "))
# print("A parte inteira de {} é {}\n".format(num, trunc(num))) 
# print("Arredondando {} para cima fica: {}\n".format(num, ceil(num)))
# print("Arredondando {} para baixo fica: {}\n".format(num, floor(num)))


#3a Forma: utilizando a função "int". 
num = float(input("Insira o valor: "))
print("A parte inteira de '{}' é '{}'.".format(num, int(num)))