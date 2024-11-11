"""
Ejercicio 1: Cargar en una pila n letras del abecedario (n debe ser menor a 30).
"""

def cargarPila(cantidad_de_letras = 27): # Por defecto si no recibe parametros son 27 letras
    for i in range(cantidad_de_letras):
        valor = input('Ingrese letra: ')
        pila.append(valor)

pila = []
n = 31

while (n > 30 or n < 0): # Verificamos que la cantidad no supere los 30 o que no sea negativa
    n = int(input('Cantidad de letras a ingresar: '))

cargarPila(n)

print(pila) # Forma incorrecta de imprimir pila