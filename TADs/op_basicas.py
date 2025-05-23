# Modele um TAD Conjunto com as operações básicas: adicionar, remover, pertence, uniao, interseccao.

class Conjunto:
    def __init__(self):
        self.elementos=[]
        
    def adicionar(self,elemento):
        if elemento in self.elementos:
            return False
        else:
            self.elementos.append(elemento)
            return True
    
    def remover(self,elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
            return True
        else:
            return False
    
    def pertence(self, elemento):
        return elemento in self.elementos
    
    def uniao(self, outro_conjunto):
        novo_conjunto = Conjunto()
        novo_conjunto.elementos = self.elementos.copy()
        for elemento in outro_conjunto.elementos:
            if elemento not in novo_conjunto.elementos:
                novo_conjunto.adicionar(elemento)
        return novo_conjunto
    
    def interseccao(self, outro_conjunto):
        novo_conjunto = Conjunto()
        for elemento in self.elementos:
            if elemento in outro_conjunto.elementos:
                novo_conjunto.adicionar(elemento)
        return novo_conjunto
    
print("Teste do TAD Conjunto")
conjunto1 = Conjunto()
conjunto2 = Conjunto()
conjunto1.adicionar(1)
conjunto1.adicionar(2)
conjunto1.adicionar(3)
conjunto2.adicionar(3) 
conjunto2.adicionar(4)
conjunto2.adicionar(5)
print("Conjunto 1:", conjunto1.elementos)
print("Conjunto 2:", conjunto2.elementos)
print("União:", conjunto1.uniao(conjunto2).elementos)
print("Interseção:", conjunto1.interseccao(conjunto2).elementos)
print("Pertence:", conjunto1.pertence(2))
print("Pertence:", conjunto1.pertence(4))
print("Remover:", conjunto1.remover(2))
print("Conjunto 1 após remoção:", conjunto1.elementos)
print("Remover:", conjunto1.remover(4))
print("Conjunto 1 após tentativa de remoção de elemento não existente:", conjunto1.elementos)
print("Adicionar:", conjunto1.adicionar(2))
print("Conjunto 1 após adição de elemento já existente:", conjunto1.elementos)
print("Adicionar:", conjunto1.adicionar(4))
print("Conjunto 1 após adição de novo elemento:", conjunto1.elementos)
