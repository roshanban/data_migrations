import pandas as pd
import os

total_df = []
csv_folder = r'F:\smapledata\panda\to_load'

for csv_file in os.listdir(csv_folder):
    if csv_file.endswith(".csv"):
        csv_path = os.path.join(csv_folder, csv_file)
        df = pd.read_csv(csv_path)
        file_date = csv_file.replace(".csv", "")
        df["file_date"] = pd.to_datetime(file_date)
        total_df.append(df)

final_df = pd.concat(total_df, ignore_index=False)
print(final_df.sample(50))

# now this csv file dump into sql 
from sqlalchemy import create_engine
from sqlalchemy.types import Date

pg_engine = create_engine(
    'postgresql+psycopg2://postgres:test@localhost:5432/hell'
)
final_df.to_sql(
    name="daily_data",
    con=pg_engine,
    if_exists="append",
    index=False,
    dtype={
        "file_date": Date
    }
)

print("Data successfully loaded into PostgreSQL")