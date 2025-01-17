import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

caminho_csv = r"tabela_temperatura_castanhal_17-01-2025.csv"
df = pd.read_csv(caminho_csv, sep=";")
print("Nomes das colunas no CSV:", df.columns)

coluna_temperatura = "Temp"  
coluna_hora = "Hora" 

# Remover valores nulos
df = df.dropna(subset=[coluna_temperatura])

# Extrair as colunas
Hora = df[coluna_hora].values.reshape(-1, 1)
Temperatura = df[coluna_temperatura].values

# Criar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(Hora, Temperatura)

# Previsão para as horas faltantes (1900, 2000, 2100, 2200, 2300)
Hora_faltantes = np.array([1900, 2000, 2100, 2200, 2300]).reshape(-1, 1)
previsoes = modelo.predict(Hora_faltantes)
print(f"Equação da Regressão: y = {modelo.coef_[0]:.2f}x + {modelo.intercept_:.2f}")
print(f"Previsões para 1900-2300: {previsoes}")

plt.scatter(Hora, Temperatura, color='blue', label='Dados Reais')
plt.plot(Hora, modelo.predict(Hora), color='red', label='Linha de Regressão')
plt.scatter(Hora_faltantes, previsoes, color='green', label='Previsões')
plt.xlabel("Hora (UTC)")
plt.ylabel("Temp. Máx. (°C)")
plt.legend()
plt.show()
