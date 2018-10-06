
# AULA 1
# JOÃO PEDRO GOMES PINHEIRO - UERJ
# 6 de outubro de 2018
import math
#exercício 1
print('exercício 1:')
distancia_km = 10
distancia_milha = 10/1.61
tempo_seg = 43*60+30
tempo_hora = tempo_seg/3600
tmedio_por_milha = tempo_hora/distancia_milha
print('tempo médio por milha = ', tmedio_por_milha,'h/milha')
velocidade = distancia_milha/tempo_hora
print('velocidade média = ', velocidade,'milhas/h')

print('------------')

#exercício 2
print('exercício 2:')
tempo_seg = 3
velocidade_som_ms=343
velocidade_luz_ms=3*(10**8)
#s1 = o quanto o som anda até a luz chegar, num tempo t1
#s2 = o quanto falta para o som chegar, ou seja, o quanto ele andou nos 3 segundos restantes
#s = s1 + s2 = (velocidade_som * t1) + (velocidade_som * tempo_seg)
#mas t1 = s/velocidade_luz
#s=  (s*velocidade_som)/velocidade_luz + velocidade_som*tempo_seg
#s=velocidade_som*tempo_seg/(1-velocidade_som/velocidade_luz)
s=velocidade_som_ms*tempo_seg/(1-velocidade_som_ms/velocidade_luz_ms)
print('distância = ', s, 'm')

print('------------')

#exercício 3
print('exercício 3:')
a=3
b=-4
c=-10
delta=b**2-4*a*c
y1=(-b+math.sqrt(delta))/2*a
y2=(-b-math.sqrt(delta))/2*a
print('y1 = ', y1)
print('y2 = ', y2)

print('------------')

#exercício 4
print('exercício 4:')
altura_m=5
comprimento_m=0.5
#tg(theta)~sin(theta)~theta para theta<<1rad
theta = comprimento_m/altura_m
print('ângulo zenital = ', theta, 'rad')

print('------------')

#exercício 5
print('exercício 5:')
altura_m=0.7
massa=11
imc=(massa)/(altura_m)**(2)
print('IMC = ',imc,'kg/m²')

print('------------')

#exercício 6
print('exercício 6:')
h=3
g=9.81
v=math.sqrt(2*g*h)
t=math.sqrt(2*h/g)
print('velocidade final = ',v,'m/s')
print('tempo = ',t,'s')
