# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Digite os Km's rodados no veículo: "))
dia = int(input("Digite quantas diárias: "))

diaria = 60*dia
kmr = km*0.15

total = diaria+kmr

print("Sua diaria ficou no valor de {} por {} dias.".format(diaria,dia))
print("kilometragem percorrida: {}, valor a pagar por km: {}".format(km,kmr))

print("Total a pagar: {}".format(total))