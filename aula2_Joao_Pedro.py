#AULA 2
#JOÃO PEDRO GOMES PINHEIRO
#6 de outubro de 2018

import math

#exercício 1
print('exercício 1: ')
largura = 17
altura = 12.0
delimitador = "."
print("largura/2 = ",largura/2,', tipo: ',type(largura/2))
print("largura/2.0 = ",largura/2.0,', tipo: ',type(largura/2.0))
print("altura/3 = ",altura/3,', tipo: ',type(altura/3))
print("1 + 2*5 = ",1+2*5,', tipo: ',type(1+2*3))
print("delimitador*5 = ",delimitador*5,', tipo: ',type(delimitador*5))

print('-------------')

#exercício 2
print('exercício 2: ')
raio = 5
volume =(4/3)*math.pi*raio**3
print('volume = ',volume)

print('-------------')

#exercício 3
print('exercício 3: ')
preco = 24.95
preco_desc = preco - preco*0.4
n_livros = 60
envio = 3+(n_livros-1)*0.75
custo_total = preco_desc*n_livros + envio
print('custo total = ', custo_total, 'reais')

print('-------------')

#exercício 4
print('exercício 4: ')
comprimento_onda=632.8*10**(-9)
D=1.98
d=0.250*10**(-3)
delta_y=comprimento_onda*D/d
print('delta y = ',delta_y*1000,'mm')