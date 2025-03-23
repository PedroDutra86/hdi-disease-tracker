import pandas as pd
import os

from data_cleaner import clean_data
from data_loader import load_data
from data_selector import select_data

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    raw_data_path = os.path.join(base_dir, "..", "data", "raw", "DENGBR25.csv")
    processed_dir = os.path.join(base_dir, "..", "data", "processed")
    output_path = os.path.join(processed_dir, "DENGBR25_processed.csv")

    os.makedirs(processed_dir, exist_ok=True)

    df = load_data(raw_data_path)
    df = select_data(df)
    df = clean_data(df)
    df_petro = df[df["Município da Notificação"] == "Petrópolis"]

    df_petro.to_csv(output_path, index=False)
    

if __name__ == "__main__":
    main()