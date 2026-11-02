# Guía práctica
# Ejemplo 1: Crear y mostrar un grafo no dirigido.
grafo = {
    "Managua": ["León", "Granada", "Masaya"],
    "León": ["Managua"],
    "Granada": ["Managua", "Masaya"],
    "Masaya": ["Managua", "Granada"]
}

def mostrar_grafo(conexiones):
    for vertice, vecinos in conexiones.items():
        print(vertice, "->", ", ".join(vecinos))


mostrar_grafo(grafo)