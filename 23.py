#5) Lo mismo que el anterior pero ordenando de mayor a menor.
bandera=True
lista=[]
while bandera:
    numero=int(input("Digite un numero: "))
    if numero!=0:
        lista.append(numero)
    else:
        bandera=False
lista.sort(reverse=True)
print(lista)