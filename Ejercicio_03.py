"""
Ejercicio 3: Dada una estructura pila que almacena la letra del pasillo donde se ubica los últimos N libros pedidos de la biblioteca, se pide agregar a la pila la letra de un nuevo libro que se debe ingresar por teclado. Mostrar
"""

pila = []  # Inicializamos una pila vacía, asumiendo que es el punto de inicio del proceso, por lo que n es 0.
n = 0      # n indica la cantidad de libros que hay en la pila

def cargarPila(cantidad_de_datos = 1, cantidad_de_libros = None): # Si la funcion no recibe parametros, por defecto se carga 1 libro
    for i in range(cantidad_de_datos):
        valor = input('Ingrese letra del pasillo: ')
        pila.append(valor)
        cantidad_de_libros += 1 # Aumentamos la cantidad de libros almacenados
    return cantidad_de_libros

def mostrarPila():
    while (len(pila) != 0): # Mientras pila contenga datos, mostramos el valor
        valor = pila.pop()
        print(f'{valor}')

n = cargarPila(cantidad_de_libros = n)
mostrarPila() # Forma correcta de mostrar una pila
print(f'Cantidad de Libros: {n}')