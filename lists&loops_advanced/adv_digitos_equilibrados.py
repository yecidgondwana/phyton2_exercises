# determina si un numero entero es equilibrado. es equilibrado
# si la suma de los digitos en las posiciones pares
# es igual a la suma de los digitos impares

n = 1210

even = 0
odd = 0

for i, d in enumerate(str(n)):
    if i% 2 == 0:
        even + int(d)
else:
    odd + int(d)

if odd == even:
    print('balanced')
else:
    print('not balanced')