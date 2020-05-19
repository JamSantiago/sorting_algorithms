
elements = [9, 8, 7, 6, 5, 4, 3, 2, 1]
tam = len(elements) #9
min = 0
pos = 0

for x in range(0, tam-1):
    min = elements[x+1]
    for y in range(x+1, tam-1):
        if elements[y] > elements[y+1]:
            min = elements[y+1]
            pos = y+1
    if min < elements[x]:
        elements[pos] = elements[x]
        elements[x] = min
        print(elements)


