

dengue_columns = [
    # Informações de Notificação
    "TP_NOT", "ID_AGRAVO", "DT_NOTIFIC", "SEM_NOT", "NU_ANO", "SG_UF_NOT", "ID_MUNICIP", 
    "ID_REGIONA", "ID_UNIDADE", "DT_SIN_PRI", "SEM_PRI",

    # Informações de Idade
    "ANO_NASC", "NU_IDADE_N", 

    # Dados Demográficos
    "CS_SEXO", "CS_GESTANT", "CS_RACA", "CS_ESCOL_N", "SG_UF", "ID_MN_RESI", "ID_RG_RESI", 
    "ID_PAIS",

    # Informações de Investigação
    "DT_INVEST", "ID_OCUPA_N", 

    # Sintomas
    "FEBRE", "MIALGIA", "CEFALEIA", "EXANTEMA", "VOMITO", "NAUSEA", 
    "DOR_COSTAS", "CONJUNTVIT", "ARTRITE", "ARTRALGIA", "PETEQUIA_N", 
    "LEUCOPENIA", "LACO", "DOR_RETRO", "DIABETES", "HEMATOLOG", "HEPATOPAT", 
    "RENAL", "HIPERTENSA", "ACIDO_PEPT", "AUTO_IMUNE", 

    # Testes e Resultados
    "DT_CHIK_S1", "DT_CHIK_S2", "DT_PRNT", "RES_CHIKS1", "RES_CHIKS2", "RESUL_PRNT", 
    "DT_SORO", "RESUL_SORO", "DT_NS1", "RESUL_NS1", "DT_VIRAL", "RESUL_VI_N", 
    "DT_PCR", "RESUL_PCR_", "SOROTIPO",

    # Histórico e Imunização
    "HISTOPA_N", "IMUNOH_N", 

    # Hospitalização e Internação
    "HOSPITALIZ", "DT_INTERNA", "DT_OBITO",

    # Informações de Localização
    "UF", "MUNICIPIO", "TPAUTOCTO", "COUFINF", "COPAISINF", "COMUNINF", 

    # Classificação e Critérios
    "CLASSI_FIN", "CRITERIO", "DOENCA_TRA", "CLINC_CHIK", "EVOLUCAO", "DT_ENCERRA", 

    # Alarmes e Monitoramento
    "ALRM_HIPOT", "ALRM_PLAQ", "ALRM_VOM", "ALRM_SANG", "ALRM_HEMAT", "ALRM_ABDOM", 
    "ALRM_LETAR", "ALRM_HEPAT", "ALRM_LIQ", "DT_ALRM", 

    # Gravidade e Manejo
    "GRAV_PULSO", "GRAV_CONV", "GRAV_ENCH", "GRAV_INSUF", "GRAV_TAQUI", "GRAV_EXTRE", 
    "GRAV_HIPOT", "GRAV_HEMAT", "GRAV_MELEN", "GRAV_METRO", "GRAV_SANG", "GRAV_AST", 
    "GRAV_MIOC", "GRAV_CONSC", "GRAV_ORGAO", "DT_GRAV", 

    # Complicações e Hemorragias
    "MANI_HEMOR", "EPISTAXE", "GENGIVO", "METRO", "PETEQUIAS", "HEMATURA", "SANGRAM", 

    # Dados Complementares
    "LACO_N", "PLASMATICO", "EVIDENCIA", "PLAQ_MENOR", "CON_FHD", "COMPLICA", "TP_SISTEMA", 
    "NDUPLIC_N", "DT_DIGITA", "CS_FLXRET", "FLXRECEBI", "MIGRADO_W"
]

CITIES_COLUMNS = [
  "ID_MUNICIP",
  "MUNICIPIO",
  "ID_MN_RESI",
  "COMUNINF"
]

DATE_COLUMNS = [
    "DT_NOTIFIC", 
    "DT_SIN_PRI", 
    "DT_INVEST", 
    "DT_CHIK_S1", 
    "DT_CHIK_S2",
    "DT_SORO", 
    "DT_PRNT", 
    "DT_NS1", 
    "DT_VIRAL", 
    "DT_PCR",
    "DT_INTERNA", 
    "DT_OBITO", 
    "DT_ENCERRA"
]

