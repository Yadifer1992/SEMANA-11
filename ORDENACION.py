def bubble_sort(fila):
    n = len(fila)
    for m in range(n):
        for n in range(0, n - m - 1):
            if fila[n] > fila[n + 1]:  # Intercambia si el elemento es mayor que el siguiente
                fila[n], fila[n + 1] = fila[n + 1], fila[n]

def ordenar_fila(matriz, fila_index):
    if 0 <= fila_index < len(matriz):
        print("\nMatriz original:")
        for fila in matriz:
            print(fila)

        # Ordena la fila específica
        bubble_sort(matriz[fila_index])

        print("\nMatriz con la fila ordenada:")
        for fila in matriz:
            print(fila)
    else:
        print("El índice de fila no es válido.")

# Matriz 3x3 de ejemplo
matriz = [
    [6, 2, 4],
    [10, 8, 12],
    [16, 14, 18]
]

# Solicita al usuario la fila a ordenar
fila_a_ordenar = int(input("Ingrese el índice de la fila que desea ordenar (0, 8 o 12): "))

# Ordena la fila seleccionada
ordenar_fila(matriz, fila_a_ordenar)