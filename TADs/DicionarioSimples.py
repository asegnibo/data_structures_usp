

class DicionarioSimples:
    def __init__(self):
        self.dicionario = {}

    def inserir(self, chave, valor):
        self.dicionario[chave] = valor

    def buscar(self, chave):
        return self.dicionario.get(chave,None) # Retorna None se a chave não existir

    def remover(self, chave):
        if chave in self.dicionario:
            self.dicionario.pop(chave)
            # del self.dicionario[chave]

dic = DicionarioSimples()
dic.inserir("a", 1)
dic.inserir("b", 2)
dic.inserir("c", 3)
dic.inserir("d", 4)
dic.inserir("e", 5)

print(dic.buscar("a"))
dic.remover("b")

print(dic.dicionario)