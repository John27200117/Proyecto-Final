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

    #------------------ Panel --------------------------

    panel = Frame(ventana, bg = '#CFD4EE', padx = 10 , pady = 10)
    panel.pack(expand = True, fill = BOTH)

    definicion = 'Este tipo de dato se representa en lenguaje de programación como float (flotante). Puede, al igual que el entero, ser positivo o negativo, conteniendo uno o más decimales. La variable float también acepta números en notación científica, en los cuales se coloca una «e» para indicar el valor de la potencia base 10.'

    contenedor = LabelFrame(panel, text = 'Definición', pady = 10, padx = 5, bg = '#CFD4EE')
    contenedor.pack(fill = X, side = TOP)

    info = Message(contenedor, text = definicion, bg = '#CFD4EE', aspect = 1000)
    info.pack(fill = X)

    ejemplo = Message(panel, text = 'Ejemplo:', bg = '#CFD4EE', width = 100)
    ejemplo.pack(side = TOP)

    lblEjemplo = Message(panel, text = 'a = 6.765', bg = '#CFD4EE', aspect = 1000)
    lblEjemplo.pack(side=LEFT, anchor = N)

# ---------------------------------------   Paneles E. E. Compuestos ----------------------------------------

def panelConjuntos(event):
    global conjunto
    global panel
    if panel is not None:
        panel.destroy()

    texto = 'Conjunto = { '
    t = 0
    for i in conjunto:
        if t == len(conjunto) - 1:
            texto += str(i)
        else:
            texto += str(i) + ', '
        t += 1
    texto += ' }'

    def agregar(event):
        global conjunto
        elemento = dato.get()
        conjunto.add(elemento)
        texto = 'Conjunto = { '
        t = 0
        for i in conjunto:
            if t == len(conjunto) - 1:
                texto += str(i)
            else:
                texto += str(i) + ', '
            t += 1
        texto += ' }'
        lblEjemplo.config(text = texto) 

    #------------------ Panel --------------------------

    panel = Frame(ventana, bg = '#CFD4EE', padx = 10 , pady = 10)
    panel.pack(expand = True, fill = BOTH)

    definicion = 'Un conjunto es una colección desordenada de valores no repetidos. Los conjuntos de Python son análogos a los conjuntos matemáticos. El tipo de datos que representa a los conjuntos se llama set. El tipo set es mutable: una vez que se ha creado un conjunto, puede ser modificado.'
    contenedor = LabelFrame(panel, text = 'Definición', pady = 10, padx = 5, bg = '#CFD4EE')
    contenedor.pack(fill = X, side = TOP)

    info = Message(contenedor, text = definicion, bg = '#CFD4EE', aspect = 1000)
    info.pack(fill = X)

    ejemplo = Message(panel, text = 'Ejemplo:', bg = '#CFD4EE', width = 100)
    ejemplo.pack(side = TOP)

    lblDato = Message(panel, text = 'Ingrese un elemento: ', bg = '#CFD4EE', width = 200)
    lblDato.pack(side = LEFT, anchor = N)

    dato = Entry(panel, width = 30, justify = RIGHT)
    dato.pack(side = LEFT, anchor = N)
    dato.bind('<Return>', agregar)

    btnAgregar = Button(panel, width = 80, height = 25, text = '  Agregar', bg = '#9C9C9C', border = 0, fg = '#000000', image = imgBtnAgr, compound = 'left', cursor = 'hand2')
    btnAgregar.pack(side = RIGHT, anchor = N)
    btnAgregar.bind('<Button-1>', agregar)

    lblEjemplo = Message(panel, text = texto, bg = '#CFD4EE', aspect = 1000)
    lblEjemplo.place(x = 0, y = 150)

