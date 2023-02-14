from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from lineales import *
from noLineales import *
import numpy as np

ventana = Tk()
ventana.title('Proyecto EDD')
ventana.geometry("1000x500+150+100")

panel = None
subMenu = None

#------------ Inicializando ------------
conjunto = set() # Conjunto
arreglo = np.array ([]) # arreglo
miListaEnlazada = [ListaEnlazada] # miListaEnlazada
milistaCircularSimple = listaCircular() # miListaCircular
miListaDoble = ListaDoble() #miListaDoble
miListaDobleCircular = ListaDobleCircular() #miListaDobleCircular
miArbol = Arbol() # miArbol
datosArbol = 'Elementos ingresados: ' # datos ingresados al arbol
miGrafo = Grafo() #miGrafo
datosCombo = () # datos para combo box

pila = Pila()
cola = cola()

numero_pila = 100
numero_cola = 100 
numero_cola_seg = 100
contador_desencolar = 0
contador_sim = 0

#---------------------------------------------------------------------------

# ------------------- Inicializando ---------------------------------

conjunto = set() # conjunto
arreglo = np.array([]) # arreglo
miListaEnlazada = ListaEnlazada() # miListaEnlazada
milistaCircularSimple = listaCircular()
miListaDoble = ListaDoble() # miListaDoble
miListaDobleCircular = ListaDobleCircular() # miListaDoble
miArbol = Arbol() # miArbol
datosArbol = 'Elementos ingresados: ' # datos ingresados al arbol
miGrafo = Grafo() # miGrafo
datosCombo = () # datos para combo box

pila = Pila() # Pila
cola = Cola() # Cola

numero_pila = 100
numero_cola = 100
numero_cola_seg = 100
contador_desencolar = 0
contador_sim = 0

#---------------------------------------------------------------------------

# ---------------------------------------   Paneles E. E. Fundamentales ----------------------------------------

def panelLogico(event):
    global panel
    if panel is not None:
        panel.destroy()

    #------------------ Panel --------------------------

    panel = Frame(ventana, bg = '#CFD4EE', padx = 10 , pady = 10)
    panel.pack(expand = True, fill = BOTH)

    definicion = 'Un dato lógico sólo puede tomar dos posibles valores: True (verdadero) o False (falso). En Python cualquier variable (en general, cualquier objeto) puede considerarse como una variable booleana. En general los elementos nulos o vacíos se consideran False y el resto se consideran True.'

    contenedor = LabelFrame(panel, text = 'Definición', pady = 10, padx = 5, bg = '#CFD4EE')
    contenedor.pack(fill = X, side = TOP)

    info = Message(contenedor, text = definicion, bg = '#CFD4EE', aspect = 1000)
    info.pack(fill = X)

    ejemplo = Message(panel, text = 'Ejemplo:', bg = '#CFD4EE', width = 100)
    ejemplo.pack(side = TOP)

    lblEjemplo = Message(panel, text = 'a = True', bg = '#CFD4EE', aspect = 1000)
    lblEjemplo.pack(side=LEFT, anchor = N)

def panelEntero(event):
    global panel
    if panel is not None:
        panel.destroy()

    #------------------ Panel --------------------------

    panel = Frame(ventana, bg = '#CFD4EE', padx = 10 , pady = 10)
    panel.pack(expand = True, fill = BOTH)

    definicion = 'Los números enteros son aquellos que no tienen decimales, tanto positivos como negativos (además del cero). En Python se pueden representar mediante el tipo int (de integer, entero) o el tipo long (largo). La única diferencia es que el tipo long permite almacenarnúmeros más grandes.'

    contenedor = LabelFrame(panel, text = 'Definición', pady = 10, padx = 5, bg = '#CFD4EE')
    contenedor.pack(fill = X, side = TOP)

    info = Message(contenedor, text = definicion, bg = '#CFD4EE', aspect = 1000)
    info.pack(fill = X)

    ejemplo = Message(panel, text = 'Ejemplo:', bg = '#CFD4EE', width = 100)
    ejemplo.pack(side = TOP)

    lblEjemplo = Message(panel, text = 'a = 5', bg = '#CFD4EE', aspect = 1000)
    lblEjemplo.pack(side=LEFT, anchor = N)
    
def panelFlotante(event):
    global panel
    if panel is not None:
        panel.destroy()

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

    lblDato = Message(panel, text = 'Ingrese un elemento: ', bg = '#CFD4EE', width = 200)
    lblDato.pack(side = LEFT, anchor = N)

    dato = Entry(panel, width = 30, justify = RIGHT)
    dato.pack(side = LEFT, anchor = N)
    dato.bind('<Return>', agregar)

    btnAgregar = Button(panel, width = 80, height = 25, text = '  Agregar', bg = '#9C9C9C', border = 0, fg = '#000000', image = imgBtnAgr, compound = 'left', cursor = 'hand2')
    btnAgregar.place(x = 600, y = 110)
    btnAgregar.bind('<Button-1>', agregar)

    # ------------------- Agregar datos despues --------------------------------

print("rereree")

