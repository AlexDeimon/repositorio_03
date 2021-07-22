#11) Crea una tupla con valores ya predefinidos del 1 al 10, 
# pide un índice por teclado y muestra los valores de la tupla.
tupla=(1,2,3,4,5,6,7,8,9,10)
n=int(input("Digite un indice de la tupla:"))
n-=1
print("El valor es",tupla[n])