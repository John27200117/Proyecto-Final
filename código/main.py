from lineales import *
from noLineales import *
import numpy as np
#------------ Inicializando ------------
conjunto = set() # Conjunto
arreglo = np.array ([]) # arreglo
miListaEnlazada = [ListaEnlazada] # miListaEnlazada
milistaCircularSimple = listaCircular() # miListaCircular
miListaDoble = ListaDoble() #miListaDoble
miListaDobleCircular = ListaDobleCircular() #miListaDobleCircular
miGrafo = Grafo() #miGrafo

pila = Pila()
cola = cola()

numero_pila = 100
numero_cola = 100 
numero_cola_seg = 100
contador_desencolar = 0
contador_sim = 0
#he llegado chicas