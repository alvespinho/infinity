#### ORIENTAÇÃO A OBJETO USANDO MODULAGEM 

class Vizinho:
    def __init__(self, nome: str, telefone: str, nascimento= "01/01/2001"):
        self.nome = nome
        self.nascimento = nascimento
        self.telefone = telefone
    
    def ToString (self):
        return f"""Nome: {self.nome},
                Telefone: {self.telefone},
                Nascimento {self.nascimento}"""
