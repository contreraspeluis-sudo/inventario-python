# ---------------------------------------------------
# PROBLEMA 3 - INVENTARIO Y REABASTECIMIENTO
# Curso: Fundamentos de Programación
# ---------------------------------------------------

# MATRIZ DE INVENTARIO
# [Código, Nombre, Stock Actual, Stock Mínimo]

inventario = [
    ["A01", "Teclado", 5, 10],
    ["A02", "Mouse", 15, 10],
    ["A03", "Monitor", 3, 8],
    ["A04", "Memoria USB", 20, 15],
    ["A05", "Impresora", 2, 5]
]

# ---------------------------------------------------
# FUNCIÓN PARA CALCULAR LA CANTIDAD A PEDIR
# ---------------------------------------------------

def calcular_pedido(stock_actual, stock_minimo):

    # Verificar si el stock actual es menor al mínimo
    if stock_actual < stock_minimo:

        # Calcular la diferencia
        cantidad = stock_minimo - stock_actual

    else:

        # No es necesario pedir productos
        cantidad = 0

    return cantidad


# ---------------------------------------------------
# TÍTULO DEL REPORTE
# ---------------------------------------------------

print("========================================")
print("     LISTA DE REABASTECIMIENTO")
print("========================================")


# ---------------------------------------------------
# RECORRER LA MATRIZ
# ---------------------------------------------------

for articulo in inventario:

    # Extraer información
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # Llamar la función
    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    # Mostrar resultados
    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Stock Actual:", stock_actual)
    print("Stock Mínimo:", stock_minimo)
    print("Cantidad a Solicitar:", cantidad_pedir)
    print("----------------------------------------")