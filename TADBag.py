class Elemento:
    #Valores dos dados
    valor: str
    num: int
    #Operações sobre os dados
    def __init__(self,valor:str):
        self.valor = valor
        self.num = 1
    def incrementa(self):
        self.num += 1
    def decrementa(self):
        if self.num == 0:
            print("Erro! Quantidade igual a zero")
            return -1
        self.num -= 1
        return 0
    def quantidade(self):
        return self.num
    def igual(self,valor:str):
        return self.valor == valor
    def imprimeElemento(self):
        print("Item: ",self.valor,"Quantidade: ",self.num)
        
class Sacola:
    used: int
    elems: list[Elemento]
    def __init__(self):
        self.used = 0
        self.elems = list()
    def insereElemento(self,nomeElemento:str):
        adicionou = False
        for i in range(self.used):
            if self.elems[i].igual(nomeElemento):
                self.elems[i].incrementa()
                adicionou = True
                break
        if not adicionou:
            self.elems.append(Elemento(nomeElemento))
            self.used += 1
    def listarElementos(self):
        for i in range(self.used):
            self.elems[i].imprimeElemento()
    def removeElemento(self,nomeElemento):
        for i in range(self.used):
            if self.elems[i].igual(nomeElemento):
                self.elems[i].decrementa()
                break
    
    def removeTipo(self,nomeElemento):
        for i in range(self.used):
            if self.elems[i].igual(nomeElemento):
                self.elems.remove(self.elems[i]) 
                self.used -= 1
                break       


if __name__ == '__main__':
    Sacola1 = Sacola()
    Sacola1.insereElemento("Quadrado")
    Sacola1.insereElemento("Triangulo")
    Sacola1.insereElemento("Cinculo")
    Sacola1.insereElemento("Triangulo")
    Sacola1.listarElementos()
    Sacola1.removeElemento("Triangulo")
    print("Nova lista")
    Sacola1.listarElementos()
    Sacola1.removeTipo("Quadrado")
    Sacola1.listarElementos()
        
__ 

# Aplicação de TAD (implementado em Python)
# Suponha que você precise implementar um sistema de gerenciamento de uma biblioteca. Escolha um TAD adequado para representar os livros e implemente as operações básicas:

# Adicionar um novo livro.
# Remover um livro.
# Buscar um livro pelo título.
# Listar todos os livros cadastrados.
# Considere as seguinte informações de um livro que devem ser salvam:

# Título do livro
# Nome do autor
# Número de páginas
# ISBN-13
# Arquivos de resposta Questão 1


class Livro:
    def __init__(self, titulo:str, autor:str, num_paginas:int,isbn:str):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.isbn = isbn
    
    def __str__(self):
        return (f"Título: {self.titulo}, Autor: {self.autor}, "
                f"Número de Páginas: {self.num_paginas}, ISBN-13: {self.isbn}")
        
        
class Biblioteca:
    def __init__(self):
        self.livros = []
        
    def adicionar_livro(self,livro:Livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado com sucesso!")
              
    def remover_livro(self,titulo:str):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                print(f"Livro '{titulo}' removido com sucesso!")
                return            
        print(f"Livro '{titulo}' não encontrado na biblioteca.")
        
    def buscar_livro(self, titulo:str):
        for livro in self.livros:
            if livro.titulo == titulo:
                print(f"Livro encontrado: {livro}")
                print(livro)
        print(f'Livro {livro} não encontrado na biblioteca.')
        return None
    
    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado na biblioteca.")
        else:
            print("Livros cadastrados na biblioteca:")
            for livro in self.livros:
                print(livro)        

bib= Biblioteca()
livro1 = Livro("Dom Casmurro", "Machado de Assis", 256, "978-85-359-0277-2")
livro2 = Livro("1984", "George Orwell", 328, "978-85-359-0278-9")

bib.adicionar_livro(livro1)
bib.adicionar_livro(livro2)

bib.listar_livros()

bib.buscar_livro("Dom Casmurro")

bib.remover_livro("Dom Casmurro")

bib.listar_livros()