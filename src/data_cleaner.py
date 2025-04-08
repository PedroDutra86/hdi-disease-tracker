from maps.value_maps import UF_MAP, COUNTRY_MAP, COLUMNS_RENAMED_MAP, NUMERIC_KEYS_MAP, TEXT_KEYS_MAP, WEEK_MAP, NU_IDADE_MAP, DATE_COLUMNS, CITIES_COLUMNS, UF_COLUMNS
from maps.municipes_cnes_map import CITIES_MAP, ID_UNIDADE_MAP

import pandas as pd

"""
Limpa os dados de acordo com as regras definidas.

Args:
    df (pd.DataFrame): DataFrame com os dados carregados.

Returns:
    pd.DataFrame: DataFrame com os dados limpos.
"""


def apply_mapping(df, column, mapping=None, fill_value="Desconhecido", to_numeric=False, dtype=None, to_datetime=False):
    if column not in df.columns:
        return

    if to_numeric:
        df[column] = pd.to_numeric(df[column], errors="coerce")
        if dtype:
            df[column] = df[column].astype(dtype)

    if mapping is not None:
        df[column] = df[column].map(mapping).fillna(fill_value)

    if to_datetime:
        df[column] = pd.to_datetime(df[column], format="%Y%m%d", errors="coerce")
        df[column] = df[column].dt.date


def clean_data(df):
    # Fatiando colunas de Semana
    df["SEM_PRI"] = df["SEM_PRI"].str[4:] 
    df["SEM_NOT"] = df["SEM_NOT"].str[4:] 

    apply_mapping(df, "ID_UNIDADE", ID_UNIDADE_MAP, to_numeric=True, dtype="Int64")
    apply_mapping(df, "ID_PAIS", COUNTRY_MAP, to_numeric=True, dtype="Int64")
    apply_mapping(df, "COPAISINF", COUNTRY_MAP, to_numeric=True, dtype="Int64")
    apply_mapping(df, "NU_IDADE_N", NU_IDADE_MAP, fill_value=0, to_numeric=True, dtype="Int64")

    apply_mapping(df, "SEM_NOT", WEEK_MAP)
    apply_mapping(df, "SEM_PRI", WEEK_MAP)

    for col, mapping in NUMERIC_KEYS_MAP.items():
        apply_mapping(df, col, mapping, fill_value = "Ignorado", to_numeric=True, dtype="Int64")
    for col, mapping in TEXT_KEYS_MAP.items():
        apply_mapping(df, col, mapping, fill_value = "Ignorado")
    for col in DATE_COLUMNS:
        apply_mapping(df, col, to_datetime=True)
    for col in CITIES_COLUMNS:
        apply_mapping(df, col, CITIES_MAP, to_numeric=True, dtype="Int64")
    for col in UF_COLUMNS:
        apply_mapping(df, col, UF_MAP, to_numeric=True, dtype="Int64")

    df.rename(columns=COLUMNS_RENAMED_MAP, inplace=True)


    # Coerções
    df["Idade"] = df["Idade"].astype("Int64")
    df["Ano"] = df["Ano"].astype("Int64")
    df["Ano de Nascimento"] = df["Ano de Nascimento"].astype("Int64")

    return df
