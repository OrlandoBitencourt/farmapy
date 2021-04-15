from datetime import datetime

class Farmaceutico:


    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return f"Bem vindo a FARMAPY SUS, meu nome é {self.nome}!\n"

    def receber_a_receita(self, dados_paciente, receita: dict) -> bool:
        data_hora = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        self.receitas_recebidas = dict(hora_recebimento=data_hora, nome=dados_paciente.nome, cpf=dados_paciente.cpf, receita=receita)
        print(f"Receita recebida: {self.receitas_recebidas}")
        return True

    def validar_receita(self, dados_paciente, receita: dict) -> bool:
        if receita["nome_paciente"] == dados_paciente.nome \
                and receita["validade"] >= datetime.today().date() \
                and receita["quantidade"] >= 1\
                and receita["cpf_paciente"] == dados_paciente.cpf:

            print("\nReceita válida.\n")
            return True
        else:
            print("\nDados inválidos! Erro no recebimento da receita, favor verificar dados informados.\n")
            return False

    def verificar_estoque(self, receita: dict) -> bool:
        with open("estoque.txt", "r") as estoque_farmacia:
            itens_estoque = estoque_farmacia.readlines()

        for item in itens_estoque:
            medicamento_estoque = item.split(";")[0]
            quantidade_estoque = int(item.split(";")[1].strip())

            if medicamento_estoque == receita["nome_medicamento"] and int(receita["quantidade"]) <= quantidade_estoque:
                print(f'Item: {receita["nome_medicamento"]}\n'
                      f'Estoque: {quantidade_estoque}\n')

                return True

        print("Item não localizado ou estoque insuficiente")
        return False

    def entregar_medicamento(self, receita: dict) -> bool:
        print(f'Pegue seu remedio: {receita["nome_medicamento"]}. QTD: {receita["quantidade"]}')
        return True

    def retirar_do_estoque(self, receita: dict) -> bool:
        with open("estoque.txt", "r") as estoque_farmacia:
            itens_estoque = estoque_farmacia.readlines()

        for i in range(len(itens_estoque)):
            linha = itens_estoque[i].split(";")
            if linha[0] == receita["nome_medicamento"] and receita["quantidade"] <= int(linha[1].strip()):
                estoque_atual = int(linha[1].strip())
                estoque_restante = estoque_atual - int(receita["quantidade"])

                print(f'\nItem: {receita["nome_medicamento"]}\n'
                        f'Solicitado: {receita["quantidade"]}\n'
                        f"Estoque: {linha[1]}\n"
                        f"Restante em estoque: {estoque_restante}\n")

                linha[1] = str(estoque_restante)+"\n"

                itens_estoque[i] = f"{linha[0]};{linha[1]}"

                with open("estoque.txt", "w") as file:
                    file.write("".join(itens_estoque))
                return True
        print("Item não localizado ou estoque insuficiente")
        return False