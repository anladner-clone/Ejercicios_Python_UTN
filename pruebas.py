def buscar_elemento(lista, elemento):
    for i in lista:
        if i == elemento:
            return True
    return False

lista = [1, 2, 3, 4, 5, 6]
print(buscar_elemento(lista, 4))  # True