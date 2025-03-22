from maps.value_maps import value_mappings, uf_map, cities_map, tp_not_map, id_unidade_map, country_map, columns_renamed_map


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
            df[col] = df[col].map(mapping)

    df["SG_UF_NOT"] = df["SG_UF_NOT"].map(uf_map).fillna("Desconhecido")
    df["ID_MUNICIP"] = df["ID_MUNICIP"].map(cities_map).fillna("Desconhecido")
    df["ID_MN_RESI"] = df["ID_MN_RESI"].map(cities_map).fillna("Desconhecido")
    df["TP_NOT"] = df["TP_NOT"].map(tp_not_map).fillna("Desconhecido")
    df["ID_UNIDADE"] = df["ID_UNIDADE"].map(id_unidade_map).fillna("Desconhecido")
    df["SG_UF"] = df["SG_UF"].map(uf_map).fillna("Desconhecido")
    df["ID_PAIS"] = df["ID_PAIS"].map(country_map).fillna("Desconhecido")
    
    df.rename(columns=columns_renamed_map, inplace=True)
    

    return df