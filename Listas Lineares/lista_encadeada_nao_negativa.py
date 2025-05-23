class ValorTransacao:
    def __init__ (self, valor):
        self.valor = valor
        self.proximo = None
    
class ListaTransacoesPositivas:
    def __init__ (self):
        self.inicio = None
    
    def adicionar_valor (self, valor):
        novo = ValorTransacao(valor)
        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo  
            atual.proximo = novo
            
    def remover_negativos(self):
        while self.inicio and self.inicio.valor < 0:
            self.inicio = self.inicio.proximo

        atual = self.inicio
        while atual and atual.proximo:
            if atual.proximo.valor < 0:
                atual.proximo = atual.proximo.proximo
            else:
                atual = atual.proximo
        
        
    def exibir_lista(self):
        atual = self.inicio
        while atual:
            print(atual.valor)
            atual = atual.proximo

valor_1 = ValorTransacao(100)
valor_2 = ValorTransacao(200)
valor_3 = ValorTransacao(300)
valor_4 = ValorTransacao(400)
valor_5 = ValorTransacao(500)

lista = ListaTransacoesPositivas()
lista.adicionar_valor(valor_1.valor)
lista.adicionar_valor(valor_2.valor)
lista.adicionar_valor(valor_3.valor)
lista.adicionar_valor(valor_4.valor)
lista.adicionar_valor(valor_5.valor)

print("Lista de transações positivas:")
lista.remover_negativos()

print("Lista de transações:")
lista.exibir_lista()


