#Exercício 4.3

from collections import deque

def verifica_ordem_crescente(fila):
    fila_aux = deque()
    elemento_anterior = float('-inf')

    while fila:
        elemento = fila.popleft()
        fila_aux.append(elemento)

        if elemento < elemento_anterior:
            return False

        elemento_anterior = elemento

    # Restaura a fila original
    fila.extend(fila_aux)
    return True

def main_verifica_ordem_crescente():
    fila_exemplo = deque()
    
    while True:
        elemento = input("digite um elemento (ou 's' para sair): ")
        if elemento.lower() == 's':
            break
        fila_exemplo.append(int(elemento))

    if verifica_ordem_crescente(fila_exemplo):
        print("a fila está ordenada de forma crescente.")
    else:
        print("a fila não está ordenada de forma crescente.")

if __name__ == "__main__":
    main_verifica_ordem_crescente()
