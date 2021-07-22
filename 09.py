#9) Mostrar los caracteres de la cadena “Hola mundo”.
cadena="Hola mundo"
# Solucion 1:
for i in range(len(cadena)):
    print(cadena[i])
# Solucion 2:
for i in "Hola mundo":
    print(i)
