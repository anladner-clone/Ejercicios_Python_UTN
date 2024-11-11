"""
Ejercicio 5:  Dada una pila que almacena un número de n dígitos mostrar el mensaje “el número es capicúa” en caso de que el número almacenado así lo sea, caso contrario mostrar el mensaje “el número no es capicúa”.
"""

pila = [323, 23, 22, 45, 575]  # Inicializamos la pila con valores, asumiendo que fue cargada anteriormente.

def esCapicua(pila=[]):
    copia_pila = pila
    while (len(pila) != 0):
        valor = pila.pop()
        valor = str(valor)  # Convertimos el número en una cadena para poder comparar el primer y último dígito.
        if valor[0] == valor[-1]:
            print(f'El número {valor} es capicúa')
        else:
            print(f'El número {valor} no es capicúa')
    
    return copia_pila # Retornamos la copia de la pila original para no perder los datos

pila = esCapicua(pila=pila)