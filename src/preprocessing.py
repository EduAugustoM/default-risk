import pandas as pd

def extrair_dados_csv(caminho_arquivo):
    arquivos = {
        'pagamentos_dev': 'base_pagamentos_desenvolvimento.csv',
        'info': 'base_info.csv',
        'cadastral': 'base_cadastral.csv',
        'pagamentos_teste': 'base_pagamentos_teste.csv'
    }
    dados = {}
    for chave, arquivo in arquivos.items():
        caminho_completo = f"{caminho_arquivo}/{arquivo}"
        try:
            dados[chave] = pd.read_csv(caminho_completo, sep=';')
        except FileNotFoundError:
            print(f"Arquivo {arquivo} não encontrado no caminho especificado.")
            dados[chave] = pd.DataFrame()

    return dados