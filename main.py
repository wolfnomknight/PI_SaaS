# Projeto integrador 2023
# Univesp Campus São Bernardo do Campo

from fastapi import FastAPI
import fluxo_cx
import datetime


# ==== O código abaixo é usado para teste ==== #
caixa_do_dia = fluxo_cx.criar_novo_caixa(data=str(datetime.date.today()))
# print(caixa_do_dia)

fluxo_cx.muda_valor(caixa=caixa_do_dia, tipo="Venda", serv_ou_prod="Refrigerante Coca-Cola 2l", valor=7.50)
fluxo_cx.muda_valor(caixa=caixa_do_dia, tipo="Venda", serv_ou_prod="Coxinha", valor=4.00)
fluxo_cx.muda_valor(caixa=caixa_do_dia, tipo="Compra", serv_ou_prod="Pacote Guardanapo", valor=10.00)
print(caixa_do_dia)

print(fluxo_cx.fechar_caixa(caixa_do_dia))

# TODO: Buscar dados do banco de dados
# TODO: Controle de estoque
# TODO: Ponto de equilibrio e sugestao de preços
# TODO: Interação com a interface
