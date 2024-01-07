class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacidade

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            raise Exception("a pilha está cheia, não é possível adicionar mais elementos.")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def top(self):
        if not self.is_empty():
            return self.items[-1]


pilha = Pilha(capacidade=5)
pilha.push(1)
pilha.push(2)
pilha.push(3)
print("Topo da pilha:", pilha.top())
pilha.pop()
print("Topo da pilha após pop:", pilha.top())
