# **ChatGPT Prompts - Análise de Vendas Meganium**  

## 📌 **1. Consolidação de Dados**  
### 🔹 **Pergunta:**  
*"Combine os arquivos de vendas de AliExpress, Etsy e Shopee em um único dataframe."*  
### 🔹 **Código gerado:**  
```python
import pandas as pd

# Carregar arquivos
ali_df = pd.read_csv("Meganium_Sales_Data_-_AliExpress.csv")
etsy_df = pd.read_csv("Meganium_Sales_Data_-_Etsy.csv")
shopee_df = pd.read_csv("Meganium_Sales_Data_-_Shopee.csv")

# Adicionar coluna indicando a plataforma
ali_df["Platform"] = "AliExpress"
etsy_df["Platform"] = "Etsy"
shopee_df["Platform"] = "Shopee"

# Unir os dataframes
consolidated_df = pd.concat([ali_df, etsy_df, shopee_df], ignore_index=True)
```

---

## 📌 **2. Identificação de Produtos Populares**  
### 🔹 **Pergunta:**  
*"Quais são os produtos mais vendidos em cada país?"*  
### 🔹 **Código gerado:**  
```python
top_products = consolidated_df.groupby(["delivery_country", "product_name"])["quantity"].sum().reset_index()
top_products = top_products.sort_values(["delivery_country", "quantity"], ascending=[True, False])
```

---

## 📌 **3. Otimização Logística**  
### 🔹 **Pergunta:**  
*"Como otimizar o transporte e a logística até o momento da venda?"*  
### 🔹 **Código gerado:**  
```python
logistics_analysis = consolidated_df.groupby(["delivery_country", "Platform"])["quantity"].sum().unstack().fillna(0)
logistics_analysis_percent = logistics_analysis.div(logistics_analysis.sum(axis=1), axis=0) * 100
logistics_summary = pd.concat([logistics_analysis, logistics_analysis_percent], axis=1, keys=["Total Sold", "Percentage"])
```

---

## 📌 **4. Visualização de Dados**  
### 🔹 **Pergunta:**  
*"Gere um gráfico de vendas por plataforma e país."*  
### 🔹 **Código gerado:**  
```python
import matplotlib.pyplot as plt

logistics_analysis.plot(kind="bar", stacked=True, figsize=(10, 6), colormap="viridis")
plt.xlabel("País")
plt.ylabel("Quantidade Vendida")
plt.title("Distribuição de Vendas por Plataforma e País")
plt.legend(title="Plataforma")
plt.xticks(rotation=45)
plt.show()
```