COLUMNS_RENAMED_MAP = {
  "TP_NOT": "Tipo de Notificação",
  "ID_AGRAVO": "Agravo",
  "DT_NOTIFIC": "Data da Notificação", #YYYY-MM-DD
  "SEM_NOT": "Semana Epidemiológica da Notificação", #YYYY-SS
  "NU_ANO": "Ano",
  "SG_UF_NOT": "Estado",
  "ID_MUNICIP": "Município",
  "ID_REGIONA": "Regional de Saúde",
  "ID_UNIDADE": "Hospital",
  "DT_SIN_PRI": "Data dos Primeiros Sintomas", #YYYY-MM-DD
  "SEM_PRI": "Semana Epidemiológica dos Primeiros Sintomas", #YYYY-SS
  "ANO_NASC": "Ano de Nascimento",
  "NU_IDADE_N": "Idade",
  "CS_SEXO": "Sexo",
  "CS_GESTANT": "Gestação",
  "CS_RACA": "Raça",
  "CS_ESCOL_N": "Escolaridade",
  "SG_UF": "Estado de Origem do Paciente",
  "ID_MN_RESI": "Município de Origem do Paciente",
  "ID_PAIS": "País",
  "ID_RG_RESI": "Regional de Saúde de Origem do Paciente",
  "DT_INVEST": "Data da Investigação",
  "ID_OCUPA_N": "Ocupação",
  "FEBRE": "Febre",
  "MIALGIA": "Dor muscular (Mialgia)",
  "CEFALEIA": "Dor de cabeça (Cefaleia)",
  "EXANTEMA": "Manchas na pele (Exantema)",
  "VOMITO": "Vômito",
  "NAUSEA": "Náusea",
  "DOR_COSTAS": "Dor nas costas",
  "CONJUNTVIT": "Conjuntivite",
  "ARTRITE": "Artrite",
  "ARTRALGIA": "Dor nas articulações (Artralgia)",
  "PETEQUIA_N": "Petéquias (manchas vermelhas na pele)",
  "LEUCOPENIA": "Leucopenia (redução de glóbulos brancos)",
  "LACO": "Teste do Laço positivo",
  "DOR_RETRO": "Dor atrás dos olhos (Retro-orbital)",
  "DIABETES": "Diabetes",
  "HEMATOLOG": "Doença hematológica",
  "HEPATOPAT": "Doença no fígado (Hepatopatia)",
  "RENAL": "Doença renal",
  "HIPERTENSA": "Hipertensão",
  "ACIDO_PEPT": "Úlcera péptica",
  "AUTO_IMUNE": "Doença autoimune",
  "DT_CHIK_S1": "Data de Coleta do Exame Sorológico da Chikungunya Soro 1",
  "DT_CHIK_S2": "Data de Coleta do Exame Sorológico da Chikungunya Soro 2",
  "DT_PRNT": "Data do Exame PRNT (Teste de Neutralização por Redução de Placas)",
  "RES_CHIKS1": "Resultado do Exame Sorológico da Chikungunya Soro 1",
  "RES_CHIKS2": "Resultado do Exame Sorológico da Chikungunya Soro 2",
  "RESUL_PRNT": "Resultado do Exame PRNT (Teste de Neutralização por Redução de Placas)",
  "DT_SORO": "Data de Coleta do Exame Sorológico da Dengue",
  "RESUL_SORO": "Resultado do Exame Sorológico da Dengue",
  "DT_NS1": "Data de Coleta do Exame Sorológico de Teste Imunoenzimático (ELISA)",
  "RESUL_NS1": "Resultado do Exame Sorológico de Teste Imunoenzimático (ELISA)",
  "HOSPITALIZ": "Hospitalização",
  "DT_VIRAL": "Data da Coleta do Exame de Isolamento Viral",
  "RESUL_VI_N": "Resultado do Exame de Isolamento Viral",
  "DT_PCR": "Data de Coleta do Exame de Reação em Cadeia da Polimerase com Transcriptase Reversa. (RT_PCR)",
  "RESUL_PCR_": "Resultado do Exame de Reação em Cadeia da Polimerase com Transcriptase Reversa. (RT_PCR)",
  "SOROTIPO": "Sorotipo",
  "HISTOPA_N": "Resultado do Exame de Histopatologia",
  "IMUNOH_N": "Resultado Exame de Imunohistoquímica",
  "DT_INTERNA": "Data de Internação",
  "DT_OBITO": "Data de Óbito",
  "UF": "UF do Hospital",
  "MUNICIPIO": "Município do Hospital",
  "TPAUTOCTO": "Caso Autóctone",
  "COUFINF": "UF Provável da Infecção",
  "COPAISINF": "País Provável da Infecção",
  "COMUNINF": "Município Provável da Infecção",
  "CLASSI_FIN": "Classificação do Caso",
  "CRITERIO": "Critério de Confirmação ou Descarte",
  "DOENCA_TRA": "Doença Relacionada ao Trabalho",
  "EVOLUCAO": "Evolução do Caso",
  "DT_ENCERRA": "Data de Encerramento do Caso",
  "ALRM_HIPOT": "Hipotensão",
  "ALRM_PLAQ": "Queda Abrupta de Plaquetas",
  "ALRM_VOM": "Vômitos Persistentes",
  "ALRM_SANG": "Sangramento de Mucosas ou Outras Hemorragias",
  "ALRM_HEMAT": "Aumento Hematócrito",
  "ALRM_ABDOM": "Dor Abdominal",
  "ALRM_LETAR": "Letargia ou Irritabilidade",
  "ALRM_HEPAT": "Hepatomegalia",
  "ALRM_LIQ": "Acúmulo de Líquidos",
  "DT_ALRM": "Data de Início dos Sintomas",
  "GRAV_PULSO": "Pulso Débil ou Indetectável",
  "GRAV_CONV": "PA Convergente",
  "GRAV_ENCH": "Tempo de Enchimento Capilar",
  "GRAV_INSUF": "Acúmulo de Líquidos com Insuficiência Respiratória",
  "GRAV_TAQUI": "Taquicardia",
  "GRAV_EXTRE": "Extremidades Frias",
  "GRAV_HIPOT": "Hipotensão Arterial em Fase Tardia",
  "GRAV_HEMAT": "Hematêmese",
  "GRAV_MELEN": "Melena",
  "GRAV_METRO": "Metrorragia Volumosa",
  "GRAV_SANG": "Sangramento do SNC",
  "GRAV_AST": "AST/ALT maior que 1000",
  "GRAV_MIOC": "Miocardite",
  "GRAV_CONSC": "Alteração de Consciência",
  "DT_GRAV": "Data de Início dos Sintômas Graves",
  "CS_FLXRET": "Registro Habilitado ou Enviado pelo Fluxo de Retorno para o Município de Residência",
  "FLXRECEBI": "Registro Recebido pelo Fluxo de Retorno"
}

