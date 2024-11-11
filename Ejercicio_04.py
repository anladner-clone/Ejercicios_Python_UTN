"""
Ejercicio 4:  Dada la pila del ejercicio anterior ya cargada en la memoria, se pide eliminar de la estructura todas las letras iguales al pasillo X. X es una componente del mismo tipo que las que están almacenadas en la estructura y se debe ingresar por teclado. Mostrar
"""

# Ejercicio 3:
pila = ["a", "b", "c", "d"]  # Inicializamos la pila, suponiendo que fue cargada en el ejercicio anterior.
n = 4  # n representa la cantidad de libros actualmente en la pila.

# Ejercicio 4:
def eliminarElemento(elemento = None, pila = []):
    pila_aux = []
    while (len(pila) != 0): # Desapilamos y omitimos el dato que no necesitamos
        valor = pila.pop()
        if (valor != elemento):
            pila_aux.append(valor)

    while (len(pila_aux)!=0): # Apilamos para no perder el orden inicial
        valor = pila_aux.pop()
        pila.append(valor)

    return pila
            
def mostrarPila(pila = []):
    while (len(pila) != 0): # Mientras pila contenga datos, mostramos el valor
        valor = pila.pop()
        print(f'{valor}')


x = input('Ingrese el pasillo a eliminar: ')
pila = eliminarElemento(elemento=x, pila=pila)

mostrarPila(pila=pila)