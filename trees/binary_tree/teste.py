class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def __str__(self):
        return str(self.data)

def construir_percorrer_arvore():
    n = int(input()) # Lê o número total de nós
    nos_arvore = {}  # Dicionário para armazenar os objetos Node
    raiz = None      # Variável para armazenar a raiz da árvore
    erro = False     # Flag para indicar se algum erro de entrada ocorreu

    # Loop para processar cada linha de entrada correspondente a um nó
    for i in range(n): # 'i' é o índice da linha atual (0 a n-1)
        linha = input().split() # Lê e divide a linha de entrada
        nome_no_atual = linha[0] # Pega o nome do nó que está sendo inserido/conectado

        # Cria uma nova instância de Node para o nó atual se ela ainda não existir no dicionário
        if nome_no_atual not in nos_arvore:
            nos_arvore[nome_no_atual] = Node(nome_no_atual)
        
        # Obtém a referência ao objeto Node do nó atual
        no_atual = nos_arvore[nome_no_atual]

        # Verifica se a linha possui informações de pai e posição (indicando que não é a raiz isolada)
        if len(linha) > 1: 
            nome_pai = linha[1]    # Obtém o nome do nó pai
            posicao = linha[2]     # Obtém a posição ('e' para esquerda, 'd' para direita)

            # >>> Validação Crítica: Verifica se o nó pai já foi definido/encontrado <<<
            if nome_pai not in nos_arvore:
                print('Erro! Pai não encontrado!')
                erro = True
                # Consome as linhas de entrada restantes para evitar que o programa tente ler mais tarde
                # n - (i + 1) é o número de linhas que ainda não foram processadas
                for _ in range(n - (i + 1)): 
                    input() 
                break # Interrompe a construção da árvore ao encontrar um erro grave
            
            # Obtém a referência ao objeto Node do nó pai
            no_pai = nos_arvore[nome_pai]

            # Conecta o nó atual ao seu pai na posição especificada
            if posicao == 'e':
                no_pai.left = no_atual
            elif posicao == 'd':
                no_pai.right = no_atual
            else: # Tratamento de erro para posições inválidas
                print(f"Erro! Posição '{posicao}' inválida para o nó '{nome_no_atual}'. Use 'e' ou 'd'.")
                erro = True
                for _ in range(n - (i + 1)): # Consome as linhas restantes também neste caso de erro
                    input()
                break
        else: # Se a linha tem apenas um elemento, este nó é considerado a raiz
            # Valida se já existe uma raiz para evitar múltiplas raízes
            if raiz is not None:
                print(f"Erro! Múltiplas raízes detectadas.")
                erro = True
                for _ in range(n - (i + 1)): # Consome as linhas restantes também neste caso de erro
                    input()
                break
            raiz = no_atual # Define este nó como a raiz da árvore

    # Se a construção da árvore ocorreu sem erros, procede para a travessia em pré-ordem
    if not erro:
        resultado_pre_ordem = [] # Lista para armazenar os nomes dos nós na ordem de pré-ordem

        # Função auxiliar recursiva para realizar a travessia em pré-ordem
        def pre_ordem_travessia(no):
            if no: # Garante que o nó não é nulo (None)
                resultado_pre_ordem.append(no.data) # Visita o nó atual (adiciona seu dado à lista)
                pre_ordem_travessia(no.left)        # Percorre a subárvore esquerda
                pre_ordem_travessia(no.right)       # Percorre a subárvore direita

        pre_ordem_travessia(raiz) # Inicia a travessia a partir da raiz da árvore
        
        # Imprime o resultado final, com os nomes dos nós separados por ponto e vírgula
        print(';'.join(resultado_pre_ordem))

# Chama a função principal para iniciar a execução do programa
construir_percorrer_arvore()