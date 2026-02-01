import pandas as pd
from sqlalchemy import create_engine

pg_engine = create_engine(
    'postgresql+psycopg2://postgres:test@localhost:5432/hell'
)
df_taxpayer = pd.read_excel(r'F:\smapledata\test.xlsx')

df_taxpayer.to_sql('Taxpayer',pg_engine, if_exists='replace', index=False)
print("Data inserted successfully into Taxpayer_detail table")

