from dados import ler_csv, gera_novo_csv, envia_arquivo_email
from analise import Analise

def main():
    df = ler_csv()
    analise = Analise(df)

    analise.corrige_coluna_item()
    analise.corrige_coluna_payment_method()
    analise.corrige_transaction_date()
    analise.corrige_coluna_location()
    analise.corrige_coluna_quantity()
    analise.corrige_coluna_price()
    analise.corrige_coluna_total_spent()

    gera_novo_csv(analise.df, 'clean_cafe_sales.csv')
    
    envia_arquivo_email('pronto/clean_cafe_sales.csv', '', '')

if __name__ == "__main__":
    main()