# Guía práctica
# Ejemplo 1. Crear y mostrar un grafo no dirigido
grafo = {
    "Managua": ["León", "Granada", "Masaya"],
    "León": ["Managua", "Estelí"],
    "Granada": ["Managua", "Masaya"],
    "Masaya": ["Managua", "Granada"],
    "Estelí": ["León"]
}

def mostrar_grafo(conexiones):
    for vertice, vecinos in conexiones.items():
        print(vertice, "->", ", ".join(vecinos))

mostrar_grafo(grafo)


# Ejemplo 2. Matriz del grado A-B-C-D
vertices = ["A", "B", "C", "D"]
matriz = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

def mostrar_matriz(nodos, conexiones):
    print("   ", " ".join(nodos))
    for i in range(len(nodos)):
        print(nodos[i], " ", " ".join(map(str, conexiones[i])))

mostrar_matriz(vertices, matriz)


def posiciones(posicion):
    if posicion == "A":
        return 0
    elif posicion == "B":
        return 1
    elif posicion == "C":
        return 2
    elif posicion == "D":
        return 3
    else:
        return "La arista no existe."


def demostrar_conexion(valor1, valor2, nodos, conexiones):
    contador = 0
    global broke
    broke = True
    num_posicion = posiciones(valor2)
    for i in range(len(nodos)):
        if nodos[i] == valor1:
            for j in range(len(conexiones)):
                if contador == num_posicion:
                    print(f"\nExiste una relación entre {valor1} y {valor2} de {conexiones[i][j]}.") # Aunque realmente hasta ahora, solo puede ser 0 y 1, entonces no es necesario poner lo de conexiones[i][j]
                    broke = False
                    break
                contador += 1
    if broke != False: # Corregir esto.
        print("No existe.")

demostrar_conexion("A", "C", vertices, matriz)
demostrar_conexion("Al", "C", vertices, matriz)


def cambiar_conexion(valor1, valor2, nodos, conexiones):
    print("hola")