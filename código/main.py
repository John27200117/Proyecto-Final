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

    panel = Frame(ventana, bg='#CFD4EE', padx=10, pady=10)
    panel.pack(expand=True, fill=BOTH)

    definicion = 'Una lista circular es una lista lineal en la que el último nodo a punta al primero.Las listas circulares evitan excepciones en las operaciones que se realicen sobre ellas. No existen casos especiales, cada nodo siempre tiene uno anterior y uno siguiente.'

    contenedor = LabelFrame(panel, text='Definición',
                            pady=10, padx=5, bg='#CFD4EE')
    contenedor.pack(fill=X, side=TOP)

    info = Message(contenedor, text=definicion, bg='#CFD4EE', aspect=1000)
    info.pack(fill=X)

    ejemplo = Message(panel, text='Ejemplo:', bg='#CFD4EE', width=100)
    ejemplo.pack(side=TOP)

    # ------------------- Agregar datos al inicio --------------------------------

    lblDato = Message(panel, text='Ingrese un elemento: ',
                      bg='#CFD4EE', width=200)
    lblDato.place(x=0, y=110)

    dato = Entry(panel, width=30, justify=RIGHT)
    dato.place(x=200, y=110)
    dato.bind('<Return>', agregar)

    btnAgregar = Button(panel, width=150, height=25, text='  Agregar al inicio', bg='#9C9C9C',
                        border=0, fg='#000000', image=imgBtnAgr, compound='left', cursor='hand2')
    btnAgregar.place(x=530, y=110)
    btnAgregar.bind('<Button-1>', agregar)

    # ------------------- Eliminar primero --------------------------------
    btnElimPri = Button(panel, width=130, height=25, text='  Eliminar primero', bg='#9C9C9C',
                        border=0, fg='#000000', image=imgBtnElim, compound='left', cursor='hand2')
    btnElimPri.place(x=390, y=110)
    btnElimPri.bind('<Button-1>', eliminarPri)

    # ------------------- Agregar datos al final --------------------------------
    lblDatoF = Message(panel, text='Ingrese un elemento: ',
                       bg='#CFD4EE', width=200)
    lblDatoF.place(x=0, y=150)

    datoF = Entry(panel, width=30, justify=RIGHT)
    datoF.place(x=200, y=150)
    datoF.bind('<Return>', agregarFin)

    btnAgregarFin = Button(panel, width=150, height=25, text='  Agregar al final', bg='#9C9C9C',
                           border=0, fg='#000000', image=imgBtnAgr, compound='left', cursor='hand2')
    btnAgregarFin.place(x=530, y=150)
    btnAgregarFin.bind('<Button-1>', agregarFin)

    # ------------------- Eliminar final --------------------------------
    btnElimF = Button(panel, width=130, height=25, text='  Eliminar ultimo', bg='#9C9C9C',
                      border=0, fg='#000000', image=imgBtnElim, compound='left', cursor='hand2')
    btnElimF.place(x=390, y=150)
    btnElimF.bind('<Button-1>', eliminarFin)

    # ------------------- Agregar datos despues --------------------------------

    lblTitle1 = Label(
        panel, text='Agregar un elemento despues de un dato existente: ', bg='#CFD4EE')
    lblTitle1.place(x=0, y=200)

    lblTlElem = Label(panel, text='Elemento: ', bg='#CFD4EE')
    lblTlElem.place(x=0, y=260)

    elemDespues = Entry(panel, width=20, justify=RIGHT)
    elemDespues.place(x=70, y=220)
    elemDespues.bind('<Return>', agregar)

    lblTlDato = Label(panel, text='Dato: ', bg='#CFD4EE')
    lblTlDato.place(x=220, y=220)

    datoDespues = Entry(panel, width=20, justify=RIGHT)
    datoDespues.place(x=270, y=220)
    datoDespues.bind('<Return>', agregarDespuesDe)

    btnAgregar = Button(panel, width=150, height=25, text='  Agregar despues', bg='#9C9C9C',
                        border=0, fg='#000000', image=imgBtnAgrDes, compound='left', cursor='hand2')
    btnAgregar.place(x=530, y=215)
    btnAgregar.bind('<Button-1>', agregarDespuesDe)

    # ------------------- Agregar datos antes --------------------------------

    lblTitle2 = Label(
        panel, text='Agregar un elemento antes de un dato existente: ', bg='#CFD4EE')
    lblTitle2.place(x=0, y=260)

    lblTlElem2 = Label(panel, text='Elemento: ', bg='#CFD4EE')
    lblTlElem2.place(x=0, y=280)

    elemAntes = Entry(panel, width=20, justify=RIGHT)
    elemAntes.place(x=70, y=280)
    elemAntes.bind('<Return>', agregar)

    lblTlDato2 = Label(panel, text='Dato: ', bg='#CFD4EE')
    lblTlDato2.place(x=220, y=280)

    datoAntes = Entry(panel, width=20, justify=RIGHT)
    datoAntes.place(x=270, y=280)
    datoAntes.bind('<Return>', agregarAntesDe)

    btnAgregar = Button(panel, width=150, height=25, text='  Agregar Antes', bg='#9C9C9C',
                        border=0, fg='#000000', image=imgBtnAgrAnt, compound='left', cursor='hand2')
    btnAgregar.place(x=530, y=275)
    btnAgregar.bind('<Button-1>', agregarAntesDe)

    # --------------- mostras lista --------------------------------------

    lblEjemplo = Label(panel, text=texto, bg='#CFD4EE')
    lblEjemplo.place(x=0, y=400)

