def leer_matriz_5x5():
    matriz = []

    for fila in range(5):
        fila_actual = []
        for columna in range(5):
            while True:
                entrada = input(f"Ingrese un numero para [{fila}][{columna}]: ")
                try:
                    numero = float(entrada)
                    break
                except ValueError:
                    print("Entrada invalida. Debe ingresar un numero.")
            fila_actual.append(numero)
        matriz.append(fila_actual)

    return matriz


def mostrar_matriz(matriz):
    print("\nMatriz ingresada:")
    for fila in matriz:
        for valor in fila:
            print(f"{valor:8.2f}", end=" ")
        print()


def main():
    matriz = leer_matriz_5x5()
    mostrar_matriz(matriz)
