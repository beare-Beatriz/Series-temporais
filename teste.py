import pandas as pd
import matplotlib.pyplot as plt

caminho_csv = r'tab.csv'
df = pd.read_csv(caminho_csv, sep=";")
print("Nomes das colunas no CSV:", df.columns)

coluna_temperatura = "temperatura"  
coluna_hora = "hora" 

df = df.sort_values(by="hora")

df["dia"] = (df.index // 24) + 1  # A cada 24 registros (horas) incrementamos um dia

media_temperatura_por_dia = df.groupby("dia")[coluna_temperatura].mean() 
print("Média de temperatura por dia:")
print(media_temperatura_por_dia)


plt.figure(figsize=(10, 6))
ax = media_temperatura_por_dia.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Média de Temperatura por Dia", fontsize=16)
plt.xlabel("Dia", fontsize=14)
plt.ylabel("Temperatura Média (°C)", fontsize=14)
plt.xticks(rotation=0)
ax.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
