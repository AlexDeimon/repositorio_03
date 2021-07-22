#10) Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono 
# (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas. 
# No se podrán meter nombres repetidos.
agenda = {}
bandera = True
while (bandera):
    nombre=input("Introduce un nombre: ")
    telefono=int(input("Introduce un telefono: "))
    if(nombre not in agenda):
        agenda[nombre] = telefono
        print('Contacto añadido')
    else:
        print('El contacto ya existe')
    respuesta = input("¿Quieres salir? (S/N): ")
    if(respuesta == "S" or respuesta=="s"):
        bandera = False
print("Contactos",agenda)