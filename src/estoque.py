
day_stock = {"Data": "",}
# O default_stock deverá ser baixado do banco de dados
# O formato é nome: [quantidade em estoque, estoque mínimo, preço de venda]
default_stock = {"Refrigerante Coca-Cola 2l": [10, 5, 7.50],
                 "Salgado Coxinha de Frango": [5, 5, 4.00],
                 "Chocolate Lacta Diamante Negro": [4, 2, 8.00]}


def alterar_estoque_padrao(add: bool, name: str, value: float):
    """ Função para alterar o estoque padrão utilizado, ou seja, quais produtos/serviços serão considerados
    no controle de estoque do dia."""
    if add:
        default_stock[name] = value
    else:
        default_stock.pop(name)


def criar_controle_de_estoque_diario(data: str):
    """ Função para criar um dicionário de controle de estoque para o dia."""
    # Cria um dicionário contendo a data e todos os itens padrão.
    stock = day_stock
    stock["Data"] = data
    for item in default_stock:
        day_stock[item] = default_stock[item]
    return stock


def mudar_quantidade_de_estoque(stock: dict, name: str, qnt: int):
    """ Função para alterar a quantidade de um produto no estoque. Deve entrar um valor negativo para saídas (vendas)
    e um valor positivo para entradas (reestocagem)."""
    if stock[name][0] + qnt <= 0:
        # TODO: Este aviso deve ser alterado para aparecer na interface
        print("Não há estoque suficiente para esta venda, favor verificar.")
    stock[name][0] += qnt


def forcar_mudanca_de_estoque(stock: dict, name: str, qnt: int):
    """ Função usada para corrigir erros de estoque, ela define um valor para o estoque de um produto ao invés de
    alterar por uma determinada quantidade."""
    stock[name][0] = qnt


def fechar_controle_de_estoque_diario(stock: dict):
    for item in stock:
        # TODO: Jogar os dados de estoque para o banco de dados
        # TODO: Estes avisos devem ser alterados para aparecer na interface
        if stock[item][0] == 0:
            print(f"O produto {item} está com estoque zerado!")
        elif stock[item][0] < 0:
            print(f"O produto {item} está com erro de quantidade em estoque!")
        elif stock[item][0] < stock[item][1]:
            print(f"O produto {item} está abaixo do estoque mínimo, hora de comprar mais!")
