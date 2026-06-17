import pandas as pd
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent

def ler_csv():
    caminho = BASE_DIR / 'dados' / 'dirty_cafe_sales.csv'
    df = pd.read_csv(caminho)
    return df

def gera_novo_csv(df, nome_arquivo):
    df.to_csv(nome_arquivo, index=False)