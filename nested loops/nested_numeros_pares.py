# cuenta cuantos numeros pares hay en una matriz dada

matrix = [[1,2,4], [3,6,9], [8,710]]
counter = 0

for element in matrix:
    for i in element:
        if i %2 == 0:
            counter = counter + 1
print(counter)
