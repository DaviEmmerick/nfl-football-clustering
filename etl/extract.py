import nfl_data_py as nfl
import pandas as pd
import os

anos = range(2022, 2025)

df_stats = nfl.import_seasonal_data(anos)
df_roster = nfl.import_seasonal_rosters(anos)

cols_roster = ['player_id', 'season', 'player_name', 'position']
cols_existentes_roster = [c for c in cols_roster if c in df_roster.columns]
df_roster_clean = df_roster[cols_existentes_roster].drop_duplicates(subset=['player_id', 'season'])

df_completo = pd.merge(df_stats, df_roster_clean, on=['player_id', 'season'], how='left')

cols_to_keep = [
    'player_id', 'player_name', 'position', 'season', 'age', 
    'completions', 'attempts', 'passing_yards', 'passing_tds', 'interceptions',
    'carries', 'rushing_yards', 'rushing_tds',
    'receptions', 'targets', 'receiving_yards', 'receiving_tds',
    'fantasy_points', 'fantasy_points_ppr',
    'tgt_sh', 'ay_sh', 'wopr_y', 'dom'
]

cols_existentes = [c for c in cols_to_keep if c in df_completo.columns]
df_clean = df_completo[cols_existentes].copy()

if 'player_name' in df_clean.columns:
    df_clean['player_name'] = df_clean['player_name'].fillna('Unknown')
if 'position' in df_clean.columns:
    df_clean['position'] = df_clean['position'].fillna('Unknown')

os.makedirs('database/processed', exist_ok=True)
df_clean.to_csv("database/processed/processed.csv", index=False)

print("Arquivo salvo em database/processed/processed.csv")