# crie um programa que peça o preço de um produto e mostre o preço dele com 5% de desconto

price = float(input("Digite o preço do produto: "))

price_disc = price-(price*5/100)


print("O preço sem desconto: R${:.2f}.".format(price))
print("preço com desconto: R${:.2f}".format(price_disc))
