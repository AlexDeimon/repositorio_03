#17) Pide una cadena e indica si es un palíndromo o no.
cadena=input("Digite una cadena: ")
if(cadena==cadena[::-1]):
    print("En un palindromo")
else:
    print("No es un palindromo")