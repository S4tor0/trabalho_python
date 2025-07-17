import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#criação do dataframe
df = pd.read_csv('https://raw.githubusercontent.com/S4tor0/trabalho_python/refs/heads/main/avg_rainfalltemp%20in%20UK%20-%20Sheet1.csv')
df
# informacoes basicas do df
df.info()

#criacao de um grafico de dispercao da relacao da temperatura em centigrados com a media de chuva em milimetros
plt.scatter(df['Avg temp(in centigrade)'], df['Avg rainfall(in mm)'])
plt.style.use('ggplot')
plt.title('Relação de temperatura para chuva')
plt.xlabel('Media de Temperatura(°c)')
plt.ylabel('Media de Chuva(mm)')
plt.show()

#vizualizar os tipos de periodos do ano
df['Type of period'].value_counts()

#dicionario para armazenar as cores para cada tipo de periodo do ano
color_mapping = {
    "Monthly":'Blue',
    "Season":'Orange',
    "Calendar Year":'Red'
}

colors = [color_mapping[tipo] for tipo in df['Type of period']]
#fazendo o grafico ficar separado por cores para cada periodo do ano
plt.scatter(df['Avg temp(in centigrade)'], df['Avg rainfall(in mm)'],color=colors)
plt.style.use('ggplot')
plt.title('Relação de temperatura para chuva')
plt.xlabel('Media de Temperatura(°c)')
plt.ylabel('Media de Chuva(mm)')
plt.show()

#separar informacoes do inverno
filtro = df['Period'] == 'Winter'
inverno = df[filtro]
inverno

#gerando o grafico
plt.bar(inverno['Year'],inverno['Avg temp(in centigrade)'].round(),color='Blue')

#mostrar todos os anos
plt.xticks(inverno['Year'])

#criando os rotulos
plt.title('Media de temperatura no inverno aos anos')
plt.xlabel('Anos')
plt.ylabel('Temperatura media(°c)')

plt.grid(axis='y')
plt.show()

# histograma da media de chuvas de todo DataSet
df['Period'].value_counts()

# Criar o gráfico
plt.figure(figsize=(12, 8))

unicos = df['Period'].unique()

# Cores personalizadas para cada período
cores = plt.cm.viridis(range(0, 256, 256 // len(unicos)))

for i, period in enumerate(unicos):
  filtro = df[df['Period'] == period]['Avg rainfall(in mm)']
  plt.hist(filtro, bins=5, alpha=0.6, label=period, color=cores[i], edgecolor='black')

# Adicionar a legenda
plt.legend(title='Período', title_fontsize='13', fontsize='11', loc='upper right', frameon=True)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Configurações do gráfico
plt.title('Precipitação de chuva por Período', fontsize=16)
plt.xlabel('Precipitação(mm)', fontsize=14)
plt.ylabel('Frequência', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
