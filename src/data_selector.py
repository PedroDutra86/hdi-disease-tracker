from maps.value_maps import dengue_columns

def select_data(df):

  missing_columns = [col for col in dengue_columns if col not in df.columns]
  if missing_columns:
    print(f"Atenção: as seguintes colunas estão faltando no DataFrame: {missing_columns}")

  df = df[dengue_columns]
  return df