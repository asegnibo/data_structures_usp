import numpy as np

class Ativo:
    def __init__ (self, preco):
        self.preco = preco
        self.next = None
        self.prev = None
        
class ListaAtivos:
    def __init__ (self):
        self.inicio = None
        self.fim = None
    
    def adicionar_ativo(self, valor):
        novo = Ativo(valor)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.next = novo
            novo.prev = self.fim
            self.fim = novo
            
    def calcular_outliers(self):
        atual = self.inicio
        valores =[]
        while atual:
            valores.append(atual.preco)
            atual = atual.next
        q1 = np.percentile(valores, 25)
        q3 = np.percentile(valores, 75)
        iqr = q3 - q1
        
        lim_inf = q1 - 1.5 * iqr
        lim_sup = q3 + 1.5 * iqr
        
        outliers = [valor for valor in valores if valor < lim_inf or valor > lim_sup]
        
        return outliers
        
    def remover_outliers(self, outliers:list):
        atual = self.inicio
        
        while atual:
            if atual.preco in outliers:
                if atual.prev:  
                    atual.prev.next = atual.next
                if atual.next:  
                    atual.next.prev = atual.prev
                if atual == self.inicio: 
                    self.inicio = atual.next
                if atual == self.fim:  
                    self.fim = atual.prev
                atual = atual.next
            else:
                atual = atual.next
        
    def exibir_lista(self):
        atual = self.inicio
        
        while atual:
            print(atual.preco)
            atual = atual.next
  
ativo_1 = Ativo(120)
ativo_2 = Ativo(115)
ativo_3 = Ativo(118)
ativo_4 = Ativo(123)
ativo_5 = Ativo(119)
ativo_6 = Ativo(-80000)
ativo_7 = Ativo(1000000)
ativo_8 = Ativo(121)
ativo_9 = Ativo(116)
ativo_10 = Ativo(122)


lista = ListaAtivos()
lista.adicionar_ativo(ativo_1.preco)
lista.adicionar_ativo(ativo_2.preco)
lista.adicionar_ativo(ativo_3.preco)
lista.adicionar_ativo(ativo_4.preco)
lista.adicionar_ativo(ativo_5.preco)
lista.adicionar_ativo(ativo_6.preco)
lista.adicionar_ativo(ativo_7.preco)

print("Lista de ativos:")
lista.exibir_lista() 
outliers = lista.calcular_outliers()

print(f"\nOutliers:")
print(outliers)         

print(f"\nLista de ativos sem outliers:")
lista.remover_outliers(outliers)
lista.exibir_lista() 