#4) Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. 
# Por último, muestra los números ordenados de menor a mayor.
bandera=True
lista=[]
while bandera:
    numero=int(input("Digite un numero: "))
    if numero!=0:
        lista.append(numero)
    else:
        bandera=False
lista.sort()
print(lista)