def panelArray(event):
    global panel
    if panel is not None:
        panel.destroy()
    #------------------ Panel --------------------------

    panel = Frame(ventana, bg = '#CFD4EE', padx = 10 , pady = 10)
    panel.pack(expand = True, fill = BOTH)

    definicion = 'El módulo array define una estructura de datos de secuencia que se ve muy parecida a una list, excepto que todos los miembros tienen que ser del mismo tipo primitivo. Los tipos admitidos son todos numéricos u otros tipos primitivos de tamaño fijo como bytes.'
    contenedor = LabelFrame(panel, text = 'Definición', pady = 10, padx = 5, bg = '#CFD4EE')
    contenedor.pack(fill = X, side = TOP)

    info = Message(contenedor, text = definicion, bg = '#CFD4EE', aspect = 1000)
    info.pack(fill = X)

    def nuevo_array():
        global array_enteros, array_flotantes, array_cadenas, array_booleanos, label_array
        label_array.destroy()
        array_enteros = np.array([])
        array_flotantes = np.array([])
        array_cadenas = np.array([])
        array_booleanos = np.array([])
        label_array = Label(panel, text="[]", bg="#CFD4EE", font=("Cambria", 15))
        label_array.place(x=295, y=230)

    def crear_array(elemento):
        global array_enteros, array_flotantes, array_cadenas, array_booleanos, label_array
        if menu_desplegable.get() == "Enteros":
            try:
                array_enteros = np.append(array_enteros, int(elemento), axis=None)
                label_array.config(text=array_enteros)
            except:
                messagebox.showerror("Aviso", "Debes crear un nuevo array")

        elif menu_desplegable.get() == "Flotantes":
            try:
                array_flotantes = np.append(array_flotantes, float(elemento), axis=None)
                label_array.config(text=array_flotantes)
            except:
                messagebox.showerror("Aviso", "Debes crear un nuevo array")

        elif menu_desplegable.get() == "Cadenas":
            try:
                array_cadenas = np.append(array_cadenas, elemento, axis=None)
                label_array.config(text=array_cadenas)
            except:
                messagebox.showerror("Aviso", "Debes crear un nuevo array")

        elif menu_desplegable.get() == "Booleanos":
            try:
                if elemento == "False":
                    elemento = not(elemento)
                array_cadenas = np.append(array_cadenas, bool(elemento), axis=None)
                label_array.config(text=array_cadenas)
                print(bool(elemento))
            except:
                messagebox.showerror("Aviso", "Debes crear un nuevo array")

        else:
            messagebox.showerror("Aviso", "Debes elegir un tipo de dato")

    global label_array
    
    boton_nuevo_array = Button(panel, width = 90, height = 25, bg = '#9C9C9C', border = 0, fg = '#000000', image = nuevo, compound = 'left', cursor = 'hand2', text="Nuevo array", command=nuevo_array)
    boton_nuevo_array.place(x=525, y=120)

    label_array = Label(panel, text="Tipo de dato:", bg="#CFD4EE")
    label_array.place(x=50, y=120)

    menu_desplegable = ttk.Combobox(panel, values=["Enteros", "Flotantes", "Cadenas", "Booleanos"])
    menu_desplegable.place(x=125, y=120)
    menu_desplegable.insert(0, "Datos")

    label_elemento = Label(panel, text="Elemento:", bg="#CFD4EE")
    label_elemento.place(x=50, y=155)

    entrada = Entry(panel, relief="ridge", bd=2)
    entrada.place(x=110, y=155)

    boton = Button(panel, width = 80, height = 25, text = '  Agregar', bg = '#9C9C9C', border = 0, fg = '#000000', image = imgBtnAgr, compound = 'left', cursor = 'hand2', command=lambda: crear_array(entrada.get()))
    boton.place(x=525, y=155)

    label_array = Label(panel, text="[]", font=("Cambria", 15), bg="#CFD4EE")
    label_array.place(x=295, y=230)

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

    lblTitle1 = Label(panel, text = 'Agregar un elemento despues de un dato existente: ', bg = '#CFD4EE')
    lblTitle1.place(x = 0, y = 150)

    lblTlElem = Label(panel, text = 'Elemento: ', bg = '#CFD4EE')
    lblTlElem.place(x = 0, y = 170)

    elemDespues = Entry(panel, width = 20, justify = RIGHT)
    elemDespues.place(x = 70, y = 170)

    lblTlDato = Label(panel, text = 'Dato: ', bg = '#CFD4EE')
    lblTlDato.place(x = 220, y = 170)

    datoDespues = Entry(panel, width = 20, justify = RIGHT)
    datoDespues.place(x = 270, y = 170)
    datoDespues.bind('<Return>', agregarDespues)

    btnAgregar = Button(panel, width = 150, height = 25, text = '  Agregar despues', bg = '#9C9C9C', border = 0, fg = '#000000', image = imgBtnAgrDes, compound = 'left', cursor = 'hand2')
    btnAgregar.place(x = 530, y = 165)
    btnAgregar.bind('<Button-1>', agregarDespues)

    # ------------------- Agregar datos antes --------------------------------

    lblTitle2 = Label(panel, text = 'Agregar un elemento antes de un dato existente: ', bg = '#CFD4EE')
    lblTitle2.place(x = 0, y = 210)

    lblTlElem2 = Label(panel, text = 'Elemento: ', bg = '#CFD4EE')
    lblTlElem2.place(x = 0, y = 230)

    elemAntes = Entry(panel, width = 20, justify = RIGHT)
    elemAntes.place(x = 70, y = 230)

    lblTlDato2 = Label(panel, text = 'Dato: ', bg = '#CFD4EE')
    lblTlDato2.place(x = 220, y = 230)

    datoAntes = Entry(panel, width = 20, justify = RIGHT)
    datoAntes.place(x = 270, y = 230)
    datoAntes.bind('<Return>', agregarAntes)

    btnAgregar = Button(panel, width = 150, height = 25, text = '  Agregar Antes', bg = '#9C9C9C', border = 0, fg = '#000000', image = imgBtnAgrAnt, compound = 'left', cursor = 'hand2')
    btnAgregar.place(x = 530, y = 225)
    btnAgregar.bind('<Button-1>', agregarAntes)

    # ------------------- Eliminar elemento --------------------------------

    lblTitle3 = Label(panel, text = 'Eliminar un elemento de la lista: ', bg = '#CFD4EE')
    lblTitle3.place(x = 0, y = 270)

    lblTlElem3 = Label(panel, text = 'Elemento: ', bg = '#CFD4EE')
    lblTlElem3.place(x = 0, y = 290)

    elemEliminar = Entry(panel, width = 20, justify = RIGHT)
    elemEliminar.place(x = 70, y = 290)
    elemEliminar.bind('<Return>', eliminar)

    btnAgregar = Button(panel, width = 100, height = 25, text = '  Eliminar', bg = '#9C9C9C', border = 0, fg = '#000000', image = imgBtnElim, compound = 'left', cursor = 'hand2')
    btnAgregar.place(x = 580, y = 285)
    btnAgregar.bind('<Button-1>', eliminar)

    # --------------- mostras lista --------------------------------------

    lblEjemplo = Label(panel, text = texto, bg = '#CFD4EE')
    lblEjemplo.place(x=0, y = 350)

