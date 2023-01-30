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
    