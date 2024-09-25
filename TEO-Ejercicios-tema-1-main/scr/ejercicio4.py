def lee_numeros(n):
    listas = []
    for posicion in range(30):
        numero = int(input("introduce un numero:"))
        listas.append(numero)
        print(listas)
    return listas


if __name__ == '__main__':
    cantidad_numeros = int(input("Cuantos números quieres leer?"))
    numeros = lee_numeros(cantidad_numeros)
    print("Esta es la lista:", numeros)
