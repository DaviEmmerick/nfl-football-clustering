import pandas as pd

df = pd.read_csv("database/processed/processed.csv")
print("As colunas que existem são:")
print(list(df.columns))
#print(df.head(5))

pos_irrelevantes = ['OL', 'G', 'C', 'T', 'OT', 'P', 'LS']

df_clean = df[~df['position'].isin(pos_irrelevantes)].copy()

colunas_modelo = [
    'player_name', 'position', 'season', 'age', 
    'fantasy_points_ppr', 
    'passing_yards', 'passing_tds', 'interceptions',
    'rushing_yards', 'rushing_tds', 
    'receptions', 'targets', 'receiving_yards', 'receiving_tds',
    'sacks', 'sack_yards', 
    'tgt_sh', 'ay_sh', 'wopr_y', 'dom' # advanced stats
]

cols_existentes = [c for c in colunas_modelo if c in df_clean.columns]

df_final = df_clean[cols_existentes].copy()

df_final = df_final.fillna(0)

df_final.to_csv("database/processed/modelo_ready.csv")
print("✅ Transformação concluída com sucesso!")