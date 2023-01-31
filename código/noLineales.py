from collections import deque
# ------------- Grafo ------------
class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz = [[None]*0 for i in range (0)]
        def mostrarMatriz(self):
            cadena = ""
            
            for c in range(len(self.matriz)):
                cadena += str(self.vertice[f]) + "|"
            cadena += "\n"
            for f in range(len(self.matriz)):
                cadena += "\t" + str(self.matriz[f][c])
            cadena += "\n"
            
        cadena += "\n"
        return cadena

    @staticmethod
    def contenido_en(lista, k):
        if lista.count(k) == 0:
            return False
        return True
    def agregarVertice(self, v):
        if self.esta_en_vertices(v):
            return False
        
        self.vertices.append(v)

        filas = columnas = len(self.matriz)
        matriz_aux = [[None] * (filas+1) for i in range(columnas+1) ]

        for f in range(filas):
            for c in range(columnas):
                matriz_aux[f][c] = self.matriz[f][c]
        
        self.matriz = matriz_aux
        return True
    
    def agregarArista(self, inicio, fin, valor, dirijida):
        if not(self.esta_en_vertices(inicio)) or not(self.esta_en_vertices(fin)):
            return False
        
        self.matriz[self.vertices.index(inicio)][self.vertices.index(fin)] = valor

        if not dirijida:
            self.matriz[self.vertices.index(fin)][self.vertices.index(inicio)] = valor
        return True

    def recorrido_anchura(self, inicio):
        if not self.esta_en_vertices(inicio):
            return None
        
        recorrido = []
        cola = deque([inicio])

        while len(cola) > 0:
            v_aux = cola.popleft()
            recorrido.append(v_aux)

            for i in range(len(self.matriz)):
                if self.matriz[self.vertices.index(v_aux)][i] is not None:
                    v_candidato = self.vertices[i]
                    if not self.contenido_en(recorrido, v_candidato) and not self.contenido_en(cola, v_candidato):
                        cola.append(v_candidato)
        
        return recorrido
        
    def recorrido_profundidad(self, inicio):
        if not self.esta_en_vertices(inicio):
            return None

        recorrido = []
        pila = [inicio]

        while len(pila) > 0:
            v_aux = pila.pop()

            if not self.contenido_en(recorrido, v_aux):
                recorrido.append(v_aux)

            condicion = True

            for i in range(len(self.matriz)):
                if self.matriz[self.vertices.index(v_aux)][i] is not None:
                    v_candidato = self.vertices[i]

                    if not self.contenido_en(recorrido, v_candidato) and condicion:

                        condicion = False

                        pila.append(v_aux)
                        pila.append(v_candidato)

        return recorrido
 # ----------------------------- Arbol -----------------------------------------    