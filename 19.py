#1) Mete los valores del 1 al 100 en una lista.
#Solucion 1
lista1=[]
i=1
while i<=100:
    lista1.append(i)
    i+=1
print(lista1)

#Solucion 2
lista2=[]
for i in range(1,101,1):
    lista2.append(i)
print(lista2)