

from collections import deque

def inverte_fila(fila):
    pilha_aux = []

    while fila:
        pilha_aux.append(fila.popleft())

    while pilha_aux:
        fila.append(pilha_aux.pop())

def main_inverte_fila():
    fila_f1 = deque()
    
    while True:
        elemento = input("digite um elemento (ou 's' para sair): ")
        if elemento.lower() == 's':
            break
        fila_f1.append(int(elemento))

    inverte_fila(fila_f1)
    print("fila f1 invertida:", list(fila_f1))

if __name__ == "__main__":
    main_inverte_fila()
