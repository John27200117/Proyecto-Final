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

# ---------------------------------------   Paneles E. D. Lineales ----------------------------------------

def panelListaSimple(event):
    global miListaEnlazada
    global panel
    if panel is not None:
        panel.destroy()

    texto = 'Lista Enlazada: ' +  miListaEnlazada.str()

    def agregar(event):
        global miListaEnlazada
        elemento = dato.get()
        
        miListaEnlazada.agregar(elemento)
        texto = 'Lista Enlazada: ' +  miListaEnlazada.str()

        lblEjemplo.config(text = texto) 

    def agregarDespues(event):
        global miListaEnlazada
        elemento = elemDespues.get()
        dato = datoDespues.get()
        
        miListaEnlazada.agregarDespuesDe(dato, elemento)
        texto = 'Lista Enlazada: ' +  miListaEnlazada.str()

        lblEjemplo.config(text = texto) 
    
    def agregarAntes(event):
        global miListaEnlazada
        elemento = elemAntes.get()
        dato = datoAntes.get()
        
        miListaEnlazada.agregarAntesDe(dato, elemento)
        texto = 'Lista Enlazada: ' +  miListaEnlazada.str()

        lblEjemplo.config(text = texto) 
    
    def eliminar(event):
        global miListaEnlazada
        elemento = elemEliminar.get()
        
        miListaEnlazada.eliminar(elemento)
        texto = 'Lista Enlazada: ' +  miListaEnlazada.str()

        lblEjemplo.config(text = texto)

    #------------------ Panel --------------------------
    
    panel = Frame(ventana, bg = '#CFD4EE', padx = 10 , pady = 10)
    panel.pack(expand = True, fill = BOTH)

    definicion = 'Es una colección de nodos de elementos enlazados dispuestos unos a continuación de otros en la que cada elemento se enlaza a otro nodo, la idea es tener un conjunto de elementos almacenados es una estructura llamados nodos, en las cuales contienen la dirección de un nodo y el elemento almacenado.'

    contenedor = LabelFrame(panel, text = 'Definición', pady = 10, padx = 5, bg = '#CFD4EE')
    contenedor.pack(fill = X, side = TOP)

    info = Message(contenedor, text = definicion, bg = '#CFD4EE', aspect = 1000)
    info.pack(fill = X)

    ejemplo = Message(panel, text = 'Ejemplo:', bg = '#CFD4EE', width = 100)
    ejemplo.pack(side = TOP)
    
    # ------------------- Agregar datos --------------------------------
