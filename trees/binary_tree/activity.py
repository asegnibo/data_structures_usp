class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def __str__(self):
        return str(self.data)

def construir_percorrer_arvore():
    n = int(input())
    nos_arvore = {}
    raiz = None

    for _ in range(n):
        linha = input().split()
        nome_no_atual = linha[0]

        if nome_no_atual not in nos_arvore:
            nos_arvore[nome_no_atual] = Node(nome_no_atual)
            no_atual = nos_arvore[nome_no_atual]

        if len(linha) > 1:
            nome_pai = linha[1]
            posicao = linha[2]

            if nome_pai not in nos_arvore:
                nos_arvore[nome_pai] = Node(nome_pai)
            
            no_pai = nos_arvore[nome_pai]

            if posicao == 'e':
                no_pai.left = no_atual
            elif posicao == 'd':
                no_pai.right = no_atual
        
        else:
            raiz = no_atual

    resultado_pre_ordem=[]

    def pre_ordem_travessia(no):
            if no:
                resultado_pre_ordem.append(no.data) # Visita a raiz
                pre_ordem_travessia(no.left)   # Percorre a subárvore esquerda
                pre_ordem_travessia(no.right)    # Percorre a subárvore direita

    pre_ordem_travessia(raiz)
    
    # Imprime o resultado formatado
    print(';'.join(resultado_pre_ordem))

# Chama a função principal para executar o programa
construir_percorrer_arvore()



