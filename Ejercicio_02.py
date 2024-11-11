"""
Ejercicio 2: En la estructura creada en el ejercicio anterior, mostrar la cantidad de “a” o “A” que hay almacenadas.
"""

# Ejercicio 1:
def cargarPila(cantidad_de_letras = 27):
    for i in range(cantidad_de_letras):
        valor = input('Ingrese letra: ')
        pila.append(valor)

pila = []
n = 31

while (n > 30 or n < 0):
    n = int(input('Cantidad de letras a ingresar: '))

cargarPila(n)

# Ejercicio 2:
def contar_Aa():
    contador = 0
    while (len(pila) != 0):
        valor = pila.pop() # Obtenemos el ultimo valor de la pila
        if (valor == 'a' or valor == 'A'): # Validamos si el elemento es "A" o "a"
            contador += 1
    return contador

print(f'Existen {contar_Aa()} elementos "a" o "A"')
