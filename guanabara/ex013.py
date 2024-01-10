# faça um programa que leia o salário de um funcionário e depois mostre o valor com aumento de 15%

sal_a = float(input("Digite o seu salário: "))

sal_n = sal_a + (sal_a*15/100)

print("Seu novo salário ficará: R${} .".format(sal_n))