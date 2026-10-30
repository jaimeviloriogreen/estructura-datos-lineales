# type:ignore

class Nodo:
    def __init__(self, dato) -> None:
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self) -> None:
        self.frente = None
        self.final = None

    def enqueue(self, dato):
        """Agrega un elemento al final de la cola"""

        nuevo = Nodo(dato)

        if self.frente is None:
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def dequeue(self):
        """Elimina el elemento que está al frente"""

        if self.frente is None:
            raise IndexError("La cola está vacía")

        dato = self.frente.dato
        self.frente = self.frente.siguiente

        if self.frente is None:
            self.frente = None

        return dato

    def peek(self):
        """Consulta el elemento del frente sin eliminarlo"""
        if self.frente is None:
            raise IndexError("La cola está vacía")

        return self.frente.dato

    def show(self):
        """Muestra todas los nodos de la cola"""

        while self.frente is not None:
            print(self.frente.dato, end="->")
            self.frente = self.frente.siguiente

        print("None")


cola = Cola()

cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)

# cola.dequeue()  # Atendí al primer cliente
# print(cola.dequeue())
# print(cola.dequeue())


# print(cola.peek())

cola.show()  # Se recorre en el mismo orden en que son atendidos
