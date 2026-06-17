import pandas as pd
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

def ler_csv():
    caminho = BASE_DIR / 'dados' / 'dirty_cafe_sales.csv'
    df = pd.read_csv(caminho)
    return df

def gera_novo_csv(df, nome_arquivo):
    try:
        caminho = BASE_DIR / 'pronto' / nome_arquivo
        # Garantir que o diretório pai exista
        caminho.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(caminho, index=False)
        print(f"Arquivo '{nome_arquivo}' gerado com sucesso em: {caminho}")
    except Exception as e:
        print(f"Erro ao gerar o arquivo '{nome_arquivo}': {e}")