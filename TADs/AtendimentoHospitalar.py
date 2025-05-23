

class AtendimentoHospitalar:
    def __init__(self):
        self.lista_pacientes = []
        # self.riscos_pacientes = []
        self.indice_atual = []
        
    def adicionar_paciente(self, paciente:str, risco:str):
        if risco == "vermelho" or risco == "amarelo" or risco == "verde":
            if risco == "vermelho":
                risco = 1
            elif risco == "amarelo":
                risco = 2
            elif risco == "verde":
                risco = 3
            self.lista_pacientes.append([paciente,risco])
            # self.riscos_pacientes.append(risco)
            # self.indice_atual.append()
        else:
            print("Digite o risco - Vermelho, Amarelo, Verde")
        
    def listar_pacientes(self):
        self.lista_ordem = sorted(self.lista_pacientes, key=lambda x:x[1])
        for i in range(len(self.lista_ordem)):
            print (f"Paciente: {self.lista_ordem[i][0]} - Risco: {self.lista_ordem[i][1]}")
            
            
            
            
atendimento = AtendimentoHospitalar()
atendimento.adicionar_paciente("João", "vermelho")
atendimento.adicionar_paciente("Maria", "amarelo")
atendimento.adicionar_paciente("José", "verde")
atendimento.adicionar_paciente("Ana", "vermelho")
print(atendimento.listar_pacientes())
