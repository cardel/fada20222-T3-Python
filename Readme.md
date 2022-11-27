# Taller 3 Rojinegros en Python

## Creacion ambiente virtual

python3 -m venv env
source env/bin/activate
pip -r requerimientos.txt

## Nota para windows

En lugar de usar el comando python3 o python usar py

## Recursos

http://www.rmboot.com/RedBlack.html

## Cambios

Se ha agregado una referencia al padre en las pruebas, puede hacer este cambio para tener el nodo padre

```python
def __init__(self, izq, der, value, black):
    self.izq = izq
    self.der = der
    self.value = value
    self.black = black
    self.father = None;

def setFather(self, father):
    self.father = father;
```