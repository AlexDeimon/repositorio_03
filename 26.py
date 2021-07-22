#8) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.
tupla=(1,2,5,1,1,6,0,2,2,0,2,1)
numero=int(input("Digite un numero: "))
cantidad=tupla.count(numero)
print("El numero se repite",str(cantidad),"veces")