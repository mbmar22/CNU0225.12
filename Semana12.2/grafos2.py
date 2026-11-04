# Construye la representación.
print("A. Construye la representación.")

grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"]
}

def mostrar_vecinos(grafo, vertice):
    if vertice not in grafo:
        return []
    return grafo[vertice]

print(mostrar_vecinos(grafo, "C"))

'''Cada arista aparece por lo menos una vez porque tiene vecinos.'''


# Retos de programación
# Reto 1 · Reconoce la estructura
print("\nReto 1 · Reconoce la estructura")
def contar_vertices(grafo):
    contador = 0
    for i in grafo:
        contador += 1
    return contador

def contar_aristas(grafo):
    contador = 0
    for i in grafo:
        for j in grafo[i]:
            contador += 1
    return contador


print("Vertices: ", contar_vertices(grafo))
print("Aristas: ", contar_aristas(grafo))