# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle  # Importanto apenas a função "Shuffle" da Biblioteca "Random"
n1 = "Julio"
n2 = "Estefany"
n3 = "Ana Laura"
n4 = "Ollecy"

lista = [n1,n2,n3,n4]      # (Line 9) Foi criada uma lista com os nomes fornecidos, (Line 10) após isso,
shuffle(lista)             # Foi utilizada a função "Shuffle" da biblioteca "Random" para embaralhar a 
print("\n",lista,"\n")     # ordem dos nomes que foi impressa na aqui (Line 11).

