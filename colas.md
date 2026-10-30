Una **cola** es una estructura de datos lineal en la que los elementos se insertan por un extremo llamado **final** y se eliminan por el otro extremo llamado **frente**. Sigue el principio **FIFO (First In, First Out)**, es decir, _el primer elemento en entrar es el primero en salir_.

**Ejemplo:** una fila de personas esperando en una caja. La primera persona en llegar es la primera en ser atendida.

Operaciones principales:

- `enqueue()` → agrega un elemento al final de la cola.
- `dequeue()` → elimina el elemento que está al frente.
- `front()` o `peek()` → consulta el elemento al frente sin eliminarlo.

En el contexto de las listas enlazadas, una pila puede implementarse insertando y eliminando nodos al inicio de la lista, mientras que una cola puede implementarse manteniendo referencias tanto al primer como al último nodo para que las operaciones de inserción y eliminación se realicen en tiempo constante **O(1)**.

## Cola implementada desde cero

```python
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
```

## La clase `Nodo`

```python
class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
```

Es idéntica a la de la pila: guarda un `dato` y una referencia al `siguiente` nodo (o `None`).

## La clase `Cola`

```python
class Cola():
    def __init__(self):
        self.frente = None
        self.final = None
```

Aquí hay **dos referencias**, no una:

- `frente`: el primer elemento, el que saldrá primero.
- `final`: el último elemento, donde entran los nuevos.

Si `frente` es `None`, la cola está vacía.

## Encolar (enqueue)

```python
nuevo = Nodo(dato)

if self.frente is None:
    self.frente = nuevo
    self.final = nuevo
else:
    self.final.siguiente = nuevo
    self.final = nuevo
```

Hay dos casos:

**Cola vacía:** el nuevo nodo es a la vez el frente y el final.

`frente → [10] ← final`

**Cola con elementos:** el nodo `final` actual apunta al nuevo, y luego `final` pasa a ser el nuevo.

Encolando 20 y 30 después del 10:

```
frente → [10] → [20] → [30] → None
                         ↑
                       final
```

Gracias a que se guarda `final`, no hace falta recorrer la lista para llegar al último nodo.

**Importante**: `None` siempre debe aparecer donde termina el último enlace de la estructura, independientemente de dónde coloquemos visualmente el frente y el final.

## Desencolar (dequeue)

```python
if self.frente is None:
	raise IndexError("La cola está vacía")

dato = self.frente.dato
self.frente = self.frente.siguiente

if self.frente is None:
    self.final = None

return dato
```

1. Si la cola está vacía, lanza `IndexError`.
2. Guarda el dato del frente.
3. Mueve `frente` al siguiente nodo.
4. **Si la cola quedó vacía**, también pone `final = None`.
5. Devuelve el dato.

El paso 4 es importante. Si solo hubiera un elemento, al hacer `dequeue` el `frente` queda en `None`, pero `final` seguiría apuntando al nodo eliminado. Eso dejaría la cola en un estado inconsistente, y el siguiente `enqueue` (que en ese caso entra por la rama `if`, así que funcionaría) ocultaría el error, pero la referencia colgante mantendría vivo un nodo que debería liberarse.

Ejemplo: `dequeue` sobre la cola anterior devuelve `10`:

```
frente → [20] → [30] → None
                  ↑
                final
```

## Mirar al frente (peek)

Devuelve `self.frente.dato` **sin eliminarlo**. Lanza `IndexError` si está vacía.

## Recorer (show)

Para recorrer la cola utilizando un ciclo while, debes comenzar desde frente y avanzar mediante el atributo siguiente hasta encontrar None.

```python
while self.frente is not None:
  print(self.frente.dato, end="->")
  self.frente = self.frente.siguiente

  print("None")
```

Esta instrucción permite avanzar de un nodo al siguiente, exactamente igual que hicimos con las listas enlazadas.

Observa que comenzamos desde self.frente, no desde self.final, porque queremos recorrer la cola siguiendo el orden en que serán atendidos los clientes.
