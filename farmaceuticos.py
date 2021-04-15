from datetime import datetime


class Farmaceutico:

    def __init__(self, nome: str):
        self.nome = nome
        self.receitas_recebidas = {}

    def __str__(self):
        return f"Bem vindo a FARMAPY SUS, meu nome é {self.nome}!\n"

    def receber_a_receita(self, dados_paciente) -> bool:
        data_hora = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        self.receitas_recebidas = dict(hora_recebimento=data_hora, nome=dados_paciente.nome, cpf=dados_paciente.cpf,
                                       receita=dados_paciente.receita)
        print(f"Receita recebida: {self.receitas_recebidas}")
        return True

    def validar_receita(self, dados_paciente) -> bool:
        if dados_paciente.receita["nome_paciente"] == dados_paciente.nome \
                and dados_paciente.receita["validade"] >= datetime.today().date() \
                and dados_paciente.receita["quantidade"] >= 1\
                and dados_paciente.receita["cpf_paciente"] == dados_paciente.cpf:

            print("\nReceita válida.\n")
            return True
        else:
            print("\nDados inválidos! Erro no recebimento da receita, favor verificar dados informados.\n")
            return False

    def verificar_estoque(self, dados_paciente) -> bool:
        with open("estoque.txt", "r") as estoque_farmacia:
            itens_estoque = estoque_farmacia.readlines()

        for item in itens_estoque:
            medicamento_estoque = item.split(";")[0]
            quantidade_estoque = int(item.split(";")[1].strip())

            if medicamento_estoque == dados_paciente.receita["nome_medicamento"] \
                    and int(dados_paciente.receita["quantidade"]) <= quantidade_estoque:
                print(f'Item: {dados_paciente.receita["nome_medicamento"]}\n'
                      f'Estoque: {quantidade_estoque}\n')

                return True

        print("Item não localizado ou estoque insuficiente")
        return False

    def entregar_medicamento(self, dados_paciente) -> bool:
        print(f'Pegue seu remedio: {dados_paciente.receita["nome_medicamento"]}. '
              f'QTD: {dados_paciente.receita["quantidade"]}')
        return True

    def retirar_do_estoque(self, dados_paciente) -> bool:
        with open("estoque.txt", "r") as estoque_farmacia:
            itens_estoque = estoque_farmacia.readlines()

        for i in range(len(itens_estoque)):
            linha = itens_estoque[i].split(";")
            if linha[0] == dados_paciente.receita["nome_medicamento"] \
                    and dados_paciente.receita["quantidade"] <= int(linha[1].strip()):
                estoque_atual = int(linha[1].strip())
                estoque_restante = estoque_atual - int(dados_paciente.receita["quantidade"])

                print(f'\nItem: {dados_paciente.receita["nome_medicamento"]}\nSolicitado: '
                      f'{dados_paciente.receita["quantidade"]}\nEstoque: {linha[1]}\nRestante em estoque: '
                      f'{estoque_restante}\n')

                linha[1] = str(estoque_restante)+"\n"

                itens_estoque[i] = f"{linha[0]};{linha[1]}"

                with open("estoque.txt", "w") as file:
                    file.write("".join(itens_estoque))
                return True
        print("Item não localizado ou estoque insuficiente")
        return False
