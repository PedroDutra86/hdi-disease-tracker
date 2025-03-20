import pandas as pd

def load_data(file_path):
    """
    Carrega os dados de um arquivo CSV.

    Args:
        file_path (str): Caminho do arquivo CSV.

    Returns:
        pd.DataFrame: DataFrame com os dados carregados ou None se houver erro.
    """
    
    try:
        df = pd.read_csv(file_path, sep=",", encoding="utf-8")
        return df
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    except pd.errors.EmptyDataError:
        print(f"Erro: O arquivo '{file_path}' está vazio.")
    except pd.errors.ParserError:
        print(f"Erro: O arquivo '{file_path}' tem um formato inválido.")
    
    return None