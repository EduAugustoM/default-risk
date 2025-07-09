import pandas as pd

def converter_colunas_datetime(df, lista_colunas):
    for coluna in lista_colunas:
        df[coluna] = pd.to_datetime(df[coluna])
    return df

def mostrar_linhas_vazias(df):
    linhas_antes = df.shape[0]
    linhas_depois = df.dropna().shape[0]
    linhas_vazias = linhas_antes - linhas_depois
    percentual = 100 - (linhas_depois * 100 / linhas_antes) if linhas_antes > 0 else 0

    print(
        f"  - Linhas antes: {linhas_antes}\n"
        f"  - Linhas depois: {linhas_depois}\n"
        f"  - Linhas vazias: {linhas_vazias} ({percentual:.2f}% do total)"
    )

