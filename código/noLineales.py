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
 class Arbol:

    __orden = []
    __preorden = []
    __postorden = []

    class Nodo:
        def __init__(self, dato):
            self.dato = dato
            self.izquierda = None
            self.derecha = None

    def __init__(self):
        self.raiz = None

    # métodos privados recursivos para recorrer el árbol

    def __agregar(self, nodo, dato):
        if nodo is None:
            self.raiz = self.Nodo(dato)

        elif dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = self.Nodo(dato)
            else:
                self.__agregar(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = self.Nodo(dato)
            else:
                self.__agregar(nodo.derecha, dato)

    def __enOrden(self, nodo):
        if nodo is not None:
            self.__enOrden(nodo.izquierda)
            self.__orden.append(nodo.dato)
            self.__enOrden(nodo.derecha)

    def __preOrden(self, nodo):
        if nodo is not None:
            self.__preorden.append(nodo.dato)
            self.__preOrden(nodo.izquierda)
            self.__preOrden(nodo.derecha)

    def __postOrden(self, nodo):
        if nodo is not None:
            self.__postOrden(nodo.izquierda)
            self.__postOrden(nodo.derecha)
            self.__postorden.append(nodo.dato)

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)
