#AULA 4 - EXERCICIOS
#JOAO PEDRO GOMES PINHEIRO

#EXEMPLO
print('exemplo')
def do_twice (f): 
    f () 
    f ()

def print_spam (): 
    print('spam') 

do_twice (print_spam)

#EXERCICIO 1
print('-----------')
print('exercicio 1')
#Modifique do_twice para que sejam necessarios dois argumentos, um objeto de funcao e um valor, e chame a funcao duas vezes, passando o valor como um argumento. Escreva uma versão mais geral de print_spam, chamada print_twice, que use uma string como parâmetro e imprima duas vezes.  Use a versao modificada do do_twice para chamar print_twice duas vezes, passando 'spam' como um argumento. 
#do_twice2 -> versao modificada do do_twice

def do_twice2 (f,x): 
    f (x) 
    f (x)

def print_twice (string): 
    print(string)
    print(string)

do_twice2(print_twice,'spam') 

#EXERCICIO 2
print('-----------')
print('exercicio 2')
#Defina uma nova função chamada do_four que recebe um objeto de função e um valor e chama a função quatro vezes, passando o valor como um parâmetro. Deve haver apenas duas declarações no corpo desta função, não quatro.
def do_four (f,x):
    do_twice2(f,x)
    do_twice2(f,x)

do_four(print_twice,'spam')

#EXERCICIO 3
print('-----------')
print('exercicio 3')
#Write a function that draws a grid like the following:
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +
#|         |         |
#|         |         |
#|         |         |
#|         |         |
#+ - - - - + - - - - +
def printonly(palavra):
    print(palavra)

def line():
    print('+','-'*5,'+','-'*5,'+')

def grid():
    line()
    do_four(printonly,'\       \       \ ')
    line()
    do_four(printonly,'\       \       \ ')
    line()

grid()

#exercício 4
print('exercício 4: ')
print(time.localtime())

print('-------------')

#exercício 5
print('exercício 5: ')
def fatorial(n):
	fatorial=1

	for i in range(n):
		fatorial=fatorial*(i+1)
	return fatorial

print ('o fatorial do número 6 é =',fatorial(6))

print('-------------')

#exercício 6
print('exercício 6: ')
def comparar(a,b):
	if (a>b):
		print ('o número ',a,'é maior que o número',b)	
		print ('o número maior é = ',a)	
	if (a<b):
		print ('o número ',a,'é menor que o número',b)
		print ('o número maior é = ',b)	
	if (a==b):
		print ('o número',a,'é igual ao número',b)
#Escrevendo um exemplo
comparar(10,11)

print('-------------')

#exercício 7
print('exercício 7: ')
def comparar(a,b):
	if (a>b):
		print ('(',b,', ',a,')')	
	if (a<b):
		print ('(',a,', ',b,')')	
	if (a==b):
		print ('(',a,', ',b,')')	
#Escrevendo um exemplo
comparar(17,12)
