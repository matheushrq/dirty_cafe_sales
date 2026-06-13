from dados import ler_csv
import pandas as pd

df = ler_csv()

# coluna item
def corrige_coluna_item():
    
    # Buscar o item com menos registros, excluindo 'ERROR' e 'UNKNOWN'
    valores_validos = df.loc[~df['Item'].isin(['ERROR', 'UNKNOWN']), 'Item']
    item_menos_frequente = valores_validos.value_counts().idxmin()

    # Atribuindo o item menos frequente aos dados com erro
    df.loc[df['Item'].isin(['ERROR', 'UNKNOWN']), 'Item'] = item_menos_frequente

    # Buscando dados nulos
    item_mais_frequente = df['Item'].value_counts().idxmax()
    df['Item'].fillna(item_mais_frequente, inplace=True)

def corrige_coluna_payment_method():

    # Atribuindo o item mais frequente aos dados com erro
    pag_mais_frequente = df['Payment Method'].value_counts().idxmax()
    df.loc[df['Payment Method'].isin(['ERROR', 'UNKNOWN']), 'Payment Method'] = pag_mais_frequente

    # Buscando dados nulos e atribuindo o item menos frequente a eles
    pag_menos_frequente = df['Payment Method'].value_counts().idxmin()
    df['Payment Method'].fillna(pag_menos_frequente, inplace=True)

def corrige_transaction_date():
    
    # Convertendo coluna 'Transaction Date' para datetime e atribuindo para a data atual
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')
    df['Transaction Date'] = df['Transaction Date'].fillna(pd.Timestamp.today())

def corrige_coluna_location():

    # Filtrando apenas os valores válidos, excluindo 'ERROR' e 'UNKNOWN'
    valor_valido = df.loc[~df['Location'].isin(['ERROR', 'UNKNOWN']), 'Location']
    local_mais_frequente = valor_valido.value_counts().idxmax()
    local_menos_frequente = valor_valido.value_counts().idxmin()

    df.loc[df['Location'] == 'ERROR', 'Location'] = local_mais_frequente
    df.loc[df['Location'] == 'UNKNOWN', 'Location'] = local_menos_frequente

    df['Location'].fillna('Other', inplace=True)