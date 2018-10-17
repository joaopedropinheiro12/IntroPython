#AULA 2
#JOÃO PEDRO GOMES PINHEIRO
#6 de outubro de 2018

import time
import math

#exercício 1
print('exercício 1: ')
def tipo(argumento):
	print('argumento = ', argumento, ', tipo = ', type(argumento))

tipo(8)
tipo(4.4)
tipo('lulalivre')
tipo(math.pi)

print('-------------')

#exercício 2
print('exercício 2: ')

def MRU(s_inicial,s_final,intervalo_tempo):
	vm=(s_final-s_inicial)/intervalo_tempo
	print('velocidade média no MRU = ', vm)
#Escrevendo um exemplo
MRU(10,20,5)

def MRUV(v_inicial,aceleracao,intervalo_tempo):
	v_final=v_inicial+aceleracao*intervalo_tempo
	print('velocidade final no MRUV = ', v_final)
#Escrevendo um exemplo
MRUV(15,10,5)

print('-------------')

#exercício 3
print('exercício 3: ')
def ang_zenital(altura,sombra):
	ang_zenital=sombra/altura
	print('ângulo zenital = ',ang_zenital,'rad')
#Escrevendo um exemplo
ang_zenital(5,0.5)

print('-------------')

#exercício 4
print('exercício 4: ')
def milha_to_metro(milha):
	metro = milha*1609.34
	return metro
	#print('o valor ',milha,' milhas em metros é igual a ',metro,'m')
#Escrevendo um exemplo
milha_to_metro(20)

def metro_to_milha(metro):
	milha = metro/1609.34
	return milha
	#print('o valor ',metro,' metros em milhas é igual a ',milha,'milhas')
#Escrevendo um exemplo
metro_to_milha(20)

def hora_to_seg(hora):
	seg = hora*3600
	return seg
	#print('o valor ',hora,' horas em segundos é igual a ',seg,'segundos')
#Escrevendo um exemplo
hora_to_seg(5)

def seg_to_hora(seg):
	hora = seg/3600
	return hora
	#print('o valor ',seg,' segundos em horas é igual a ',hora,'horas')
#Escrevendo um exemplo
seg_to_hora(10000)

distancia_m = 10000
tempo_seg = 43*60+30
tempo_hora = seg_to_hora(tempo_seg)
distancia_milha = metro_to_milha(10000)
tempo_milha = tempo_hora/distancia_milha
velocidade = distancia_milha/tempo_milha
print('tempo por milha = ', tempo_hora,'h/milha')
print('velocidade = ', velocidade,'milha/h')

distancia_milha=4.
tempo_seg=30*60
distancia_m=milha_to_metro(distancia_milha)
tempo_hora=seg_to_hora(tempo_seg)
distancia_km=distancia_m/1000
velocidade = (distancia_m/1000.)/tempo_hora
tempo_milha = tempo_hora/(distancia_m/1000)
print('tempo por km = ',tempo_milha,'h/km')
print('velocidade média = ',velocidade,'km/h')

print('-------------')

#exercício 5
print('exercício 5: ')
def IMC(massa,altura):
	IMC = massa/altura**2
	return IMC
#Escrevendo um exemplo
print('IMC = ',IMC(11,0.7),'kg/m²')

def volume_esfera(raio):
	volume = (4/3)*math.pi*raio**3
	return volume
#Escrevendo um exemplo
print('volume da esfera = ',volume_esfera(5))

def difracao(D,d,comp_onda):
	#Levando em conta que as unidades inseridas estão corretas, iguais e em metro
	delta_y=comp_onda*D/d
	return delta_y
#Escrevendo um exemplo	
print('delta_y da difração = ', difracao(1.98,0.25*10**(-3),632.8*10**(-9)), 'm')

print('-------------')
