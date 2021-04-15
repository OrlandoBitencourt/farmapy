class Paciente():


    def __init__(self, nome: str, cpf: str, receita: dict):
        self.nome = nome
        self.cpf = cpf
        self.receita = receita

    def __str__(self):
        return (f"Nome: {self.nome}\n" \
               f"CPF: {self.cpf}\n" \
               f"Receita: {self.receita}\n")