UF_COLUMNS = [
  "SG_UF", 
  "SG_UF_NOT", 
  "UF", 
  "COUFINF"
]

COUNTRY_MAP = { 
  1: "Brasil",
}

UF_MAP = {
  12: "Acre",
  27: "Alagoas",
  13: "Amazonas",
  16: "Amapá",
  29: "Bahia",
  23: "Ceará",
  53: "Distrito Federal",
  32: "Espírito Santo",
  52: "Goiás",
  21: "Maranhão",
  51: "Mato Grosso",
  50: "Mato Grosso do Sul",
  31: "Minas Gerais",
  15: "Pará",
  25: "Paraíba",
  41: "Paraná",
  26: "Pernambuco",
  22: "Piauí",
  33: "Rio de Janeiro",
  24: "Rio Grande do Norte",
  43: "Rio Grande do Sul",
  11: "Rondônia",
  14: "Roraima",
  42: "Santa Catarina",
  35: "São Paulo",
  28: "Sergipe",
  17: "Tocantins"
}

NUMERIC_KEYS_MAP = {
    "RES_CHIKS1": {
      1: "Reagente",
      2: "Não Reagente",
      3: "Inconclusivo",
      4: "Não realizado"
    },
    "RES_CHIKS2": {
      1: "Reagente",
      2: "Não Reagente",
      3: "Inconclusivo",
      4: "Não realizado"
    },
    "RESUL_PRNT": {
      1: "Reagente",
      2: "Não Reagente",
      3: "Inconclusivo",
      4: "Não realizado"
    },
    "RESUL_SORO": {
      1: "Reagente",
      2: "Não Reagente",
      3: "Inconclusivo",
      4: "Não realizado"
    },
    "RESUL_NS1": {
      1: "Reagente",
      2: "Não Reagente",
      3: "Inconclusivo",
      4: "Não realizado"
    },
    "RESUL_VI_N": {
      1: "Reagente",
      2: "Não Reagente",
      3: "Inconclusivo",
      4: "Não realizado"
    },
    "RESUL_PCR_": {
      1: "Reagente",
      2: "Não Reagente",
      3: "Inconclusivo",
      4: "Não realizado"
    },
    "SOROTIPO": {
      1: "Dengue 1",
      2: "Dengue 2",
      3: "Dengue 3",
      4: "Dengue 4"
    },
    "HISTOPA_N": {
      1: "Reagente",
      2: "Não Reagente",
      3: "Inconclusivo",
      4: "Não realizado"
    },
    "IMUNOH_N": {
      1: "Reagente",
      2: "Não Reagente",
      3: "Inconclusivo",
      4: "Não realizado"
    },
    "TPAUTOCTO": {
      1: "Sim",
      2: "Não",
      3: "Indeterminado"
    },
    "CLASSI_FIN": {
      5: "Descartado",
      10: "Dengue",
      11: "Dengue com sinais de alarme",
      12: "Dengue grave",
      13: "Chikungunya"
    },
    "CRITERIO": {
      1: "Laboratório",
      2: "Clínico Epidemiológico",
      3: "Em investigação"
    },
    "DOENCA_TRA": {
      1: "Sim",
      2: "Não",
      9: "Ignorado"
    },
    "EVOLUCAO": {
      1: "Cura",
      2: "Óbito pelo agravo",
      3: "Óbito por outras causas",
      4: "Óbito em investigação",
      9: "Ignorado"
    },
    "CS_FLXRET": {
      0: "Não",
      1: "Habilitado para Envio",
      2: "Enviado"
    },
    "HOSPITALIZ": {
      1: "Sim", 
      2: "Não",
      0: "Ignorado"
    },
    "CS_ESCOL_N": {
      1: "1ª à 4ª série incompleta (Ensino Fundamental)", 
      2: "4ª série completa (Ensino Fundamental)", 
      3: "5ª à 8ª série incompleta (Ensino Fundamental)", 
      4: "Ensino Fundamental Completo", 
      5: "Ensino Médio incompleto", 
      6: "Ensino Médio completo", 
      7: "Educação Superior incompleta", 
      8: "Educação Superior completa", 
      9: "Ignorado", 
      10: "Não se aplica", 
      43: "Analfabeto"
    },
    "CS_RACA": {
      1: "Branca", 
      2: "Preta", 
      3: "Amarela", 
      4: "Parda", 
      5: "Indígena",
      9: "Ignorado"
    },
    "CS_GESTANT": {
      1: "1º trimestre", 
      2: "2º trimestre", 
      3: "3º trimestre", 
      4: "Idade gestacional ignorada", 
      5: "Não", 
      6: "Não se aplica", 
      9: "Ignorado"
    },
    "TP_NOT": {
      1: "Negativa",
      2: "Individual",
      3: "Surto",
      4: "Agregado"
    },
    "FEBRE": {
      1: "Sim", 
      2: "Não"
    },
    "MIALGIA": {
      1: "Sim", 
      2: "Não"
    },
    "CEFALEIA": {
      1: "Sim", 
      2: "Não"
    },
    "EXANTEMA": {
      1: "Sim", 
      2: "Não"
    },
    "VOMITO": {
      1: "Sim", 
      2: "Não"
    },
    "NAUSEA": {
      1: "Sim", 
      2: "Não"
    },
    "DOR_COSTAS": {
      1: "Sim", 
      2: "Não"
    },
    "CONJUNTVIT": {
      1: "Sim", 
      2: "Não"
    },
    "ARTRITE": {
      1: "Sim", 
      2: "Não"
    },
    "ARTRALGIA": {
      1: "Sim", 
      2: "Não"
    },
    "PETEQUIA_N": {
      1: "Sim", 
      2: "Não"
    },
    "LEUCOPENIA": {
      1: "Sim", 
      2: "Não"
    },
    "LACO": {
      1: "Sim", 
      2: "Não"
    },
    "DOR_RETRO": {
      1: "Sim", 
      2: "Não"
    },
    "DIABETES": {
      1: "Sim", 
      2: "Não"
    },
    "HEMATOLOG": {
      1: "Sim", 
      2: "Não"
    },
    "HEPATOPAT": {
      1: "Sim", 
      2: "Não"
    },
    "RENAL": {
      1: "Sim", 
      2: "Não"
    },
    "HIPERTENSA": {
      1: "Sim", 
      2: "Não"
    },
    "ACIDO_PEPT": {
      1: "Sim", 
      2: "Não"
    },
    "AUTO_IMUNE": {
      1: "Sim", 
      2: "Não"}  
      
}

