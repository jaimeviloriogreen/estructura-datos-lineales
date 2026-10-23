# type: ignore

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    def __init__(self) -> None:
        self.tope = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def mostrar(self):
        while self.tope is not None:
            print(self.tope.dato, end="->")

            self.tope = self.tope.siguiente

    def eliminar_tope(self):
        if self.tope is None:
            raise IndexError("La lista no tiene elementos")

        dato = self.tope.dato
        self.tope = self.tope.siguiente

        return dato

    def consultar_tope(self):
        if self.tope is None:
            raise IndexError("La lista no tiene elementos")

        return self.tope.dato

    def esta_vacia(self):
        return self.tope is None


pila_numeros = Pila()
# pila_numeros.eliminar_tope()

pila_numeros.agregar(10)
pila_numeros.agregar(20)
pila_numeros.agregar(30)

# print(pila_numeros.consultar_tope())
print(pila_numeros.eliminar_tope())

pila_numeros.mostrar()
