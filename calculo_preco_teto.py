import pandas as pd
import yfinance as yf


# Extraindo os dados da ação do yahoo finance
acao = input('Qual ação você deseja analisar? ').upper()
acao = acao + '.SA'
codigo = yf.Ticker(acao)
historico = codigo.history(period = '5y')
# print(historico)

# Extraindo o histórico de dividendos da ação
dividendos = codigo.dividends
dados = pd.DataFrame(dividendos).reset_index()
print(f'\n{dados}')

# Calculando a média de pagamentos de dividendos nos ultimos 5 anos
soma_dividendos = dados.Dividends.sum()
print(f'\nNos últimos 5 anos, o total de dividendos pago por cada ação de {acao} foi de R$ {soma_dividendos:.2f}')

pagamento_medio = soma_dividendos / 5
print(f'Pagamento médio de dividendos por ano: R$ {pagamento_medio:.2f}')

# Calculando o preço teto da ação
def preco_teto(pagamento_medio, dividendo_esperado):
  return print(f'Preço teto (máximo recomendado à pagar pela ação): R$ {pagamento_medio / dividendo_esperado:.2f}')

dividendo_desejado = float(input('\nQual a porcentagem esperada de pagamento do dividendo? (Usual = 6%) ')) / 100

# print(f'\nO preço atual da ação é de R$' {codigo.splits})
preco_teto(pagamento_medio, dividendo_desejado)
