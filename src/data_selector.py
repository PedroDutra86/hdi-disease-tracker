from src.maps.value_maps import important_columns

def select_data(df):

  missing_columns = [col for col in important_columns if col not in df.columns]
  if missing_columns:
    print(f"Atenção: as seguintes colunas estão faltando no DataFrame: {missing_columns}")

  df = df[important_columns]
  return df