from ArbolesRojinegros import ArbolRojinegro


class RojinegroGenerador:
    # Ejemplo 1 rotación a la izquierda
    def ejemplo1(self):
        nodoIzq = ArbolRojinegro(
            None,
            None,
            1,
            True)

        nodoDerIzq = ArbolRojinegro(
            None,
            None,
            3,
            True)
        nodoDerDer = ArbolRojinegro(
            None,
            None,
            5,
            True)
        nodoDer = ArbolRojinegro(
            nodoDerIzq,
            nodoDerDer,
            4,
            False)
        raiz = ArbolRojinegro(
            nodoIzq,
            nodoDer,
            2,
            True)

        nodoDer.setFather(raiz)
        nodoIzq.setFather(raiz)
        nodoDerIzq.setFather(nodoDer)
        nodoDerDer.setFather(nodoDer)

        return raiz

    # Ejemplo 2 rotación a la izquierda
    def ejemplo2(self):
        nodoIzq = ArbolRojinegro(
            None,
            None,
            1,
            True)

        nodoDerIzq = ArbolRojinegro(
            None,
            None,
            6,
            True)

        nodoDerDer = ArbolRojinegro(
            None,
            None,
            9,
            True)

        nodoDer = ArbolRojinegro(
            nodoDerIzq,
            nodoDerDer,
            8,
            False)
        raiz = ArbolRojinegro(
            nodoIzq,
            nodoDer,
            5,
            True)
        nodoDer.setFather(raiz)
        nodoIzq.setFather(raiz)
        nodoDerIzq.setFather(nodoDer)
        nodoDerDer.setFather(nodoDer)
        return raiz

    # Ejemplo 3 para rotación a la derecha
    def ejemplo3(self):
        nodoIzqIzq = ArbolRojinegro(
            None,
            None,
            1,
            True)

        nodoIzqDer = ArbolRojinegro(
            None,
            None,
            3,
            True)

        nodoIzq = ArbolRojinegro(
            nodoIzqIzq,
            nodoIzqDer,
            2,
            False)

        nodoDer = ArbolRojinegro(
            None,
            None,
            5,
            True)
        raiz = ArbolRojinegro(
            nodoIzq,
            nodoDer,
            4,
            True)

        nodoIzq.setFather(raiz)
        nodoDer.setFather(raiz)
        nodoIzqDer.setFather(nodoDer)
        nodoIzqIzq.setFather(nodoIzq)
        return raiz


    # Ejemplo 4 para rotación a la derecha
    def ejemplo4(self):
        nodoIzqIzq = ArbolRojinegro(
            None,
            None,
            1,
            True)

        nodoIzqDer = ArbolRojinegro(
            None,
            None,
            6,
            True)

        nodoIzq = ArbolRojinegro(
            nodoIzqIzq,
            nodoIzqDer,
            5,
            False)
        nodoDer = ArbolRojinegro(
            None,
            None,
            9,
            True)
        raiz = ArbolRojinegro(
            nodoIzq,
            nodoDer,
            8,
            True)

        nodoIzq.setFather(raiz)
        nodoDer.setFather(raiz)
        nodoIzqDer.setFather(nodoDer)
        nodoIzqIzq.setFather(nodoIzq)
        return raiz
