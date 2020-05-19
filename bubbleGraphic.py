import turtle

pos0 = 0
pos1 = 50
pos2 = 100
pos3 = 150

tam1 = 1
tam2 = 2
tam3 = 3
tam4 = 4
y=100
i =0

##elements = [50,40,30,20,10]
elements = [tam4, tam3, tam2, tam1]
aux = 0
tam = len(elements)-1


def desenhar(array):

    turtle03 = turtle.Turtle()
    turtle03.speed(1)
    turtle03.penup()
    turtle03.shapesize(array[0])
    turtle03.setx(pos0)
    turtle03.sety(y)
    turtle03.pendown()

    turtle02 = turtle.Turtle()
    turtle02.speed(1)
    turtle02.penup()
    turtle02.shapesize(array[1])
    turtle02.setx(pos1)
    turtle02.sety(y)
    turtle02.pendown()

    turtle01 = turtle.Turtle()
    turtle01.speed(1)
    turtle01.penup()
    turtle01.shapesize(array[2])
    turtle01.setx(pos2)
    turtle01.sety(y)
    turtle01.pendown()

    turtle00 = turtle.Turtle()
    turtle00.speed(1)
    turtle00.penup()
    turtle00.shapesize(array[3])
    turtle00.setx(pos3)
    turtle00.sety(y)
    turtle00.pendown()

def desenhar2(array):
    desenha = turtle.Turtle()
    desenha.speed(1)
    desenha.penup()
    desenha.sety(y)
    desenha.write(array,False,
                  align="left",font="arial,20")
    desenha.pendown()


print(elements)
desenhar(elements)



while(tam >0):
    for i in range(len(elements)-1):
        if elements[i] > elements[i+1]:
           aux = elements[i]
           elements[i] = elements[i+1]
           elements[i+1] = aux
           y = y - 50
           desenhar(elements)
           print(elements)
    tam -= 1

turtle.done()