# Faça um programa que leia a LARGURA e a ALTURA de uma parede em metros, calcule sua area e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta 2m

larg = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))

area = larg*alt
litro = area/2

print("Sua parede tem {:g}x{:g} e precisará de {:g}L de tinta.".format(larg, alt, litro))