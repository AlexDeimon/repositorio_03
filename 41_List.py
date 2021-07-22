n = int(input().strip())
lista = []
for t in range(n):
    Cadena = input().strip().split(" ")
    if Cadena[0] == "append":
        lista.append(int(Cadena[1]))
    elif Cadena[0] == "insert":
        lista.insert(int(Cadena[1]), int(Cadena[2]))
    elif Cadena[0] == "remove":
        lista.remove(int(Cadena[1]))
    elif Cadena[0] == "pop":
        lista.pop()
    elif Cadena[0] == "sort":
        lista.sort()
    elif Cadena[0] == "reverse":
        lista.reverse()
    elif Cadena[0] == "print":
        print(lista)