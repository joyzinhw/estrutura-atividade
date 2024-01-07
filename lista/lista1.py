class arraylist:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def append(self, item):
        self.items.append(item)

    def insert_at_index(self, index, item):
        self.items.insert(index, item)

    def remove_at_index(self, index):
        if 0 <= index < len(self.items):
            del self.items[index]
        else:
            print("índice fora do intervalo.")

    def get_element_at_index(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        else:
            return None

    def get_size(self):
        return len(self.items)

    def concatenate(self, other_list):
        new_list = arraylist()
        new_list.items = self.items + other_list.items
        return new_list

    def divide(self, index):
        if 0 <= index < len(self.items):
            left_list = arraylist()
            right_list = arraylist()

            left_list.items = self.items[:index]
            right_list.items = self.items[index:]

            return left_list, right_list
        else:
            print("índice fora do intervalo.")
            return None, None

    def copy(self):
        new_list = arraylist()
        new_list.items = self.items.copy()
        return new_list

    def search(self, item):
        return item in self.items


def menu_interativo():
    minha_lista = arraylist()

    while True:
        print("1. adicionar elemento")
        print("2. remover elemento por índice")
        print("3. concatenar com outra lista")
        print("4. dividir a lista")
        print("5. copiar a lista")
        print("6. procurar elemento")
        print("7. ver a lista")
        print("8. sair")

        escolha = input("digite a sua escolha (1-8): ")

        if escolha == "1":
            elemento = input("digite o elemento que você deseja adicionar: ")
            minha_lista.append(elemento)
        elif escolha == "2":
            indice = int(input("digite o índice do elemento que você deseja remover: "))
            minha_lista.remove_at_index(indice)
        elif escolha == "3":
            outra_lista = arraylist()
            elemento = input("digite um elemento para adicionar à segunda lista: ")
            outra_lista.append(elemento)
            resultado = minha_lista.concatenate(outra_lista)
            print("lista concatenada:", resultado.items)
        elif escolha == "4":
            indice = int(input("digite o índice para dividir a lista: "))
            esquerda, direita = minha_lista.divide(indice)
            print("lista à esquerda:", esquerda.items)
            print("lista à direita:", direita.items)
        elif escolha == "5":
            lista_copiada = minha_lista.copy()
            print("lista copiada:", lista_copiada.items)
        elif escolha == "6":
            elemento = input("digite o elemento para procurar: ")
            resultado = minha_lista.search(elemento)
            print(f"o elemento {elemento} está na lista? {resultado}")
        elif escolha == "7":
            print("lista atual:", minha_lista.items)
        elif escolha == "8":
            print("encerrando o programa. adeus!")
            break
        else:
            print("escolha inválida. por favor, digite um número entre 1 e 8.")


if __name__ == "__main__":
    menu_interativo()
