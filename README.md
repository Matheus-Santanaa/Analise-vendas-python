# 📊 Análise de Vendas com Python

Projeto de análise de dados que identifica produtos mais vendidos, faturamento por produto e desempenho por loja, com visualização interativa em Plotly. Dados fictícios, usados para fins de estudo.

## 🎯 O que o projeto faz

- Lê e consolida vários arquivos CSV de vendas em uma única base
- Identifica o produto mais vendido em quantidade
- Calcula o produto que mais gerou faturamento
- Compara o faturamento entre as diferentes lojas
- Gera um gráfico de barras interativo (Plotly) com o faturamento por loja

## 🛠️ Tecnologias utilizadas

- Python 3
- Pandas
- Plotly

## 📁 Estrutura do projeto

```
analise-vendas/
├── dados/                  # arquivos CSV de vendas
├── analise_vendas.py       # script principal
├── requirements.txt        # dependências do projeto
└── README.md
```

## ▶️ Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/analise-vendas-python.git
   cd analise-vendas-python
   ```

2. (Opcional, mas recomendado) Crie um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Rode o script:
   ```bash
   python analise_vendas.py
   ```

O gráfico de faturamento por loja vai abrir automaticamente no seu navegador.

## 📈 Resultado

*(cole aqui um print do gráfico gerado, depois de rodar o projeto)*

## 🚀 Possíveis melhorias futuras

- Transformar em dashboard web interativo (Streamlit)
- Adicionar filtros por período e por produto
- Exportar relatórios em PDF/Excel automaticamente

## ✍️ Autor

Seu Nome — [LinkedIn](#) | [GitHub](#)