TEXT_KEYS_MAP = {
  "CS_SEXO": {
    "M": "Masculino", 
    "F": "Feminino"
  },
  "ID_AGRAVO": {
    "A90": "Dengue", 
    "Z209": "Acidente com Material Biológico", 
    "Y96": "Acidente de Trabalho",
    "B24": "HIV/AIDS",
    "X29": "Acidente por Animais Peçonhentos"
  },
}

WEEK_MAP = {
  "01": "Semana 1",
  "02": "Semana 2",
  "03": "Semana 3",
  "04": "Semana 4",
  "05": "Semana 5",
  "06": "Semana 6",
  "07": "Semana 7",
  "08": "Semana 8",
  "09": "Semana 9",
  "10": "Semana 10",
  "11": "Semana 11",
  "12": "Semana 12",
  "13": "Semana 13",
  "14": "Semana 14",
  "15": "Semana 15",
  "16": "Semana 16",
  "17": "Semana 17",
  "18": "Semana 18",
  "19": "Semana 19",
  "20": "Semana 20",
  "21": "Semana 21",
  "22": "Semana 22",
  "23": "Semana 23",
  "24": "Semana 24",
  "25": "Semana 25",
  "26": "Semana 26",
  "27": "Semana 27",
  "28": "Semana 28",
  "29": "Semana 29",
  "30": "Semana 30",
  "31": "Semana 31",
  "32": "Semana 32",
  "33": "Semana 33",
  "34": "Semana 34",
  "35": "Semana 35",
  "36": "Semana 36",
  "37": "Semana 37",
  "38": "Semana 38",
  "39": "Semana 39",
  "40": "Semana 40",
  "41": "Semana 41",
  "42": "Semana 42",
  "43": "Semana 43",
  "44": "Semana 44",
  "45": "Semana 45",
  "46": "Semana 46",
  "47": "Semana 47",
  "48": "Semana 48",
  "49": "Semana 49",
  "50": "Semana 50",
  "51": "Semana 51",
  "52": "Semana 52"
}

