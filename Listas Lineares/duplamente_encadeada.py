class Aluno:
    def __init__ (self,nome):
        self.nome = nome
        self.anterior = None
        self.proximo = None
    
class ListarAlunos:
    def __init__ (self):
        self.inicio = None
        self.fim = None
    
    def adicionar_aluno(self, nome):
        novo = Aluno(nome)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            novo.anterior = self.fim
            self.fim = novo
            
    def exibir_lista_inversa(self):
        atual = self.fim
        while atual:
            print(atual.nome) 
            atual = atual.anterior    
    
    
aluno_1 = Aluno("João")
aluno_2 = Aluno("Maria")
aluno_3 = Aluno("Pedro")
aluno_4 = Aluno("Ana")
aluno_5 = Aluno("Lucas")

lista = ListarAlunos()
lista.adicionar_aluno(aluno_1.nome)
lista.adicionar_aluno(aluno_2.nome)
lista.adicionar_aluno(aluno_3.nome)
lista.adicionar_aluno(aluno_4.nome)
lista.adicionar_aluno(aluno_5.nome)

lista.exibir_lista_inversa()