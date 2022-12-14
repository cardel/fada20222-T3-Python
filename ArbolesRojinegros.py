"""
Clase para arboles rojinegros
"""


class ArbolRojinegro:

    def __init__(self, izq, der, value, black):
        self.izq = izq
        self.der = der
        self.value = value
        self.black = black
        self.father = None

    def setFather(self, father):
        self.father = father

    def insertar(self, x):
        if self.value == 0 and self.father == None:
            self.value = x
        else:
            if x >= self.value:
                if self.der == None:
                    self.der = ArbolRojinegro(None, None, x, 1)
                    self.der.father = self
                else:
                    self.der.insertar(x)
            else:
                if x < self.value:
                    if self.izq == None:
                        self.izq = ArbolRojinegro(None, None, x, 1)
                        self.izq.father = self
                    else:
                        self.izq.insertar(x)

    def insertarfixup(self, x):

        if self.value == 0:
            self.value = x
        while self.father and self.black == 0:
            if self.father == self.father.father.der:
                y = self.father.father.izq
                if y and y.black == 0:
                    self.black = 1
                    self.father.black = 1
                    self.father.father.black = 0
                    self = self.father.father
                else:
                    if self == self.father.izq:
                        self = self.father
                        self.rotacionDerecha(self)
                    self.father.black = 1
                    self.father.father.black = 0
                    self.rotacionIzquierda(self.father.father)
            else:
                y = self.father.father.der
                if y and y.black == 0:
                    self.black = 1
                    self.father.black = 1
                    self.father.father.black = 0
                    self = self.father.father
                else:
                    if self == self.father.izq:
                        self = self.father
                        self.rotacionIzquierda(self)
                    self.father.black = 1
                    self.father.father.black = 0
                    self.rotacionDerecha(self.father.father)
            if self is None:
                break
        self.black = 1

    def maximo(self):
        nodo = self
        while nodo.der is not None:
            nodo = nodo.der
        return nodo.value

    def minimo(self):
        nodo = self
        while nodo.izq is not None:
            nodo = nodo.izq
        return nodo.value

    def search(self, x):
        if self is None or x is self.value:
            return self
        elif x > self.value:
            return self.der.search(x)
        elif x < self.value:
            return self.izq.search(x)

    def rotacionD



    # #Area de pruebas
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
