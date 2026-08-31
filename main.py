import os
import pandas as pd

lista_arquivo = os.listdir("/content/drive/MyDrive/Curso Básico de Python/Vendas")
display(lista_arquivo)

tabela_total = pd.DataFrame()

# Importar as bases de dados de vendas
for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"/content/drive/MyDrive/Curso Básico de Python/Vendas/{arquivo}")
        tabela_total = tabela_total.append(tabela)

display(tabela_total)

# Calcular o produto mais vendido (em quantidade)
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False)
display(tabela_produtos)

# Calculando o produto que mais faturou
tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
display(tabela_faturamento)

# Calcular a loja/cidade que mais vendeu (em faturamento)
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]
display(tabela_lojas)

import plotly.express as px

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()