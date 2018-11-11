#Projeto 1 - Introdução a Python
#Profs: Helena Malbouisson e Clemencia Mora
#Alunos: João Pedro Gomes Pinheiro e Matheus Pereira Macedo
#Data: 14/11/2018
#PÊNDULO ELÁSTICO

import math

#Parâmetros:
print('Input de Parâmetros:')
l0 = float(input('Digite o comprimento da mola relaxada, em metros: '))
k = float(input('Digite a constante elástica da mola, em Newtons/metro: '))
m = float(input('Digite a massa do corpo, em quilogramas: '))
g = 9.81 #m/s²

#Condições Iniciais
print('\n')
print('Input das Condições Iniciais:')
x = float(input('Digite a posição inicial em x, em metros: '))
z = float(input('Digite a posição inicial em z, em metros: '))
v_x = float(input('Digite a velocidade inicial em x, em metros/segundo: '))
v_z = float(input('Digite a velocidade inicial em z, em metros/segundo: '))
print('\n')

#Valor calcular r e theta a partir das funções cal_r e calc_theta
#Definindo funções:
def calc_r(x,z):
	'''Calculando o valor de r a partir dos valores respectivos de x e z
		r = sqrt(x²+z²)
	'''
	r = math.sqrt(x*x+z*z)
	return r
def calc_theta(x,z):
	'''Calculando o valor de theta a partir dos valores respectivos de x e z
		theta = arctan(x/z)
	'''
	theta=0
	if (z<=0):
		theta = math.atan(-1*x/z)
	elif (x>=0 and z>0):
		theta = math.pi/2 + math.atan(z/x)
	elif (x<=0 and z>0):
		theta = -1*math.pi/2 + math.atan(z/x)
	return theta	

def calc_ac_x(r,theta):
	'''Calculando a aceleração em x, a partir dos parâmetros constantes e dos respectivos valores de r e theta
		aceleração_x = -1*(k*(r-l0)*sin(theta))/m
	'''
	ac_x = -1*(k*(r-l0)*math.sin(theta))/m
	return ac_x

def calc_ac_z(r,theta):
	'''Calculando a aceleração em z, a partir dos parâmetros constantes e dos respectivos valores de r e theta
		aceleração_z = -1*g+(k*(r-l0)*cos(theta))/m
	'''
	ac_z = -1*g+(k*(r-l0)*math.cos(theta))/m
	return ac_z

#Coletando o valor máximo para o tempo 
t_max = float(input('Insira o valor máximo de tempo, em segundos: '))
passo = float(input('Insira o passo do tempo, ou seja, de quanto em quanto o programa tomará uma medida (em segundos): '))
t = 0
ac_x_lista=[]
ac_z_lista=[]
v_x_lista=[]
v_z_lista=[]
x_lista=[]
z_lista=[]
t_lista=[]
print('Início do processamento dos dados')
print('\n')
while t<=t_max:
	r = calc_r(x,z)
	theta = calc_theta(x,z)
	ac_x = calc_ac_x(r,theta)
	ac_z = calc_ac_z(r,theta)
	print('x=',x,'z=',z)
	print('r =',r,'theta=',theta*180/math.pi)
	print('ac_x=',ac_x,' ac_z=',ac_z)
	print('\n')
	v_x = v_x + ac_x*passo
	v_z = v_z + ac_z*passo
	x = x + v_x*passo
	z = z + v_z*passo
	ac_x_lista.append(ac_x)
	ac_z_lista.append(ac_z)
	v_x_lista.append(v_x)
	v_z_lista.append(v_z)
	x_lista.append(x)
	z_lista.append(z)
	t = t+passo
	t_lista.append(t)

print('Fim do processamento dos dados')

import matplotlib.pyplot as XversusZ
import matplotlib.pyplot as TversusX
import matplotlib.pyplot as TversusZ
import matplotlib.pyplot as TversusVx
import matplotlib.pyplot as TversusVz
'''
print('x lista: ', x_lista)
print('z lista: ', z_lista)
print('vx lista: ', v_x_lista)
print('vz lista: ', v_z_lista)
print('ax lista: ', ac_x_lista)
print('az lista: ', ac_z_lista)
'''
XversusZ.plot(x_lista,z_lista)
XversusZ.xlabel('x (m)')
XversusZ.ylabel('z (m)')
XversusZ.show()
XversusZ.close()
