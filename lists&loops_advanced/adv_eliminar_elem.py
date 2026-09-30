# dada una lista, el programa debe elimninar el elemento
# que seleccione el usuario

my_list = [1,2,3,4,3,5,3,3]
n = int(input('enter n')) # n you want eliminate of the list
new_list = []

for numero in my_list:
  if numero != n:
    new_list.append(numero)

print(new_list)








