

class Musica:
    def __init__(self, titulo):
        self.titulo = titulo
        self.next = None
        
class Playlist:
    def __init__(self):
        self.inicio = None
    
    def add_inicio(self, titulo):
        nova = Musica(titulo)
        nova.next = self.inicio
        self.inicio = nova
        print(f"Adicionada música '{titulo}' no início da playlist.")
        
    def add_fim(self, titulo):
        nova = Musica(titulo)
        if self.inicio is None:
            self.inicio = nova
        else:
            atual = self.inicio
            while atual.next:
                atual = atual.next
            atual.next = nova
        print(f"Adicionada música '{titulo}' no fim da playlist.")
    
    def add_posicao(self, titulo_referencia, novo_titulo): # Adiciona nova música após a música de referência
        atual = self.inicio
        while atual:
            if atual.titulo == titulo_referencia:
                nova = Musica(novo_titulo)
                nova.next = atual.next 
                atual.next = nova
                print(f"Adicionada música '{novo_titulo}' após '{titulo_referencia}' na playlist.")
                return
            atual = atual.next
        print(f"Música '{titulo_referencia}' não encontrada na playlist.")
        
    def buscar_musica(self,titulo_busca):
        atual=self.inicio
        while atual:
            if atual.titulo == titulo_busca:
                print(f"Música '{titulo_busca}' encontrada na playlist.")
                return True
            atual=atual.next
        print(f"Música '{titulo_busca}' não encontrada na playlist.")
        return None
    
    def exibir_playlist(self):
        atual = self.inicio
        if atual is None:
            print("Playlist vazia.")
            return
        while atual:
            print(atual.titulo)
            atual = atual.next

playlist = Playlist()
playlist.add_inicio("Música A")
playlist.add_fim("Música C")
playlist.add_fim("Música B")
playlist.exibir_playlist()

playlist.add_posicao("Música A", "Música D")
playlist.add_posicao("Música E", "Música F")
playlist.exibir_playlist()

playlist.buscar_musica("Música B")
playlist.buscar_musica("Música Z")


            
        