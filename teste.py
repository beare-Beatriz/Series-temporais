import pandas as pd
import matplotlib.pyplot as plt

caminho_csv = r'tab.csv'
df = pd.read_csv(caminho_csv, sep=";")
print("Nomes das colunas no CSV:", df.columns)

coluna_temperatura = "temperatura"  
coluna_hora = "hora" 

# Verificar os valores únicos na coluna 'hora'
print("Valores únicos na coluna 'hora':", df[coluna_hora].unique())

# Converter a coluna 'hora' para inteiro, caso esteja como string
df["hora"] = pd.to_numeric(df["hora"], errors="coerce")

# Ordenar os dados pela hora
df = df.sort_values(by="hora")

# Criar uma coluna para identificar o dia com base na posição dos dados
# Como a ordenação foi feita por hora, cada bloco de 24 registros será um dia
df["dia"] = (df.index // 24) + 1  # A cada 24 registros (horas) incrementamos um dia

# Verificar os dias identificados
print("Dias identificados:", df["dia"].unique())

# Calcular a média de temperatura por dia
media_temperatura_por_dia = df.groupby("dia")[coluna_temperatura].mean()

# Verificar a média de temperatura por dia
print("Média de temperatura por dia:")
print(media_temperatura_por_dia)

# Gerar o gráfico
plt.figure(figsize=(10, 6))
ax = media_temperatura_por_dia.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Média de Temperatura por Dia", fontsize=16)
plt.xlabel("Dia", fontsize=14)
plt.ylabel("Temperatura Média (°C)", fontsize=14)
plt.xticks(rotation=0)

# Adicionar a grade (grid)
ax.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()

# Exibir o gráfico
plt.show()