def panelListaDoble(event):
    global miListaEnlazada
    global panel
    if panel is not None:
        panel.destroy()

    texto = 'Lista doblemente enlazada: ' +  miListaDoble.str()

    def agregar(event):
        global miListaDoble
        elemento = dato.get()
        
        miListaDoble.agregarFinal(elemento)
        texto = 'Lista Enlazada: ' +  miListaDoble.str()

        lblEjemplo.config(text = texto) 
    
    def agregarInicio(event):
        global miListaDoble
        elemento = elemInicio.get()
        
        miListaDoble.agregarInicio(elemento)
        texto = 'Lista Enlazada: ' +  miListaDoble.str()

        lblEjemplo.config(text = texto) 
    
    def eliminarInicio(event):
        global miListaDoble
        
        miListaDoble.eliminarInicio()
        texto = 'Lista Enlazada: ' +  miListaDoble.str()

        lblEjemplo.config(text = texto)
    
    def eliminarFinal(event):
        global miListaDoble
        
        miListaDoble.eliminarFinal()
        texto = 'Lista Enlazada: ' +  miListaDoble.str()

        lblEjemplo.config(text = texto)

    #------------------ Panel --------------------------

    panel = Frame(ventana, bg = '#CFD4EE', padx = 10 , pady = 10)
    panel.pack(expand = True, fill = BOTH)

    definicion = 'Las listas doblemente enlazadas son estructuras de datos similares a las listas simples. La asignación de memoria es hecha al momento de la ejecución, la diferencia radica en que el enlace entre los elementos se hace con dos apuntadores (uno que apunta hacia el nodo anterior y otro apunta hacia el siguiente nodo).'

    contenedor = LabelFrame(panel, text = 'Definición', pady = 10, padx = 5, bg = '#CFD4EE')
    contenedor.pack(fill = X, side = TOP)

    info = Message(contenedor, text = definicion, bg = '#CFD4EE', aspect = 1000)
    info.pack(fill = X)

    ejemplo = Message(panel, text = 'Ejemplo:', bg = '#CFD4EE', width = 100)
    ejemplo.pack(side = TOP)

    # ------------------- Agregar datos al final --------------------------------

    lblDato = Message(panel, text = 'Ingrese un elemento: ', bg = '#CFD4EE', width = 200)
    lblDato.pack(side = LEFT, anchor = N)

    dato = Entry(panel, width = 30, justify = RIGHT)
    dato.pack(side = LEFT, anchor = N)
    dato.bind('<Return>', agregar)

    btnAgregar = Button(panel, width = 80, height = 25, text = '  Agregar', bg = '#9C9C9C', border = 0, fg = '#000000', image = imgBtnAgr, compound = 'left', cursor = 'hand2')
    btnAgregar.place(x = 600, y = 110)
    btnAgregar.bind('<Button-1>', agregar)

    # ------------------- Agregar datos al inicio --------------------------------

    lblTitle1 = Label(panel, text = 'Agregar un elemento al inicio: ', bg = '#CFD4EE')
    lblTitle1.place(x = 0, y = 150)

    lblTlElem = Label(panel, text = 'Elemento: ', bg = '#CFD4EE')
    lblTlElem.place(x = 0, y = 170)

    elemInicio = Entry(panel, width = 20, justify = RIGHT)
    elemInicio.place(x = 70, y = 170)
    elemInicio.bind('<Return>', agregarInicio)

    btnAgregar = Button(panel, width = 150, height = 25, text = '  Agregar al inicio', bg = '#9C9C9C', border = 0, fg = '#000000', image = imgBtnAgrDes, compound = 'left', cursor = 'hand2')
    btnAgregar.place(x = 530, y = 165)
    btnAgregar.bind('<Button-1>', agregarInicio)

    # ------------------- Eliminar elemento del inicio --------------------------------

    lblTitle2 = Label(panel, text = 'Eliminar elemento del inicio: ', bg = '#CFD4EE')
    lblTitle2.place(x = 0, y = 210)

    btnAgregar = Button(panel, width = 150, height = 25, text = '  Eliminar inicio', bg = '#9C9C9C', border = 0, fg = '#000000', image = imgBtnAgrAnt, compound = 'left', cursor = 'hand2')
    btnAgregar.place(x = 530, y = 205)
    btnAgregar.bind('<Button-1>', eliminarInicio)

    # ------------------- Eliminar elemento del final --------------------------------

    lblTitle3 = Label(panel, text = 'Eliminar un elemento del final la lista: ', bg = '#CFD4EE')
    lblTitle3.place(x = 0, y = 250)

    btnAgregar = Button(panel, width = 100, height = 25, text = '  Eliminar final', bg = '#9C9C9C', border = 0, fg = '#000000', image = imgBtnElim, compound = 'left', cursor = 'hand2')
    btnAgregar.place(x = 580, y = 245)
    btnAgregar.bind('<Button-1>', eliminarFinal)

    # --------------- mostras lista --------------------------------------

    lblEjemplo = Label(panel, text = texto, bg = '#CFD4EE')
    lblEjemplo.place(x=0, y = 300)

