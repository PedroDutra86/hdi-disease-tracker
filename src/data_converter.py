import pandas as pd
import os

from data_cleaner import clean_data
from data_loader import load_data
from data_selector import select_data

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    raw_data_path = os.path.join(base_dir, "..", "data", "raw", "DENGBR23.parquet") # Alterar nome do arquivo de acordo com arquivo que estiver trabalhando
    processed_dir = os.path.join(base_dir, "..", "data", "processed")
    output_path = os.path.join(processed_dir, "DENGBR23_processed.parquet") # Alterar nome do arquivo de acordo como quiser salvar

    os.makedirs(processed_dir, exist_ok=True) # Se não existir a pasta no caminho, cria

    df = load_data(raw_data_path)
    df = select_data(df)
    df = clean_data(df)

    # Remove colunas duplicadas antes de filtrar
    df = df.loc[:, ~df.columns.duplicated()]

    # df_petropolis = df[df["Município"] == "Petrópolis"] # Mudar o Município caso queira um df filtrado
    df.to_parquet(output_path, index=False)

if __name__ == "__main__":
    main()
