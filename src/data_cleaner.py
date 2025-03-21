from src.maps.value_maps import value_mappings, uf_map, cities_map, tp_not_map, id_unidade_map


def clean_data(df):
    """
    Limpa os dados de acordo com as regras definidas.
    
    Args:
        df (pd.DataFrame): DataFrame com os dados carregados.
    
    Returns:
        pd.DataFrame: DataFrame com os dados limpos.
    """

    # Aplicar mapeamento às colunas
    for col, mapping in value_mappings.items():
        if col in df.columns:
            df[col] = df[col].map(mapping).fillna("Desconhecido")
    
    df["SG_UF_NOT"] = df["SG_UF_NOT"].map(uf_map).fillna("Desconhecido")
    df["ID_MUNICIP"] = df["ID_MUNICIP"].map(cities_map).fillna("Desconhecido")
    df["TP_NOT"] = df["TP_NOT"].map(tp_not_map).fillna("Desconhecido")
    df["ID_UNIDADE"] = df["ID_UNIDADE"].map(id_unidade_map).fillna("Desconhecido")

    return df