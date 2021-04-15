from pacientes import Paciente
from farmaceuticos import Farmaceutico
from datetime import datetime


""""
    Criar uma farmácia do SUS

    Classe para farmacêutica
    •	Receber a receita
    •	Validar receita
    •	Verificar estoque
    •	Entregar medicamento
    •	Retirar do estoque

    Classe para o paciente
    •	Ter uma receita (atributo)
    •	Ter um documento (atributo)

    Regras:
    Receita deve ter (Nome do medicamento, Validade, Quantidade, Nome do paciente)
    Receita deve ter só um medicamento
    Deve existir um estoque de medicamentos
    O documento do paciente deve coincidir com os dados da receita

"""

print("***** FARMAPY - SUS *****")

data_validade_medicamento = datetime.strptime('2021-05-15', "%Y-%m-%d").date()

receita1 = dict(nome_medicamento="ibunprofeno",
                   validade=data_validade_medicamento,
                   quantidade=1,
                   nome_paciente="Orlando",
                   cpf_paciente="0000000000")
print("-----------------")
paciente1 = Paciente("Orlando","0000000000",receita1)
dados_paciente = dict(nome= paciente1.nome,
                      cpf= paciente1.cpf)
print(paciente1)
print("-----------------")
farmaceutico1 = Farmaceutico("Gabriela")
print(farmaceutico1)

print("-----------------")
print("\nTESTE validar_receita: ")
farmaceutico1.receber_a_receita(dados_paciente, receita1)

print("-----------------")
print("\nTESTE validar_receita")
farmaceutico1.validar_receita(dados_paciente, receita1)

print("-----------------")
print("\nTESTE verificar estoque")
farmaceutico1.verificar_estoque(receita1)

print("-----------------")
print("\nTESTE retirar_do_estoque")
farmaceutico1.retirar_do_estoque(receita1)

print("-----------------")
print("\nTESTE entregar_medicamento")
farmaceutico1.entregar_medicamento(receita1)
