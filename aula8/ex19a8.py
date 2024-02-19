# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

n1 = "Julio"
n2 = "Estefany"
n3 = "Laura"
n4 = "Ollecy"

lista = [n1,n2,n3,n4]
escolhido = choice(lista)

print("O escolhido é: {}".format(escolhido))