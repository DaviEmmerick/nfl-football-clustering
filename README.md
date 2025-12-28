# 🏈 NFL Player Clustering & Fantasy Tiers

## 📄 Sobre o Projeto
Este projeto utiliza técnicas de Aprendizado de Máquina Não Supervisionado (Unsupervised Learning) para segmentar jogadores da NFL em "tiers" (níveis) de performance.

O objetivo é apoiar a tomada de decisão no Fantasy Football, identificando matematicamente quais jogadores pertencem à elite, quais são titulares sólidos e quais são apostas de risco, eliminando o viés subjetivo das análises manuais.

## 🎯 Objetivos

Agrupar jogadores com características estatísticas similares usando o algoritmo K-Means.

Determinar o número ideal de tiers para cada posição (QB, RB, WR, TE) usando métodos matemáticos (Cotovelo e Silhueta).

Visualizar a distribuição dos jogadores da temporada atual em comparação com dados históricos.

## 🛠️ Tecnologias e Metodologia

#### Tech Stack

Linguagem: Python

Manipulação de Dados: Pandas, NumPy

Machine Learning: Scikit-learn (KMeans, StandardScaler, Silhouette Score)

Visualização: Matplotlib, Seaborn

#### Workflow do Modelo

Coleta e Filtragem: Seleção de dados históricos e atuais, aplicando filtros de relevância (ex: QBs com > 500 jardas, RBs com > 50 pontos Fantasy) para eliminar ruído.

Feature Selection: Definição de métricas chave por posição:

QB: Passing Yards, Passing TDs, Rushing Yards, Interceptions, Fantasy Points.

RB/WR/TE: Envolvimento no jogo (Target Share), Produção (Yards, TDs) e Eficiência.

Pré-processamento: Tratamento de valores nulos e Padronização com StandardScaler para garantir que métricas com escalas diferentes (ex: 4000 jardas vs 30 TDs) tenham o mesmo peso no cálculo de distância.

Determinação do K (Clusters): Análise do Elbow Method (Método do Cotovelo) combinada com conhecimento de domínio para definir o número ideal de grupos.

Clusterização: Aplicação do K-Means e rotulagem dos dados.

## 📊 Resultados e Visualização

1. Definição do Número de Clusters 

![Elbow Method](nfl-football-clustering/results\output-cotovelokmeans.png)

Utilizei a inércia (WCSS) para identificar o ponto de inflexão onde adicionar mais clusters deixa de trazer ganho significativo de melhoria

2. Análise de Tiers (Scatter Plot)

![Elbow Method](nfl-football-clustering/results\output-graphkmeans.png)

## 🚀 Como Executar

1. Clone o repositório e instale as dependências:

```
git clone https://github.com/seu-usuario/nfl-football-clustering.git
cd nfl-football-clustering
pip install -r requirements.txt
```

2. Use-case

```
df_rb = rodar_kmeans_historico(df, 'RB', config_pos['RB'], n_clusters=4)
```

## Próximos Passos

- Implementar PCA (Principal Component Analysis) para visualização 2D mais precisa de dados multidimensionais.

- Criar uma análise detalhada dos centróides para nomear automaticamente os tiers (ex: "Elite", "Boom/Bust").