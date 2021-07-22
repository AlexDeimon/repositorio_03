#6) Añadir al anterior ejercicio, que si esta entre 11 y 20, 
# muestre otro mensaje diferente y si esta entre 21 y 30 otro mensaje.
#Solucion 1:
x=int(input("digite un numero: "))
if(0<=x<=10):
    print(x,"está entre 0 y 10")
elif(11<=x<=20):
    print(x,"está entre 11 y 20")
elif(21<=x<=30):
    print(x,"está entre 21 y 30")
else:
    print(x,"no esta entre 0 y 30")
#Soluucion 2:
if(x>=1 and x<=10):
    print("Esta entre 0 y 10")
elif(x>=11 and x<=20):
    print("Esta entre 11 y 20")
elif(x>=21 and x<=30):
    print("Esta entre 21 y 30")
else:
    print("No esta en ese rango")