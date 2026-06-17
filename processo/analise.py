from dados import ler_csv
import pandas as pd

df = ler_csv()

class Analise:
    def __init__(self, df):
        self.df = df

    def corrige_coluna_item(self):
    
        # Buscar o item com menos registros, excluindo 'ERROR' e 'UNKNOWN'
        valores_validos = self.df.loc[~self.df['Item'].isin(['ERROR', 'UNKNOWN']), 'Item']
        item_menos_frequente = valores_validos.value_counts().idxmin()

        # Atribuindo o item menos frequente aos dados com erro
        self.df.loc[self.df['Item'].isin(['ERROR', 'UNKNOWN']), 'Item'] = item_menos_frequente

        # Buscando dados nulos e preenchendo sem usar 'inplace' para evitar warnings
        item_mais_frequente = self.df['Item'].value_counts().idxmax()
        self.df['Item'] = self.df['Item'].fillna(item_mais_frequente)

    def corrige_coluna_payment_method(self):

        # Atribuindo o item mais frequente aos dados com erro
        pag_mais_frequente = self.df['Payment Method'].value_counts().idxmax()
        self.df.loc[self.df['Payment Method'].isin(['ERROR', 'UNKNOWN']), 'Payment Method'] = pag_mais_frequente

        # Buscando dados nulos e atribuindo o item menos frequente a eles
        pag_menos_frequente = self.df['Payment Method'].value_counts().idxmin()
        self.df['Payment Method'] = self.df['Payment Method'].fillna(pag_menos_frequente)

    def corrige_transaction_date(self):

        # Convertendo coluna 'Transaction Date' para datetime e atribuindo para a data atual
        self.df['Transaction Date'] = pd.to_datetime(self.df['Transaction Date'], errors='coerce')
        self.df['Transaction Date'] = self.df['Transaction Date'].fillna(pd.Timestamp.today())

    def corrige_coluna_location(self):

        # Filtrando apenas os valores válidos, excluindo 'ERROR' e 'UNKNOWN'
        valor_valido = self.df.loc[~self.df['Location'].isin(['ERROR', 'UNKNOWN']), 'Location']
        local_mais_frequente = valor_valido.value_counts().idxmax()
        local_menos_frequente = valor_valido.value_counts().idxmin()

        self.df.loc[self.df['Location'] == 'ERROR', 'Location'] = local_mais_frequente
        self.df.loc[self.df['Location'] == 'UNKNOWN', 'Location'] = local_menos_frequente

        # Preencher valores nulos sem 'inplace' para evitar chained-assignment warnings
        self.df['Location'] = self.df['Location'].fillna('Other')

    def corrige_coluna_quantity(self):

        # convertendo a coluna 'Quantity' para numérica, atribuindo 0 para os erros
        self.df['Quantity'] = pd.to_numeric(self.df['Quantity'], errors='coerce').fillna(0).astype(int)

    def corrige_coluna_price(self):

        # convertendo a coluna 'Price Per Unit' para float, atribuindo 0 para os erros
        self.df['Price Per Unit'] = pd.to_numeric(self.df['Price Per Unit'], errors='coerce').fillna(0.0)

    def corrige_coluna_total_spent(self):

        # convertendo a coluna 'Total Spent' para float, atribuindo 0 para os erros
        self.df['Total Spent'] = pd.to_numeric(self.df['Total Spent'], errors='coerce').fillna(0.0)