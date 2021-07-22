#5) Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo.
# Solucion 1
x=int(input("digite un numero: "))
if(0<=x<=10):
    print(x,"está entre 0 y 10")
else:
    print(x,"no está entre 0 y 10")
# Solucion 2:
if(x>=1 and x<=10):
    print("Esta entre 0 y 10")
else:
    print("No esta en ese rango")