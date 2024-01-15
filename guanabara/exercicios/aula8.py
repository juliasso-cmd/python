# Aula 8 – Utilizando Módulos

# import math #importando pacote matemático (math)

# num = float(input("Digite o valor desejado: ")) 

# raiz = math.sqrt(num) #utilizando função "squareroot" do pacote math
# print("A raiz quadrada deste numero é: {:.2f}.".format(math.ceil(raiz)))

# -------------------------------------------------------------------- #

#importação "leve"

from math import sqrt, floor

num = float(input("Digite o valor: "))

raiz = sqrt(num)

print("A raiz quadrada de {:g} é {} ({:.3f}).".format(num,floor(raiz), raiz))

