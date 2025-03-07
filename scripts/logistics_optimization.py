import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados processados
df = pd.read_excel("data/processed_data/Meganium_Sales_data.xlsx")

# Agrupar vendas por país e plataforma
logistics_analysis = df.groupby(["delivery_country", "Platform"])["quantity"].sum().unstack().fillna(0)

# Criar gráfico de barras empilhadas
logistics_analysis.plot(kind="bar", stacked=True, figsize=(10, 6), colormap="viridis")
plt.xlabel("País")
plt.ylabel("Quantidade Vendida")
plt.title("Distribuição de Vendas por Plataforma e País")
plt.legend(title="Plataforma")
plt.xticks(rotation=45)
plt.savefig("insights/logistics_analysis.png")
plt.show()

print("Gráfico de análise logística salvo em insights/logistics_analysis.png")
