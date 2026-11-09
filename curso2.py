ventas = [
    [12, 15, 10, 18],
    [8, 14, 16, 12],
    [20, 18, 15, 22]
]


def mostrar_resultados(ventas):
    cantidad_vendedores = len(ventas)
    cantidad_semanas = len(ventas[0])

    print("\n===== MATRIZ DE VENTAS (millones de pesos) =====")
    for i in range(cantidad_vendedores):
        for j in range(cantidad_semanas):
            print("Vendedor", i + 1, "- Semana", j + 1, ":", ventas[i][j])
        print("---")

    print("\n===== TOTAL POR VENDEDOR =====")
    totales_vendedor = []
    for i in range(cantidad_vendedores):
        suma = 0
        for j in range(cantidad_semanas):
            suma += ventas[i][j]
        totales_vendedor.append(suma)
        print("Vendedor", i + 1, ":", suma, "millones")

    print("\n===== TOTAL POR SEMANA =====")
    totales_semana = []
    for j in range(cantidad_semanas):
        suma = 0
        for i in range(cantidad_vendedores):
            suma += ventas[i][j]
        totales_semana.append(suma)
        print("Semana", j + 1, ":", suma, "millones")

    mayor_vendedor = totales_vendedor[0]
    mejor_vendedor = 1
    for i in range(cantidad_vendedores):
        if totales_vendedor[i] > mayor_vendedor:
            mayor_vendedor = totales_vendedor[i]
            mejor_vendedor = i + 1
    print("\nEl vendedor con más ventas es el Vendedor", mejor_vendedor,
          "con", mayor_vendedor, "millones")

    mayor_semana = totales_semana[0]
    mejor_semana = 1
    for j in range(cantidad_semanas):
        if totales_semana[j] > mayor_semana:
            mayor_semana = totales_semana[j]
            mejor_semana = j + 1
    print("La semana con más ventas es la Semana", mejor_semana,
          "con", mayor_semana, "millones")

    suma_total = 0
    cantidad_datos = 0
    for fila in ventas:
        for valor in fila:
            suma_total += valor
            cantidad_datos += 1
    promedio = suma_total / cantidad_datos
    print("Promedio general de ventas:", round(promedio, 2), "millones")


mostrar_resultados(ventas)

print("\n===== MODIFICAR UNA VENTA =====")

vendedor = int(input("Ingrese el número del vendedor (1 a 3): "))
while vendedor < 1 or vendedor > len(ventas):
    print("Vendedor no válido.")
    vendedor = int(input("Ingrese el número del vendedor (1 a 3): "))

semana = int(input("Ingrese el número de la semana (1 a 4): "))
while semana < 1 or semana > len(ventas[0]):
    print("Semana no válida.")
    semana = int(input("Ingrese el número de la semana (1 a 4): "))

nuevo_valor = float(input("Ingrese el nuevo valor de ventas: "))

ventas[vendedor - 1][semana - 1] = nuevo_valor

print("\nVenta modificada. Resultados actualizados:")
mostrar_resultados(ventas)