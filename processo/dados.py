import pandas as pd
from pathlib import Path
from datetime import datetime
import smtplib
from email.message import EmailMessage

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

def envia_arquivo_email(caminho_arquivo, remetente, destinatario):

    # Configurações do servidor SMTP (exemplo com Gmail)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    remetente = remetente # Substitua pelo seu e-mail
    destinatario = destinatario  # Substitua pelo e-mail do destinatário
    senha = ''  # Senha do aplicativo ou senha real, dependendo da configuração

    # Criando a mensagem de e-mail
    msg = EmailMessage()
    msg['Subject'] = 'Arquivo CSV Processado'
    msg['From'] = remetente
    msg['To'] = destinatario
    msg.set_content('Segue em anexo o arquivo CSV processado.')

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(remetente, senha)
            with open(caminho_arquivo, 'rb') as f:
                msg.add_attachment(f.read(), maintype='application', subtype='csv', filename=caminho_arquivo.name)
            server.send_message(msg)
            print(f"E-mail enviado com sucesso para {destinatario}.")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")