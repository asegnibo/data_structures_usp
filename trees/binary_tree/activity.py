class NoArvore:
    def __init__(self, nome):
        self.nome = nome
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        self.erro = None

    def adicionar_filho(self, nome_pai, nome_filho, posicao):
        if self.raiz is None:
            self.raiz = NoArvore(nome_filho)
            return

        pai = self._busca_no(self.raiz, nome_pai)
        if pai is None:
            self.erro = "Erro! Pai não encontrado!"
            return

        novo_no = NoArvore(nome_filho)
        if posicao == "e":
            if pai.esquerda:
                self.erro = "Erro! Filho já existe!"
            else:
                pai.esquerda = novo_no
        elif posicao == "d":
            if pai.direita:
                self.erro = "Erro! Filho já existe!"
            else:
                pai.direita = novo_no
        else:
            self.erro = "Erro! Opção de posição errada!"

    def _busca_no(self, no_atual, nome_busca):
        if no_atual is None:
            return None
        if no_atual.nome == nome_busca:
            return no_atual

        encontrado = self._busca_no(no_atual.esquerda, nome_busca)
        if encontrado:
            return encontrado

        return self._busca_no(no_atual.direita, nome_busca)

    def busca_no(self, nome_busca):
        return self._busca_no(self.raiz, nome_busca)

    def _percorre_em_ordem(self, no_atual, lista):
        if no_atual:
            self._percorre_em_ordem(no_atual.esquerda, lista)
            lista.append(no_atual.nome)
            self._percorre_em_ordem(no_atual.direita, lista)

    def gera_lista_em_ordem(self):
        lista = []
        self._percorre_em_ordem(self.raiz, lista)
        return lista

    def _percorre_pre_ordem(self, no_atual, lista):
        if no_atual:
            lista.append(no_atual.nome)
            self._percorre_pre_ordem(no_atual.esquerda, lista)
            self._percorre_pre_ordem(no_atual.direita, lista)

    def gera_lista_pre_ordem(self):
        lista = []
        self._percorre_pre_ordem(self.raiz, lista)
        return lista

    def _percorre_pos_ordem(self, no_atual, lista):
        if no_atual:
            self._percorre_pos_ordem(no_atual.esquerda, lista)
            self._percorre_pos_ordem(no_atual.direita, lista)
            lista.append(no_atual.nome)

    def gera_lista_pos_ordem(self):
        lista = []
        self._percorre_pos_ordem(self.raiz, lista)
        return lista

    def _calcula_altura(self, no_atual):
        if no_atual is None:
            return -1  # Altura de uma árvore vazia é -1 (por convenção)

        altura_esquerda = self._calcula_altura(no_atual.esquerda)
        altura_direita = self._calcula_altura(no_atual.direita)

        return 1 + max(altura_esquerda, altura_direita)

    def calcula_altura_arvore(self):
        return self._calcula_altura(self.raiz)

    def apresentar_erro(self):
        return self.erro


# --- Entrada e Saída ---
if __name__ == "__main__":
    arvore = ArvoreBinaria()

    n = int(input())

    for i in range(n):
        linha = input().split()
        if i == 0:
            arvore.adicionar_filho(None, linha[0], None)  # Adiciona o nó raiz
        else:
            nome_filho = linha[0]
            nome_pai = linha[1]
            posicao = linha[2]
            arvore.adicionar_filho(nome_pai, nome_filho, posicao)

    if arvore.apresentar_erro() == None:
        print(";".join(arvore.gera_lista_pre_ordem()) + ";")
        print(";".join(arvore.gera_lista_em_ordem()) + ";")
        print(";".join(arvore.gera_lista_pos_ordem()) + ";")
        print(arvore.calcula_altura_arvore())
    else:
        print(arvore.apresentar_erro())
