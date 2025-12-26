import nfl_data_py as nfl

anos_selecionados = range(2022, 2025)

df = nfl.import_seasonal_data(anos_selecionados)
df.to_csv("database/processed/processed.csv")