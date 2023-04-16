
present_value = 0.00

# O value_income_options e o value_outcome_options devem ser baixados do banco de dados, usando estas listas para
# demonstrar o funcionamento pretendido
value_income_options = ["Venda", "Investimento"]
value_outcome_options = ["Compra", "Despesa"]

day_dict = {"Data": "",
            "Total Entradas": 0.00,
            "Total Saídas": 0.00}


def alterar_opcoes_de_fluxo(income: bool, add: bool, name: str):
    """ Função para adicionar ou retirar tipos de entradas e saídas."""
    # Primeiro, verifica qual lista será alterada
    if income:
        # Verifica se vai adicionar ou retirar um item e executa a mudança
        if add:
            value_income_options.append(name)
        else:
            value_income_options.remove(name)

    else:
        if add:
            value_outcome_options.append(name)
        else:
            value_outcome_options.remove(name)


def criar_novo_caixa(data: str):
    """Função executada no início de um novo dia onde será necessário um fluxo de caixa.
    Cria um dicionário contendo a data atual e o total de entradas e saídas."""
    caixa = day_dict
    caixa["Data"] = data
    return caixa


def muda_valor(caixa: dict, tipo: str, serv_ou_prod: str, valor: float):
    """Esta função coloca ou retira valores do fluxo de caixa. Adiciona valores e descritivos no dicionário do caixa do dia.
    caixa: o dict que representa o fluxo de caixa do dia;
    tipo: dentre os valores presentes nas opções de entradas e saídas;
    serv_ou_prod: referente a que é o valor;
    valor: valor monetário."""
    if tipo not in caixa:
        caixa[tipo] = [{serv_ou_prod: valor}]
    else:
        caixa[tipo].append({serv_ou_prod: valor})

    if tipo in value_income_options:
        caixa["Total Entradas"] += valor
    elif tipo in value_outcome_options:
        caixa["Total Saídas"] += valor


def fechar_caixa(caixa: dict):
    """Função executada ao final do dia. Calcula o saldo e envia as informações do caixa ao banco de dados."""
    balance = caixa["Total Entradas"] - caixa["Total Saídas"]
    # Adicionar a consolidação do caixa do dia no banco de dados
    # - jogar os dados do caixa do dia para o BD
    return balance
