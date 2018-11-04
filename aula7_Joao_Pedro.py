
import  turtle
import  math
 
def draw_bar(t, valor_min, valor_max, binn, dados):
    # t - turtle
    # dados - lista
    # binn (quantidade de torres), valor_min e valor_max - números reais



    height=[]
    if valor_min >= valor_max:
        print ('ERRO: O valor mínimo deve ser colocado primeiro do que o valor máximo')
    if type(dados) != tuple:
        print ('ERRO: o conjunto de dados precisa ser do tipo tuple')

    bin_size = (valor_max-valor_min)/binn

    n = len(dados)
    altura = 0
    for j in range(0,int(binn)):
        for dado in dados:
            if (dado<valor_min or dado>valor_max):
                print('ERRO: Existem valores da lista que são maiores ou menores que os limites solicitados')


            if dado >= valor_min + bin_size*j and dado < valor_min + bin_size*(j+1):
                altura = altura + 1
        height.append(altura)
        altura = 0 

    i = len(height)
    print('len(height) = ', i)
    print(height)
    for n in range(0,i):
        t.begin_fill()           # Added this line
        t.left(90)
        t.forward(height[n])
        t.write("  "+ str(height[n]))
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(height[n])
        t.left(90)
        t.end_fill()             # Added this line
        t.forward(1)

wn = turtle.Screen()         # Set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()       # Create tess and set some attributes
tess.color("blue", "red")
tess.pensize(3)

dados = (2,4,6,1,8,4,12,16,18,15,18,14,16,13,15,13,15,18,20,23,25,25,26,26,26,28,26,15,26,14,26,15,17,17,14,17,27,27,25,13,13,15,14,13,14,1,6,16,14,13,15,16,11,13,13,12,1,26,26,27,12,12,12,12,12,12,12,12,12,1,21,12,12,12,12,12,12)

draw_bar(tess,0,30,3,dados)

wn.mainloop()