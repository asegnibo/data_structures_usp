# Modele e implemente um TAD HistoricoNavegador que armazene as paginas visitadas em um navegador. Ele deve permitir visitar uma nova pagina, voltar para a pagina anterior e avancar para a proxima pagina (caso tenha voltado anteriormente).

class HistoricoNavegador:
    def __init__ (self):
        self.historico = []
        self.indice_atual = -1
        
    def visitar_pagina(self, pagina: str):
        self.historico = self.historico[:self.indice_atual +1]
        self.historico.append(pagina)
        self.indice_atual += 1
        
    def voltar(self):
        if self.indice_atual > 0:
            self.indice_atual -+ 1
            return self.historico[self.indice_atual]
        return None
    
    def avancar(self):
        if self.indice_atual < len(self.historico) - 1:
            self.indice_atual += 1
            return self.historico[self.indice_atual]
        return None
    
    def obter_pagina_atual(self):
        if self.indice_atual >= 0:
            return self.historico[self.indice_atual]
        return None
    
historico = HistoricoNavegador()

# Visitando páginas
historico.visitar_pagina("Página 1")
historico.visitar_pagina("Página 2")
historico.visitar_pagina("Página 3")

print(historico.obter_pagina_atual())  # Deve imprimir "Página 3"

# Voltando para páginas anteriores
print(historico.voltar())  # Deve imprimir "Página 2"
print(historico.voltar())  # Deve imprimir "Página 1"
print(historico.voltar())  # Deve imprimir None (não há mais páginas anteriores)

# Avançando para páginas seguintes
print(historico.avancar())  # Deve imprimir "Página 2"
print(historico.avancar())  # Deve imprimir "Página 3"
print(historico.avancar())  # Deve imprimir None (não há mais páginas seguintes)