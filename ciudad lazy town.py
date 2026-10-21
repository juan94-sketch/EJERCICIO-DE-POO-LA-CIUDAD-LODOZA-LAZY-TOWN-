class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def agregar_arista(self, u, v, peso):
        self.grafo.append((peso, u, v))

    def buscar(self, padre, i):
        if padre[i] == i:
            return i
        return self.buscar(padre, padre[i])

    def unir(self, padre, rango, x, y):
        raiz_x = self.buscar(padre, x)
        raiz_y = self.buscar(padre, y)

        if rango[raiz_x] < rango[raiz_y]:
            padre[raiz_x] = raiz_y
        elif rango[raiz_x] > rango[raiz_y]:
            padre[raiz_y] = raiz_x
        else:
            padre[raiz_y] = raiz_x
            rango[raiz_x] += 1

    def kruskal_mst(self):
        resultado = []
        i = 0
        e = 0
        
        # Ordenar todas las aristas en orden ascendente de peso (número de losas)
        self.grafo = sorted(self.grafo, key=lambda item: item[0])
        
        padre = []
        rango = []

        for nodo in range(self.V):
            padre.append(nodo)
            rango.append(0)

        while e < self.V - 1 and i < len(self.grafo):
            peso, u, v = self.grafo[i]
            i += 1
            x = self.buscar(padre, u)
            y = self.buscar(padre, v)

            if x != y:
                e += 1
                resultado.append((u, v, peso))
                self.unir(padre, rango, x, y)

        return resultado

# Definición de los puntos (Casas, Iglesias y Ubicaciones de la Ciudad Lodosa)
# Asignamos un índice numérico a cada ubicación con atributo verde
nombres_vertices = [
    "A: CASA DE HUMO", 
    "B: IGLESIA", 
    "C: CASA C", 
    "D: TIENDA CENTRAL", 
    "E: ESTACIÓN DE BICICLETAS", 
    "F: CASA F", 
    "G: CASA DEL PANEL", 
    "H: PUENTE DEL RÍO", 
    "I: CASA PEQUEÑA", 
    "J: CASA DEL JARDÍN"
]

g = Grafo(len(nombres_vertices))

# Registro de caminos (aristas) con su respectivo costo en cuadros/losas
# Formato: agregar_arista(nodo1, nodo2, numero_de_losas)
# (Mapeado de acuerdo a los pesos visibles en las conexiones del mapa)
conexiones = [
    (0, 5, 2), (0, 2, 2), (0, 3, 2), (0, 6, 2), # Conexiones desde Casa de Humo (A)
    (1, 4, 2), (1, 6, 1), (1, 7, 2),             # Conexiones desde Iglesia (B)
    (2, 5, 2), (2, 3, 1),                        # Conexiones Casa C (C)
    (3, 7, 2), (3, 5, 2),                        # Conexiones Tienda Central (D)
    (4, 6, 2), (4, 7, 1), (4, 9, 3),             # Conexiones Estación de Bicicletas (E)
    (6, 7, 3), (7, 8, 1), (8, 9, 2)              # Otras conexiones centrales e inferiores
]

for u, v, peso in conexiones:
    g.agregar_arista(u, v, peso)

# Ejecutar el algoritmo para encontrar la ruta óptima
ruta_optima = g.kruskal_mst()

# Parámetros económicos del problema
COSTO_POR_LOSA = 15
total_losas = sum(peso for u, v, peso in ruta_optima)
costo_total = total_losas * COSTO_POR_LOSA

# Mostrar resultados en consola
print("=== LA CIUDAD LODOSA (LAZY TOWN)===")
print("Atributos aplicados a las casas: Color Verde.\n")
print("Ruta más óptima (Caminos a pavimentar):")
for u, v, peso in ruta_optima:
    print(f" - [{nombres_vertices[u]}  <--->  {nombres_vertices[v]}]: {peso} losas")

print(f"\nTotal de losas utilizadas: {total_losas}")
print(f"Costo por losa: ${COSTO_POR_LOSA}")
print(f"COSTO TOTAL MÍNIMO: ${costo_total}")