# Estrutura de Dados - Atividade 1
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