def panelListaDobleCircular(event):
    global miListaDobleCircular
    global panel
    if panel is not None:
        panel.destroy()

    texto = 'Lista doble circular de inicio a fin: ' +  miListaDobleCircular.strInicioFin()
    texto1 = 'Lista doble circular de fin a inicio: ' +  miListaDobleCircular.strFinInicio()

    def agregarFinal(event):
        global miListaDobleCircular
        elemento = dato.get()
        
        miListaDobleCircular.agregarFinal(elemento)
        texto = 'Lista doble circular de inicio a fin: ' +  miListaDobleCircular.strInicioFin()
        texto1 = 'Lista doble circular de fin a inicio: ' +  miListaDobleCircular.strFinInicio()

        lblEjemplo.config(text = texto)
        lblEjemplo1.config(text = texto1) 
    
    def agregarInicio(event):
        global miListaDobleCircular
        elemento = elemInicio.get()
        
        miListaDobleCircular.agregarInicio(elemento)
        texto = 'Lista doble circular de inicio a fin: ' +  miListaDobleCircular.strInicioFin()
        texto1 = 'Lista doble circular de fin a inicio: ' +  miListaDobleCircular.strFinInicio()

        lblEjemplo.config(text = texto) 
        lblEjemplo1.config(text = texto1) 
    
    def eliminarInicio(event):
        global miListaDobleCircular
        
        miListaDobleCircular.eliminarInicio()
        texto = 'Lista doble circular de inicio a fin: ' +  miListaDobleCircular.strInicioFin()
        texto1 = 'Lista doble circular de fin a inicio: ' +  miListaDobleCircular.strFinInicio()

        lblEjemplo.config(text = texto)
        lblEjemplo1.config(text = texto1) 
    
    def eliminarFinal(event):
        global miListaDobleCircular
        
        miListaDobleCircular.eliminarFinal()
        texto = 'Lista doble circular de inicio a fin: ' +  miListaDobleCircular.strInicioFin()
        texto1 = 'Lista doble circular de fin a inicio: ' +  miListaDobleCircular.strFinInicio()

        lblEjemplo.config(text = texto)
        lblEjemplo1.config(text = texto1) 

    #------------------ Panel --------------------------

    panel = Frame(ventana, bg = '#CFD4EE', padx = 10 , pady = 10)
    panel.pack(expand = True, fill = BOTH)

    definicion = 'En una lista enlazada doblemente circular, cada nodo tiene dos enlaces, similares a los de la lista doblemente enlazada, excepto que el enlace anterior del primer nodo apunta al último y el enlace siguiente del último nodo, apunta al primero.'

    contenedor = LabelFrame(panel, text = 'Definición', pady = 10, padx = 5, bg = '#CFD4EE')
    contenedor.pack(fill = X, side = TOP)

    info = Message(contenedor, text = definicion, bg = '#CFD4EE', aspect = 1000)
    info.pack(fill = X)

    ejemplo = Message(panel, text = 'Ejemplo:', bg = '#CFD4EE', width = 100)
    ejemplo.pack(side = TOP)

    # ------------------- Agregar datos al final --------------------------------

    lblDato = Message(panel, text = 'Agregar un elemento al final: ', bg = '#CFD4EE', width = 200)
    lblDato.pack(side = LEFT, anchor = N)

    dato = Entry(panel, width = 30, justify = RIGHT)
    dato.pack(side = LEFT, anchor = N)
    dato.bind('<Return>', agregarFinal)

    btnAgregar = Button(panel, width = 80, height = 25, text = '  Agregar', bg = '#9C9C9C', border = 0, fg = '#000000', image = imgBtnAgr, compound = 'left', cursor = 'hand2')
    btnAgregar.place(x = 600, y = 110)
    btnAgregar.bind('<Button-1>', agregarFinal)

    # ------------------- Agregar datos al inicio --------------------------------

    lblTitle1 = Label(panel, text = 'Agregar un elemento al inicio: ', bg = '#CFD4EE')
    lblTitle1.place(x = 0, y = 150)

    lblTlElem = Label(panel, text = 'Elemento: ', bg = '#CFD4EE')
    lblTlElem.place(x = 0, y = 170)

    elemInicio = Entry(panel, width = 20, justify = RIGHT)
    elemInicio.place(x = 70, y = 170)
    elemInicio.bind('<Return>', agregarInicio)

    btnAgregar = Button(panel, width = 150, height = 25, text = '  Agregar al inicio', bg = '#9C9C9C', border = 0, fg = '#000000', image = imgBtnAgrDes, compound = 'left', cursor = 'hand2')
    btnAgregar.place(x = 530, y = 165)
    btnAgregar.bind('<Button-1>', agregarInicio)

    # ------------------- Eliminar elemento del inicio --------------------------------

    lblTitle2 = Label(panel, text = 'Eliminar elemento del inicio: ', bg = '#CFD4EE')
    lblTitle2.place(x = 0, y = 210)

    btnAgregar = Button(panel, width = 150, height = 25, text = '  Eliminar inicio', bg = '#9C9C9C', border = 0, fg = '#000000', image = imgBtnAgrAnt, compound = 'left', cursor = 'hand2')
    btnAgregar.place(x = 530, y = 205)
    btnAgregar.bind('<Button-1>', eliminarInicio)

    # ------------------- Eliminar elemento del final --------------------------------

    lblTitle3 = Label(panel, text = 'Eliminar un elemento del final la lista: ', bg = '#CFD4EE')
    lblTitle3.place(x = 0, y = 250)

    btnAgregar = Button(panel, width = 100, height = 25, text = '  Eliminar final', bg = '#9C9C9C', border = 0, fg = '#000000', image = imgBtnElim, compound = 'left', cursor = 'hand2')
    btnAgregar.place(x = 580, y = 245)
    btnAgregar.bind('<Button-1>', eliminarFinal)

    # --------------- mostras lista --------------------------------------
