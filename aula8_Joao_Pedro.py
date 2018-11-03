#AULA 8
#JOÃO PEDRO GOMES PINHEIRO
#03 de novembro de 2018

import math

#EXERCÍCIO 1
print('Exercício 1: ')

n = 600

while (n>1):
	print(n)
	if n % 2 == 0:
		n = n/2
	elif  n % 2 == 1 and n != 1:
		n=3*n+1

print(n)

#EXERCÍCIO 2
print('Exercício 2: ')

def counter(n):
	count  =  0
	while  n!=0:
		if n % 5 == 0:
			count = count + 1
		n = n // 10
	return count

print(counter(710580))

#EXERCÍCIO 3
print('Exercício 3: ')

def par_impar(lista):
	for i in range(len(lista)):
		if lista[i] % 2 == 1:  # If the number is odd
			print(lista[i], 'é ímpar')
		elif lista[i] % 2 == 0:  # If the numbar isn't odd	
			print(lista[i], 'é par')

lista = [3,6,4,56,12,75,2,8,13,65,87]
par_impar(lista)

#EXERCÍCIO 4
print('Exercício 4: ')
def raiz_quadrada(lista):
	for i in range(len(lista)):
		n = lista[i]/2
		while (n**2 - lista[i]) > 0.001:
			n = n - (n**2-lista[i])/(2*n)
		print('a raiz quadrada de ', lista[i], 'é: ', n)

lista = [6, 16, 19, 25, 36]
raiz_quadrada(lista)