# Este arquivo contem sugestoes ao usuario quanto a precificação e estoque mínimo de produtos

# O default_stock deverá ser baixado do banco de dados
# É igual ao estoque finalizado no dia anterior
# O formato é nome: [quantidade em estoque, estoque mínimo, preço de venda, vendidos hoje]
default_stock = {"Refrigerante Coca-Cola 2l": [10, 5, 7.50, 1],
                 "Salgado Coxinha de Frango": [5, 5, 4.00, 2],
                 "Chocolate Lacta Diamante Negro": [4, 2, 8.00, 3]}

# Quantos dias serão considerados para calculo das sugestões, padrão é 30
DAYS_TO_BE_USED = 30
# Qual a margem de lucro a ser adicionada em cada produto, padrão é 30%
PROFIT_MARGIN = 0.3


def set_default_days(number: int):
    """ Define quantos dias serão usados do banco de dados para cálculo das sugestões, padrão é 30."""
    global DAYS_TO_BE_USED
    DAYS_TO_BE_USED = number


def set_profit(profit: float):
    """ Define qual a margem de lucro a ser aplicada nos produtos."""
    global PROFIT_MARGIN
    PROFIT_MARGIN = profit


def get_stocks_from_database():
    """ Cria uma lista de dicionários com os dados para calcular as sugestões."""
    # Esta variável deve ser trazida do banco de dados, é o número total de dias que estão armazenados no DB
    qnt_days_in_database = 30

    calculate_days = 0

    if qnt_days_in_database > DAYS_TO_BE_USED:
        calculate_days = DAYS_TO_BE_USED
    else:
        calculate_days = qnt_days_in_database

    stocks = list()

    for day_index in range(calculate_days):
        # Este loop serve para colocar dias do banco de dados na lista "stocks", para calcular as sugestoes
        stocks.append(default_stock)  # Ainda deve ser alterado, atualmente usado para teste

    return stocks


def get_products(stock_list):
    """ Retorna uma lista de produtos que estão presentes nos dias selecionados do banco de dados."""
    product_list = list()
    for index in stock_list:
        for product in index:
            if product not in product_list:
                product_list.append(product)
    return product_list


def calculate_minimum_stock(product: str, days_to_restock: int, stocks: list):
    """ Calcula o valor recomendado de estoque mínimo para um determinado produto."""
    total_usage = 0
    product_days = 0
    for index in stocks:
        if product in index:
            total_usage += index[product][3]
            product_days += 1
    average_usage = int(total_usage / product_days)
    return average_usage * days_to_restock


def calculate_price(product: str):
    """ Calcula o preço do produto de acordo com a margem de lucro estabelecida."""
    # TODO: Tudo nessa função
    pass


# === Teste === #
calculate_stocks = get_stocks_from_database()
quantity_of_stocks = len(calculate_stocks)
products = get_products(calculate_stocks)
print(calculate_minimum_stock("Chocolate Lacta Diamante Negro", 7, calculate_stocks))
# print(quantity_of_stocks)
# print(calculate_stocks)
# print(products)