def panelSimpleCircular(event):
    global milistaCircularSimple
    global panel
    if panel is not None:
        panel.destroy()

    texto = 'Lista Circular Simple: ' + milistaCircularSimple.Recorrer()

    def agregar(event):
        global milistaCircularSimple
        elemento = dato.get()

        milistaCircularSimple.AgregarInicio(elemento)
        texto = 'Lista Circular Simple: ' + milistaCircularSimple.Recorrer()

        lblEjemplo.config(text=texto)

    def agregarFin(event):
        global milistaCircularSimple
        elemento = datoF.get()

        milistaCircularSimple.AgregarFinal(elemento)
        texto = 'Lista Circular Simple: ' + milistaCircularSimple.Recorrer()

        lblEjemplo.config(text=texto)

    def agregarDespuesDe(event):
        global milistaCircularSimple
        elemento = elemDespues.get()
        dato = datoDespues.get()

        milistaCircularSimple.agregarDespues(dato, elemento)
        texto = 'Lista Circular Simple ' + milistaCircularSimple.Recorrer()

        lblEjemplo.config(text=texto)

    def agregarAntesDe(event):
        global miListaEnlazada
        elemento = elemAntes.get()
        dato = datoAntes.get()

        milistaCircularSimple.agregarAntes(dato, elemento)
        texto = 'Lista Circular Simple: ' + milistaCircularSimple.Recorrer()

        lblEjemplo.config(text=texto)

    def eliminarPri(event):
        global milistaCircularSimple

        milistaCircularSimple.EliminarInicio()
        texto = 'Lista Circular Simple: ' + milistaCircularSimple.Recorrer()

        lblEjemplo.config(text=texto)

    def eliminarFin(event):
        global milistaCircularSimple

        milistaCircularSimple.EliminarFinal()
        texto = 'Lista Circular Simple: ' + milistaCircularSimple.Recorrer()

        lblEjemplo.config(text=texto)

    # ------------------ Panel --------------------------