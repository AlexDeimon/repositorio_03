#12) Crea una lista vacía (pongamos 10 posiciones), pide sus valores y devuelve la suma y la media de los números.
lista=[]
suma=0
media=0
for i in range(1,11):
    n=int(input("Digite un numero: "))
    lista.append(n)
    suma+=n
    media=suma/len(lista)
print(lista)
print("la suma de los valores es:",suma)
print("la media de los valores es:",media)
