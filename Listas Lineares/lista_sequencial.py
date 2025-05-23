# Desenvolva um sistema de gerenciamento de tarefas onde cada tarefa possui um t´ ıtulo, uma descri¸c˜ao e uma posi¸c˜ ao de prioridade. Utilize uma lista sequencial para armazenar as tarefas e implemente opera¸c˜ oes para inserir, remover e reordenar tarefas em qualquer posi¸c˜ ao da lista.

class Tarefa:
    def __init__ (self, titulo, desc, pos):
        self.titulo = titulo
        self.desc = desc
        self.pos = pos    
    def __str__ (self): # retorna uma representação em string da tarefa
        return f'Tarefa: {self.titulo}, Descrição: {self.desc}, Posição: {self.pos}' 
    
class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
    
    def inserir_tarefa(self, tarefa):
        # Adiciona uma nova tarefa na lista de tarefas
        self.tarefas.append(tarefa)
        self.tarefas.sort(key=lambda x: x.pos)
        return True
    
    def remover_tarefa(self,pos):
        # Remove uma tarefa da lista de tarefas com base na posição
        if pos < 0 or pos >= len(self.tarefas):
            print("Posição inválida.")
            return False
        else:
            self.tarefas.pop(pos)
            return True
        
    def reordenar_tarefa(self, pos, nova_pos):
        # Reordena uma tarefa na lista de tarefas com base na nova posição
        if pos < 0 or pos >= len(self.tarefas) or nova_pos < 0 or nova_pos >= len(self.tarefas):
            print("Posição inválida.")
            return False
        else:
            tarefa = self.tarefas.pop(pos)         
            tarefa.pos = nova_pos
            self.tarefas.insert(nova_pos, tarefa)
            self.tarefas.sort(key=lambda x:x.pos)
            return True
            
tarefa_1 = Tarefa("Tarefa 1", "Descrição da tarefa 1", 2)
tarefa_2 = Tarefa("Tarefa 2", "Descrição da tarefa 2", 1)
tarefa_3 = Tarefa("Tarefa 3", "Descrição da tarefa 3", 3)
tarefa_4 = Tarefa("Tarefa 4", "Descrição da tarefa 4", 0)
tarefa_5 = Tarefa("Tarefa 5", "Descrição da tarefa 5", 4)

gerenciar = GerenciadorTarefas()
gerenciar.inserir_tarefa(tarefa_1)
gerenciar.inserir_tarefa(tarefa_2)
gerenciar.inserir_tarefa(tarefa_3) 
gerenciar.inserir_tarefa(tarefa_4)
gerenciar.inserir_tarefa(tarefa_5)

print("Lista de tarefas após inserção:")
for tarefa in gerenciar.tarefas:
    print(tarefa) # imprime a lista de tarefas após inserção

gerenciar.remover_tarefa(2) # remove a tarefa na posição 2
print("Lista de tarefas após remoção:")
for tarefa in gerenciar.tarefas:
    print(tarefa) # imprime a lista de tarefas após remoção
    
gerenciar.reordenar_tarefa(1, 3) # reordena a tarefa na posição 1 para a posição 3
print("Lista de tarefas:")
for tarefa in gerenciar.tarefas:
    print(tarefa) # imprime a lista de tarefas após reordenação