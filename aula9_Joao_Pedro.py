import math

#EXERCÍCIO 1
print('Exercício 1: ')

distancia1 = 5 #5 km
velocidade1 = 12 #km/h
velocidade1 = velocidade1/60 #convertendo para km/min

tempototal1 = distancia1/velocidade1
tempototal1 = tempototal1//1 #transformando num int
tempototal1_int = int(float(tempototal1))+1

lista_tempo = []
lista_distancia = []

for i in range(tempototal1_int):
	lista_tempo.append(i)
	lista_distancia.append(velocidade1*i)


#EXERCÍCIO 2
print('Exercício 2: ')

v_inicial = 12 #12 km/h
v_inicial = v_inicial/60 #convertendo pra km/min

v_final = 15 #15 km/h
v_final = v_final/60 #convertendo para km/min

distancia2 = 0.2 #0.2 km

aceleracao = (v_final**2 - v_inicial**2)/(2*distancia2)

tempototal2 = (v_final-v_inicial)/aceleracao

i=0
while (i<(tempototal2-0.1)):

	lista_distancia.append(5+v_inicial*(i+0.05)+((aceleracao)*((i+0.05)**2))/2)
	print 
	lista_tempo.append(i+0.05+tempototal1)
	i=i+0.05

distancia3 = 7-5.2 #km
velocidade3 = 15 #km/h
velocidade3 = velocidade3/60 #convertendo para km/min

tempototal3 = distancia3/velocidade3
tempototal3 = tempototal3//1 #transformando num int
tempototal3_int = int(float(tempototal3))+1

for i in range(tempototal3_int):
	lista_tempo.append(i+tempototal1+tempototal2)
	lista_distancia.append(5.2+velocidade3*i)


for n in range(len(lista_distancia)):
	print("%.2f" % lista_distancia[n], "%.2f" % lista_tempo[n])

import matplotlib.pyplot as plt

#plt.plot(lista_tempo,lista_distancia)
#plt.xlabel("tempo min")
#plt.ylabel("distância km")
#plt.show()
#plt.close()

#EXERCÍCIO 3
print('Exercício 3: ')
x = []
y = []
t = []
time=0.1
i = 0
while (time<10):
	x.append(math.sin(math.cos(math.sqrt(9.81)*time)))
	y.append(-1*math.cos (math.cos(math.sqrt(9.81)*time))) 
	t.append(time)
	time = time + 0.1

print(' x     y     t')
for n in range(len(x)):
	print("%.2f" % x[n],"%.2f" %  y[n],"%.2f" %  t[n])

import matplotlib.pyplot as plot_TversusY
import matplotlib.pyplot as plot_TversusX
import matplotlib.pyplot as plot_XversusY

plot_TversusY.plot(t,y)
plot_TversusY.xlabel('t')
plot_TversusY.ylabel('y')
plot_TversusY.show()
plot_TversusY.close()

plot_TversusX.plot(t,x)
plot_TversusX.xlabel('t')
plot_TversusX.ylabel('x')
plot_TversusX.show()
plot_TversusX.close()

plot_XversusY.plot(x,y)
plot_XversusY.xlabel('x')
plot_XversusY.ylabel('y')
plot_XversusY.show()
plot_XversusY.close()
		