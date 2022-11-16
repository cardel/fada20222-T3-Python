"""
Clase para arboles rojinegros
"""

class ArbolRojinegro:
    def __init__(self, izq, der, value, black):
        self.izq = izq
        self.der = der
        self.value = value
        self.black = black

    def insertar(self, x):
        raise NotImplemented

    def maximo(self):
        raise NotImplemented

    def minimo(self):
        raise NotImplemented

    def search(self, x):
        raise NotImplemented

    def rotacionDerecha(self, x):
        raise NotImplemented

    def rotacionIzquierda(self, x):
        raise NotImplemented

    """
    Area de pruebas
    """
    def bfs(self):
        salida = ""
        separador = ""
        cola = []
        cola.append(self)

        while(len(cola)>0):
            nodo = cola.pop(0)
            salida += separador + str(nodo.value)
            separador = " "

            if nodo.izq != None:
                cola.append(nodo.izq)

            if nodo.der != None:
                cola.append(nodo.der)

        return salida

    def inorden(self):
        recorrido = ""
        separador = ""

        if self.izq != None:
            recorrido += self.izq.inorden()
            separador = " "

        recorrido += separador + str(self.value)

        if self.der != None:
            recorrido += " " + self.der.inorden()

        return recorrido


