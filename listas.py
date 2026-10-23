# type: ignore
from nodo import Nodo

class ListaEnlazada:
    """Lista enlazada simple"""

    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
            return

        actual = self.cabeza

        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza

        while actual:
            print(actual.dato, end="->")
            actual = actual.siguiente
        print("None")

    def eliminar():
        # TODO: Implementar eliminar un nodo
        """Elimina un nodo de la lista enlazada enlazada simple"""
        pass


lista = ListaEnlazada()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)
lista.agregar(40)
lista.agregar(50)
lista.agregar(60)

lista.mostrar()
