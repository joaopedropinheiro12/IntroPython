#AULA 10
#07 de novembro de 2018

#EXERCÍCIO 1
print('EXERCÍCIO 1: ')
def dobrar_elementos (uma_lista):
    """ Reescreve os elementos de uma_lista em outra_lista com o dobro de seus valores originais.
    """
    outra_lista = []
    for (valor) in uma_lista:
        novo_elem = 2 * valor
        outra_lista.append(novo_elem)

    return outra_lista

minha_lista = [2, 4, 6]
print(minha_lista)
outra_lista = dobrar_elementos(minha_lista)
print(outra_lista)

#help(dobrar_elementos)

#EXERCÍCIO 2
print('EXERCÍCIO 2: ')

num = [1]
for i in range(1,10000):
	num.append(num[i-1]+1)

print(num)

#EXERCÍCIO 3
print('EXERCÍCIO 3: ')

n = input('escolha um número maior do que 101: ')
n = int(n)

while n<101:
	n = input('INSIRA UM NÚMERO MAIOR QUE 101: ')
	n = int(n)

for i in range (101,n):
	if i%21 == 0:
		print('o menor número entre 101 e', n, 'divisível por 21 é:', i)
		break


#EXERCÍCIO 4
print('EXERCÍCIO 4: ')

linha1 = [-1,0,0,0]
linha2 = [0,1,0,0]
linha3 = [0,0,1,0]
linha4 = [0,0,0,1]

matriz = [linha1,linha2,linha3,linha4]
print(chr(951),'=')
for i in range(0,4):
	print(matriz[i])
	
print('o elemento 3x3 da matriz', chr(951),'é:', matriz[3][3])
