## ------------ Lista Simple Enlazada --------------
class ListaEnlazada:
    class Nodo:
        def _init_(self,dato):
            self.dato = dato
            self.siguiente = None
        
    def _init_(self):
        self.primero = None
        self.tamanio = 0
        
    def agregar(self,valor): # Agregamos los valores a la lista
        nodo = self.Nodo(valor)
        if self.tamanio == 0:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nodo
        
        self.tamanio += 1
        
    def agregarDespuesDe(self, dato, valor):
        nodo = self.Nodo(valor)
        if self.tamanio == 0:
            return False
        else:
            try:
                actual = self.primero
                while actual.dato != dato:
                    actual = actual.siguiente
                nodo.siguiente = actual .siguiente
                actual.siguiente = nodo
                
                self.tamanio += 1
            except AttributeError:
                return False
            
    def agregarAntesDe(self, dato, valor):
        nodo = self.Nodo(valor)
        if self.tamanio == 0:
            return False
        elif dato == self.primero.dato:
            nodo.siguiente = self.primero
            self.primero = nodo
        else:
            try:
                actual = self.primero
                while actual.siguiente.dato != dato:
                    actual = actual.siguiente
                nodo.siguiente = actual.siguiente
                actual.siguiente = nodo
                
                self.tamanio += 1
            except AttributeError:
                return False
    
    def eliminar(self, valor): # Eliminamos un valor de la lista
        if self.tamanio == 0:
            return False
        elif valor == self.primero.dato:
            self.primero = self.primero.siguiente
            
        else:
            actual = self.primero
            try:
                while actual.siguiente.dato != valor:
                    actual = actual.siguiente
                
                nodoBorrar = actual.siguiente
                actual.siguiente = nodoBorrar.siguiente
                
            except AttributeError:
                return False
            
        self.tamanio -= 1
        
    def _len_(self): # Nos muestra la cantidad de datos que hay en la lista
        return self.tamanio
    
    def str(self):
        cadena = ''
        actual = self.primero
        while actual != None:
            cadena += str(actual.dato)
            cadena += '---->'
            actual = actual.siguiente
        cadena += 'None'
        return cadena
    
##------------ Lista simple Circular ------------
class listaCircular():
    class Nodo ():
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None
    
    def _init_(self):
        self.primero = None
        self.ultimo = None

    def AgregarInicio(self, dato):
        if self.esVacio():
            self.primero = self.ultimo = self.Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            auxiliar = self.Nodo(dato)
            auxiliar.siguiente = self.primero
            self.primero = auxiliar
            self.ultimo.siguiente = self.primero

    def AgregarFinal(self, dato):
        if self.esVacio():
            self.primero = self.ultimo = self.Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            auxiliar = self.ultimo
            self.ultimo = auxiliar.siguiente = self.Nodo(dato)
            self.ultimo.siguiente = self.primero  

# eliminar el inicio
# eliminar el final
# agregar despues
# agregar antes


##------------ Lista Doble Enlazada ------------
class ListaDoble():
    class Nodo:
        def _init_(self, dato):
            self.anterior = None
            self.dato = dato
            self.siguiente = None
    
    def _init_(self):
        self.primero = None
        self.ultimo = None
    

##------------ Lista Doble Circular ------------
class ListaDobleCircular:
    class Nodo:
        def _init_(self, dato):
            self.anterior = None
            self.siguiente = None
    
    def _init_(self):
        self.primero = None
        self.ultimo = None
