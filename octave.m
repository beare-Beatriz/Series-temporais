% Caminho para o arquivo CSV
caminho_csv = "tabela_temperatura_castanhal_17-01-2025.csv";

% Abrir o arquivo para leitura
fid = fopen(caminho_csv, "r");

% Ler o cabeçalho
header = fgetl(fid); % Ignorar a primeira linha (cabeçalho)
disp(["Cabeçalho do CSV: ", header]);

% Ler os dados numéricos, ignorando valores nulos
dados = textscan(fid, "%f %f", "Delimiter", ";", "EmptyValue", NaN);
fclose(fid);

% Separar as colunas
Hora = dados{1};           % Primeira coluna (Hora)
Temperatura = dados{2};    % Segunda coluna (Temp)

% Remover valores nulos
idx_validos = ~isnan(Temperatura);
Hora_validas = Hora(idx_validos);
Temperatura_validas = Temperatura(idx_validos);

% Normalizar a escala da Hora (se necessário)
Hora_norm = Hora_validas - min(Hora_validas);

% Regressão linear
X = [ones(length(Hora_norm), 1), Hora_norm]; % Adicionar o termo de intercepto
theta = (X' * X) \ (X' * Temperatura_validas); % Calcular os coeficientes (regressão normal)

% Previsões para as horas faltantes
Hora_faltantes = [1900; 2000; 2100; 2200; 2300];
Hora_faltantes_norm = Hora_faltantes - min(Hora_validas); % Normalizar as horas faltantes
X_faltantes = [ones(length(Hora_faltantes_norm), 1), Hora_faltantes_norm];
previsoes = X_faltantes * theta;

% Exibir a equação da regressão e previsões
printf("Equação da Regressão: y = %.2fx + %.2f\n", theta(2), theta(1));
disp("Previsões para 1900-2300:");
disp(previsoes);

% Criar linha de regressão para todas as horas
Hora_range = linspace(min(Hora_validas), max(Hora_validas), 100)'; % Gera 100 pontos no intervalo de Hora
Hora_range_norm = Hora_range - min(Hora_validas); % Normalizar a escala
X_range = [ones(length(Hora_range_norm), 1), Hora_range_norm];
Temperatura_range = X_range * theta;

% Plotar os resultados
figure; % Abrir uma nova janela de figura
scatter(Hora_validas, Temperatura_validas, "b", "filled"); hold on; % Dados reais
plot(Hora_range, Temperatura_range, "r", "LineWidth", 2); % Linha de regressão
scatter(Hora_faltantes, previsoes, "g", "filled"); % Previsões
xlabel("Hora (UTC)");
ylabel("Temp. Máx. (°C)");
legend("Dados Reais", "Linha de Regressão", "Previsões");
grid on;
title("Regressão Linear - Temperatura por Hora");
hold off;

% Exibir o gráfico explicitamente
drawnow;