NU_IDADE_MAP = {
  4000: 0,
  4001: 1,
  4002: 2,
  4003: 3,
  4004: 4,
  4005: 5,
  4006: 6,
  4007: 7,
  4008: 8,
  4009: 9,
  4010: 10,
  4011: 11,
  4012: 12,
  4013: 13,
  4014: 14,
  4015: 15,
  4016: 16,
  4017: 17,
  4018: 18,
  4019: 19,
  4020: 20,
  4021: 21,
  4022: 22,
  4023: 23,
  4024: 24,
  4025: 25,
  4026: 26,
  4027: 27,
  4028: 28,
  4029: 29,
  4030: 30,
  4031: 31,
  4032: 32,
  4033: 33,
  4034: 34,
  4035: 35,
  4036: 36,
  4037: 37,
  4038: 38,
  4039: 39,
  4040: 40,
  4041: 41,
  4042: 42,
  4043: 43,
  4044: 44,
  4045: 45,
  4046: 46,
  4047: 47,
  4048: 48,
  4049: 49,
  4050: 50,
  4051: 51,
  4052: 52,
  4053: 53,
  4054: 54,
  4055: 55,
  4056: 56,
  4057: 57,
  4058: 58,
  4059: 59,
  4060: 60,
  4061: 61,
  4062: 62,
  4063: 63,
  4064: 64,
  4065: 65,
  4066: 66,
  4067: 67,
  4068: 68,
  4069: 69,
  4070: 70,
  4071: 71,
  4072: 72,
  4073: 73,
  4074: 74,
  4075: 75,
  4076: 76,
  4077: 77,
  4078: 78,
  4079: 79,
  4080: 80,
  4081: 81,
  4082: 82,
  4083: 83,
  4084: 84,
  4085: 85,
  4086: 86,
  4087: 87,
  4088: 88,
  4089: 89,
  4090: 90,
  4091: 91,
  4092: 92,
  4093: 93,
  4094: 94,
  4095: 95,
  4096: 96,
  4097: 97,
  4098: 98,
  4099: 99,
  4100: 100,
}