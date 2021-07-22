#16) Pide dos cadenas por teclado, muestra ambas cadenas con un espacio entre ellas 
# y con los 2 primeros caracteres intercambiados. Por ejemplo, hola mundo pasaría a mula hondo
cadena1=input("Digite cadena 1: ")
cadena2=input("Digite cadena 2: ")
print( cadena2[:2] + cadena1[2:] + " " + cadena1[:2] + cadena2[2:] )