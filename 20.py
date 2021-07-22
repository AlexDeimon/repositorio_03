#2) Crea una tupla con los meses del año, pide números al usuario, 
# si el numero esta entre 1 y la longitud máxima de la tupla, 
# muestra el contenido de esa posición sino muestra un mensaje de error.
#El programa termina cuando el usuario introduce un cero.
tupla=('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
bandera=True
while bandera:
    numero=int(input("Digite un número: "))
    if numero==0:
        bandera=False
    else:
        try:
            numero-=1
            print(tupla[numero])
        except:
            print("El numero no está en el rango")
