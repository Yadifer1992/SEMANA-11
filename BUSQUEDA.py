def buscar_valor(matriz,valor):
    for m in range(len(matriz)):  # Recorre filas
        for n in range(len(matriz[m])):  # Recorre columnas
            if matriz[m][n]==valor:
                return m,n # Retorna la posición si se encuentra
    return None  # Retorna None si no se encuentra

# Matriz 3x3 de ejemplo
matriz = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]
# Solicita al usuario el número a buscar
valor_buscado = int(input("Ingrese el número que desea buscar: "))

# Busca el valor en la matriz
posicion = buscar_valor(matriz, valor_buscado)

# Muestra el resultado
if posicion:
    print(f"El valor {valor_buscado} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")