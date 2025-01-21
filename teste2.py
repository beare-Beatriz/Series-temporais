import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

caminho_csv = r'tab.csv'
df = pd.read_csv(caminho_csv, sep=";")

coluna_temperatura = "temperatura"
coluna_hora = "hora"


df = df.sort_values(by="hora")

df['dia'] = (df.index // 24) + 1


media_temperatura_por_dia = df.groupby('dia')[coluna_temperatura].mean()


dias = media_temperatura_por_dia.index.values.reshape(-1, 1)
temperaturas = media_temperatura_por_dia.values

# Treinar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(dias, temperaturas)


dias_futuros = np.array([16, 17, 18]).reshape(-1, 1)
previsoes_temperatura = modelo.predict(dias_futuros)


plt.scatter(dias, temperaturas, color='blue', label='Médias Diárias')
plt.plot(dias, modelo.predict(dias), color='red', label='Linha de Regressão')
plt.xticks(ticks=np.arange(1, 19, 1))
plt.scatter(dias_futuros, previsoes_temperatura, color='green', label='Previsões (Dias 16-18)', marker='o')
plt.xlabel("Dia")
plt.ylabel("Temperatura Média (°C)")
plt.title("Regressão Linear da Temperatura Média por Dia")
plt.legend()
plt.grid(linestyle="--", alpha=0.9)
plt.tight_layout()
plt.show()

#equação
print(f"Equação da Regressão: y = {modelo.coef_[0]:.2f}x + {modelo.intercept_:.2f}")
# previsões
for dia, temp in zip(dias_futuros.flatten(), previsoes_temperatura):
    print(f"Previsão para o dia {dia}: Temperatura média = {temp:.2f}°C")
#médias
print("Média de temperatura por dia:")
print(media_temperatura_por_dia)