# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta 2m

larg=float(input("Digite a largura da parede: "))
alt=float(input("Digite a altura da parede: "))

area=larg*alt
print("A dimensão da sua parede é {:g}x{:g} e tem {:g}m2\n".format(larg,alt,area))

tinta = area/2

print("Para pintar essa parede você precisará de {:g}L de tinta\n".format(tinta))
