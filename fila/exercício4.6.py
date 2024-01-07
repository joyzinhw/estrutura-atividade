from typing import Union

class Fila:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item: Union[int, str]):
        # Adiciona um elemento ao final da fila
        self.items.append(item)

    def dequeue(self) -> Union[int, str, None]:
        # Remove e retorna o elemento no início da fila, se a fila não estiver vazia
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self) -> Union[int, str, None]:
        # Retorna o elemento no início da fila, se a fila não estiver vazia
        if not self.is_empty():
            return self.items[0]
        return None


fila = Fila()
fila.enqueue(5)
fila.enqueue("hello")
fila.enqueue(3)
print("Frente da fila:", fila.front())

while not fila.is_empty():
    print("Desenfileirando:", fila.dequeue())
