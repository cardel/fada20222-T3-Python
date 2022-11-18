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
        raise NotImplementedError

    def maximo(self):
        raise NotImplementedError

    def minimo(self):
        raise NotImplementedError

    def search(self, x):
        raise NotImplementedError

    def rotacionDerecha(self, x):
        raise NotImplementedError

    def rotacionIzquierda(self, x):
        raise NotImplementedError

    #Area de pruebas
    def bfs(self):
        salida = ""
        separador = ""
        cola = []
        cola.append(self)

        while len(cola) > 0:
            nodo = cola.pop(0)
            salida += separador + str(nodo.value)
            separador = " "

            if nodo.izq is not None:
                cola.append(nodo.izq)

            if nodo.der is not None:
                cola.append(nodo.der)

        return salida

    def inorden(self):
        recorrido = ""
        separador = ""

        if self.izq is not None:
            recorrido += self.izq.inorden()
            separador = " "

        recorrido += separador + str(self.value)

        if self.der is not None:
            recorrido += " " + self.der.inorden()

        return recorrido
