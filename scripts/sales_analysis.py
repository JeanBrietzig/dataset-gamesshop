import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados processados
df = pd.read_excel("data/processed_data/Meganium_Sales_data.xlsx")

# Analisar vendas por plataforma
sales_by_platform = df.groupby("Platform")["quantity"].sum()

# Gráfico de vendas por plataforma
sales_by_platform.plot(kind="bar", color=["blue", "green", "red"])
plt.xlabel("Plataforma")
plt.ylabel("Total Vendido")
plt.title("Vendas Totais por Plataforma")
plt.xticks(rotation=0)
plt.savefig("insights/sales_by_platform.png")
plt.show()

print("Gráfico de vendas por plataforma salvo em insights/sales_by_platform.png")
