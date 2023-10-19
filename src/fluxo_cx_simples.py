# Módulo de fluxo de caixa simples para funcionamento do site

import mysql.connector

import datetime
# Adicionando o datetime aqui mas no produto final o front-end deve enviar a data quando chamar as funções
data_atual = str(datetime.date.today())


class FluxoDeCaixa:
    """ Classe básica do fluxo de caixa, contem a data de abertura e um dicionário para os registros. """
    def __init__(self, data_atual):
        self.data_do_fluxo = data_atual
        self.indexacao_de_registro = 1
        self.registros = {}


def conexao_com_banco_de_dados(host_name, usuario, senha):
    """ Cria uma conexão com o banco de dados. """
    conexao = None
    try:
        conexao = mysql.connector.connect(host=host_name, user=usuario, passwd=senha)
        print("BD Conectado")
    except mysql.connector.Error:
        print(f"Deu merda: {mysql.connector.Error}")
    return conexao


banco_de_dados = conexao_com_banco_de_dados("host_name", "usuario", "senha")


def novo_fluxo_de_caixa(data_atual=data_atual):
    """ Cria um novo objeto de fluxo e atribui a data atual. """
    return FluxoDeCaixa(data_atual)


def novo_registro(fluxo, tipo, valor, descr, obs=""):
    """ Cria um novo registro dentro de um fluxo de caixa. """
    fluxo.registros[fluxo.indexacao_de_registro] = [tipo, valor, descr, obs]
    fluxo.indexacao_de_registro += 1
    return fluxo


def editar_registro(fluxo, chave, tipo=None, valor=None, descr=None, obs=None):
    """ Altera os dados de um registro existente. """
    if tipo is None:
        tipo = fluxo.registros[chave][0]
    if valor is None:
        valor = fluxo.registros[chave][1]
    if descr is None:
        descr = fluxo.registros[chave][2]
    if obs is None:
        obs = fluxo.registros[chave][3]
    fluxo.registros[chave] = [tipo, valor, descr, obs]
    return fluxo


def deletar_registro(fluxo, chave):
    """ Deleta um registro do fluxo. """
    del fluxo.registros[chave]
    return fluxo


def salvar_fluxo(fluxo):
    """ Salva os dados do fluxo de caixa no banco de dados. """
    # A ideia é salvar o objeto inteiro no BD, com nome igual à data
    # Atualmente a função apenas cria um arquivo de texto, mas isso deve ser alterado para lidar com o BD
    with open("banco_de_dados_teste.txt", "a") as file:
        file.write(fluxo.data_do_fluxo)
        for i in fluxo.registros:
            file.write(f"\n{fluxo.registros[i]}")


def ler_fluxo(data_do_fluxo):
    """ Lê um fluxo salvo no banco de dados, busca pela data. """
    leitura = f"READ DATABASE _ {data_do_fluxo}"
    return banco_de_dados.cursor().execute(leitura)

# Todas as funções precisam que indique qual o fluxo, exceto a de criar um novo fluxo (obvio) e a de ler um fluxo, que
# vai carregar o bicho do BD

# TESTES ===============
fluxo_teste = novo_fluxo_de_caixa()
print(fluxo_teste.data_do_fluxo)
novo_registro(fluxo_teste, "Entrada", 9.99, "Venda de Refrigerante")
novo_registro(fluxo_teste, "Saída", 2.99, "Compra de bombom")
print(fluxo_teste.registros)
editar_registro(fluxo_teste, 2, valor=1.99)
print(fluxo_teste.registros)
deletar_registro(fluxo_teste, 2)
print(fluxo_teste.registros)
salvar_fluxo(fluxo_teste)
