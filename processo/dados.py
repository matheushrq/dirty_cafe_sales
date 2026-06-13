import pandas as pd
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

def ler_csv():
    caminho = BASE_DIR / 'dados' / 'dirty_cafe_sales.csv'
    df = pd.read_csv(caminho)
    return df

df = ler_csv()

# Verificando quantos registros existem por item
qtd_itens = df.groupby(['Item']).size()
print(qtd_itens)

# Buscar o item com mais registros
item_mais_frequente = df['Item'].value_counts().idxmax()
print(item_mais_frequente)

# Buscar o item com menos registros, excluindo 'ERROR' e 'UNKNOWN'
valores_validos = df.loc[~df['Item'].isin(['ERROR', 'UNKNOWN']), 'Item']
item_menos_frequente = valores_validos.value_counts().idxmin()
print(item_menos_frequente)

df.loc[df['Item'].isin(['ERROR', 'UNKNOWN']), 'Item'] = item_menos_frequente

df.head(20)

df['Item'].isnull().sum()

df['Item'].fillna(item_mais_frequente, inplace=True)

df.head(20)

metodos = df.groupby(['Payment Method']).size()
print(metodos)

pag_mais_frequente = df['Payment Method'].value_counts().idxmax()
print(pag_mais_frequente)

pag_menos_frequente = df['Payment Method'].value_counts().idxmin()
print(pag_menos_frequente)

df.loc[df['Payment Method'].isin(['ERROR', 'UNKNOWN']), 'Payment Method'] = pag_mais_frequente

df.head(20)

df['Payment Method'].isnull().sum()

df['Payment Method'].fillna(pag_menos_frequente, inplace=True)

df.head(20)

datas_erradas = df[df['Transaction Date'].isin(['ERROR', 'UNKNOWN'])]
print(datas_erradas)

df.info()

# convertendo a coluna transaction date para datetime
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

df.head(15)

df['Transaction Date'] = df['Transaction Date'].fillna(pd.Timestamp.today())

df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

df[df.index == 11]

df.head(15)

erro_local = df.groupby(['Location']).size()
print(erro_local)

valor_valido = df.loc[~df['Location'].isin(['ERROR', 'UNKNOWN']), 'Location']
local_mais_frequente = valor_valido.value_counts().idxmax()
local_menos_frequente = valor_valido.value_counts().idxmin()

print(local_mais_frequente)
print(local_menos_frequente)

df.loc[df['Location'] == 'ERROR', 'Location'] = local_mais_frequente
df.loc[df['Location'] == 'UNKNOWN', 'Location'] = local_menos_frequente

df.head(15)

df['Location'].fillna('Other', inplace=True)

df.head(15)