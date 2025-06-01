class Node:
    """
    Representa um nó na árvore binária.
    Cada nó armazena um dado (nome do nó) e referências para os filhos esquerdo e direito.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    """
    Implementação do Tipo Abstrato de Dados (TAD) para uma Árvore Binária.
    """
    def __init__(self):
        self.root = None
        # Dicionário para armazenar referências a nós por seus nomes,
        # facilitando a busca de nós pais.
        self.nodes = {}

    def add_root(self, data):
        """
        Adiciona o nó raiz à árvore.
        Assume que os nomes dos nós são únicos.
        """
        if self.root is None:
            node = Node(data)
            self.root = node
            self.nodes[data] = node
            return True
        return False # Raiz já existe

    def search_node(self, data):
        """
        Busca um nó na árvore pelo seu nome.
        Retorna o objeto Node se encontrado, caso contrário None.
        """
        return self.nodes.get(data)

    def add_child(self, child_data, parent_data, position):
        """
        Adiciona um nó filho (esquerdo ou direito) a um nó pai existente.
        Imprime mensagens de erro conforme especificado se a adição falhar.
        Assume que child_data é o nome de um novo nó a ser inserido.
        """
        parent_node = self.search_node(parent_data)

        if not parent_node:
            print("Erro! Pai não encontrado!")
            return False

        # Verifica se o nome do nó filho já existe no dicionário de nós.
        # O problema não especifica um erro para "nó já existe", mas para que
        # self.nodes funcione como um mapa de nomes únicos para nós,
        # é implícito que os nomes dos nós inseridos são únicos.
        # A lógica aqui assume que child_data é para um novo nó.
        if child_data in self.nodes:
            # Este erro não está na especificação do problema, mas seria uma inconsistência.
            # Vamos seguir estritamente as mensagens de erro fornecidas.
            # Se um nó com child_data já existe e tentamos adicioná-lo novamente,
            # a referência em self.nodes[child_data] seria sobrescrita para o novo nó.
            # O exemplo sugere nomes únicos (A, B, C...), então vamos assumir que
            # os inputs para child_data são para nós genuinamente novos na árvore.
            pass


        if position == 'e': # Filho esquerdo
            if parent_node.left is not None:
                print("Erro! Filho já existe!")
                return False
            child_node = Node(child_data)
            parent_node.left = child_node
            self.nodes[child_data] = child_node
        elif position == 'd': # Filho direito
            if parent_node.right is not None:
                print("Erro! Filho já existe!")
                return False
            child_node = Node(child_data)
            parent_node.right = child_node
            self.nodes[child_data] = child_node
        else:
            print("Erro! Opção de posição errada!")
            return False
        return True

    def get_pre_order(self):
        """
        Gera uma lista de nomes de nós visitados em pré-ordem.
        """
        result = []
        self._pre_order_recursive(self.root, result)
        return result

    def _pre_order_recursive(self, node, result_list):
        if node:
            result_list.append(node.data)
            self._pre_order_recursive(node.left, result_list)
            self._pre_order_recursive(node.right, result_list)

    def get_in_order(self):
        """
        Gera uma lista de nomes de nós visitados em ordem (in-order).
        """
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result_list):
        if node:
            self._in_order_recursive(node.left, result_list)
            result_list.append(node.data)
            self._in_order_recursive(node.right, result_list)

    def get_post_order(self):
        """
        Gera uma lista de nomes de nós visitados em pós-ordem.
        """
        result = []
        self._post_order_recursive(self.root, result)
        return result

    def _post_order_recursive(self, node, result_list):
        if node:
            self._post_order_recursive(node.left, result_list)
            self._post_order_recursive(node.right, result_list)
            result_list.append(node.data)

    def get_height(self):
        """
        Calcula a altura da árvore.
        A altura de uma árvore com um único nó é 0.
        A altura de uma árvore vazia é -1.
        """
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1  # Altura de subárvore vazia
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)

def main():
    """
    Função principal para processar a entrada, construir a árvore e gerar a saída.
    """
    tree = BinaryTree()

    try:
        num_additional_nodes = int(input())
        root_name = input()

        if not root_name.strip(): # Validação básica do nome da raiz
            # O problema não especifica erro para nome de raiz inválido,
            # mas é uma boa prática considerar.
            # print("Erro! Nome da raiz não pode ser vazio.")
            return
        
        tree.add_root(root_name)
        if tree.root is None: # Falha ao adicionar raiz (improvável com a lógica atual)
            return


        for _ in range(num_additional_nodes):
            line = input().split()
            if len(line) == 3:
                child_name, parent_name, position = line
                tree.add_child(child_name, parent_name, position)
            # else:
                # O problema não especifica como lidar com linhas mal formatadas
                # print("Erro! Linha de entrada de nó mal formatada.")

        # Gerar saídas
        pre_order_list = tree.get_pre_order()
        print(";".join(pre_order_list) + ";" if pre_order_list else "")

        in_order_list = tree.get_in_order()
        print(";".join(in_order_list) + ";" if in_order_list else "")

        post_order_list = tree.get_post_order()
        print(";".join(post_order_list) + ";" if post_order_list else "")
        
        print(tree.get_height())

    except EOFError:
        # Fim de arquivo inesperado
        pass
    except ValueError:
        # Erro ao converter num_additional_nodes para int
        # print("Erro! Número de nós inválido.")
        pass
    # Outras exceções podem ser tratadas se necessário

if __name__ == "__main__":
    main()