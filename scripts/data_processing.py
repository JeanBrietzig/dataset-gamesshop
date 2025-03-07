import pandas as pd
import os

# Diretório dos arquivos brutos
raw_data_path = "data/raw_data"

# Lista de arquivos CSV
files = ["Meganium_Sales_Data_-_AliExpress.csv", 
         "Meganium_Sales_Data_-_Etsy.csv", 
         "Meganium_Sales_Data_-_Shopee.csv"]

# Lista para armazenar os DataFrames
dfs = []

# Carregar e unificar os arquivos
for file in files:
    df = pd.read_csv(os.path.join(raw_data_path, file))
    df["Platform"] = file.split("_")[-1].replace(".csv", "")  # Adiciona a origem dos dados
    dfs.append(df)

# Concatenar todos os dados em um único DataFrame
consolidated_df = pd.concat(dfs, ignore_index=True)

# Remover valores nulos e duplicados
consolidated_df.dropna(inplace=True)
consolidated_df.drop_duplicates(inplace=True)

# Salvar os dados processados
processed_data_path = "data/processed_data/Meganium_Sales_data.xlsx"
consolidated_df.to_excel(processed_data_path, index=False)

print(f"Dados processados e salvos em {processed_data_path}")
