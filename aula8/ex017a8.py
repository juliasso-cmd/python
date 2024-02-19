# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

# # Utilizando a forma "matematica"
# co = float(input("comprimento do cateto oposto: "))
# ca = float(input("comprimento do cateto adjacente: "))
# hi = (co**2+ca**2) ** (1/2)
# print("A hipotenusa vai medir: {:.2f}".format(hi))

#Utilizando módulos:
import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = math.hypot(co,ca)
print("O valor da hipotenusa é: {}".format(hi)) 