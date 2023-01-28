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