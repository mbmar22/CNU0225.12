# Construye la representación.
print("A. Construye la representación.")

grafo = {
    "A": ["B", "C"], # A-B, A-C
    "B": ["A", "D"], # B-D
    "C": ["A", "D", "E"], # C-D, C-E
    "D": ["B", "C", "F"], # D-F
    "E": ["C", "F"], # E-F
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

def contar_aristas(grafo): #aplicar un sort para ordenar cada par, de modo que si tengo por ejemplo ["DA"] se cambie a ["AD"].
    contador = 0
    lista = []
    add = []

    for i in grafo:
        # print(i)
        for j in grafo[i]:
            add = [i, j]
            add.sort()
            add = add[0] + add[1]
            juntos = [add]
            lista.extend(juntos)
            # print(add)
            #contador += 1
            # print(j)

    # print(lista) # Por algna razón, cuando imprimo la lista, los valores están separados en lugar de juntos. Averiguar por qué. Resuelto.
    lista.sort()
    # print(lista)

    lista_final = []

    for i in lista:
        for j in lista:
            if i != j:
                if i not in lista_final:
                    lista_final.append(i)
                    contador += 1



    #print(lista_final)

    return contador



print("Vertices:", contar_vertices(grafo))
print("Aristas:", contar_aristas(grafo))
# Sería bueno ver si la cantidad de combinaciones global (o sea, que por ejemplo "AB" y "BA" sean diferentes) es lógicamente siempre la mitad. Por ejemplo, en este caso 14, pero si lo dividimos entre 2 nos da 7, la cantidad total de aristas. Ahora que lo reviso: Sí, en efecto, es la mitad.