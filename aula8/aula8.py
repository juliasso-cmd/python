# # Trabalhando com Módulos

# import math
# #importando o pacote math para o código
# n = int(input("Digite o número: ")) 
# # Solicitando o valor ao usuário.
# raiz = math.sqrt(n) 
# # salvando em "raiz" a raiz quadrada de "n"
# print("A raiz quadrada de {} é: {:.20f} (PADRÃO)".format(n,raiz))
# # Exibindo o valor .format(o numero fornecido pelo user, a raiz quadrada do numero fornecido)
# print("A raiz quadrada de {} é: {} (ARREDONDADA /\)".format(n,math.ceil(raiz)))
# # Exibindo o valor . format(o numero fornecido pelo user, utilizando a função de arredondamento para cima(ciel) do pacote math no valor fornecido)
# print("A raiz quadrada de {} é: {} (ARREDONDADA \/)".format(n,math.floor(raiz)))
# # Exibindo o valor . format(o numero fornecido pelo user, utilizando a função de arredondamento para baixo(floor) do pacote math no valor fornecido)


# from math import floor, sqrt, ceil

# n = int(input("Digite o valor: "))

# raiz = sqrt(n)

# print("A raiz quadrada de {} é {:.2f}".format(n,raiz))

# ------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------------------------------------ #

import random

n = random.randint(1,20)
print(n)