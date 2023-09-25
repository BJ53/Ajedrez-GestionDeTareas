def pintar_tablero_ajedrez():
    tablero = [[0 for _ in range(8)] for _ in range(8)]  # Crear un tablero de 8x8 inicialmente lleno de 0s
    colores = ["rojo", "azul"]

    for fila in range(8):
        for columna in range(8):
            color_actual = colores[(fila + columna) % 2]
            tablero[fila][columna] = color_actual
            print(f"Casilla ({fila}, {columna}): {color_actual}")

    return tablero

tablero_pintado = pintar_tablero_ajedrez()