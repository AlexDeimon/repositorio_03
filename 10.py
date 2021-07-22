#10) Mostrar los números pares entre 1 al 100.
# Solucion 1:
for x in range(1,101):
    if(x%2==0):
        print(x)
# Solucion 2:
for i in range(2,101,2):    
    print(i)
    