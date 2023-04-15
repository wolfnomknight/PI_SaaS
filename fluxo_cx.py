
initial_value = 0.00
present_value = 0.00
value_income_options = ["Venda", "Investimento"]
value_outcome_options = ["Compra", "Despesa"]
day_dict = {"Data": "",
            "Total Entradas": 0.00,
            "Total Saídas": 0.00}


def criar_novo_caixa(data: str):
    caixa = day_dict
    caixa["Data"] = data
    return caixa


def muda_valor(caixa: dict, tipo: str, serv_ou_prod: str, valor: float, valor_atual=present_value):
    """Esta função coloca ou retira valores do fluxo de caixa:
    caixa: o dict que representa o fluxo de caixa do dia;
    tipo: dentre os valores presentes nas opções de entradas e saídas;
    serv_ou_prod: referente a que é o valor;
    valor: valor monetário;
    valor_atual: parâmetro opcional."""
    valor_atual += valor

    if tipo not in caixa:
        caixa[tipo] = [{serv_ou_prod: valor}]
    else:
        caixa[tipo].append({serv_ou_prod: valor})

    if tipo in value_income_options:
        caixa["Total Entradas"] += valor
    elif tipo in value_outcome_options:
        caixa["Total Saídas"] += valor


def fechar_caixa(caixa: dict):
    balance = caixa["Total Entradas"] - caixa["Total Saídas"]
    # Adicionar a consolidação do caixa do dia no banco de dados
    # - jogar os dados do caixa do dia para o BD
    return balance


# muda_valor(caixa=day_dict, tipo="Venda", serv_ou_prod="refri", valor=10.00, valor_atual=0)
# print(day_dict)
# muda_valor(caixa=day_dict, tipo="Venda", serv_ou_prod="chocolate", valor=20.00, valor_atual=0)
# print(day_dict)

