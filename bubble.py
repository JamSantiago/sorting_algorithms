
elements = [9,8,7,6,5,4,3,2,1,0]
aux = 0
tam = len(elements)-1


while(tam >0):

    for i in range(len(elements)-1):
        if elements[i] > elements[i+1]:
           aux = elements[i]
           elements[i] = elements[i+1]
           elements[i+1] = aux
           print(elements)

    tam -= 1


print("final: ")
print(elements)