import pandas as pd

def load_data(file_path):
    """
    Carrega os dados de um arquivo Parquet.

    Args:
        file_path (str): Caminho do arquivo Parquet.

    Returns:
        pd.DataFrame: DataFrame com os dados carregados ou None se houver erro.
    """
    
    try:
        df = pd.read_parquet(file_path)
        return df
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    except pd.errors.EmptyDataError:
        print(f"Erro: O arquivo '{file_path}' está vazio.")
    except Exception as e:
        print(f"Erro: O arquivo '{file_path}' tem um formato inválido ou outro erro.\n{e}")
    
    return None
