# dada un matriz, crea una nueva matriz que sea igual a la dada
# pero transpuesta filas por columnas

matrix = [[4,2], [8,7]]
new_matrix = []

for columna in range(2):
    new_row = []
    for fila in matrix:
        new_row.append(fila[columna])

    new_matrix.append(new_row)
    
print(new_matrix)

