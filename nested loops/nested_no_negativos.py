# remplaza todos los numeros negativos en una matriz dada con 0

matrix = [[4,-3,2], [-1,6,-7]]
new_matrix = []

for element in matrix:
    new_file = []
    for i in element:
        if i < 0:
            new_file.append(0)
        else:
            new_file.append(i)
    new_matrix.append(new_file)

print(new_matrix)
            