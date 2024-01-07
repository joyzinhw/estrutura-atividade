class Pilha:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()


def decimal_para_binario(decimal):
    pilha = Pilha()

    # Lidando com o caso especial de 0
    if decimal == 0:
        return "0"

    resultado = ""
    while decimal > 0:
        resto = decimal % 2
        pilha.push(resto)
        decimal //= 2

    while not pilha.is_empty():
        resultado += str(pilha.pop())

    return resultado


numero_decimal = int(input("digite o número decimal: "))


resultado_binario = decimal_para_binario(numero_decimal)
print("o resultado em binário é:", resultado_binario)
