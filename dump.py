import sqlite3
import pandas as pd
import os

# # for db connection
# sqlite_db = "chinook.db"
# #  Connect to SQLite
# conn = sqlite3.connect(sqlite_db)

# folder to save csvs
# output_dir = "csv_dump"
# os.makedirs(output_dir,exist_ok=True)

# # Get all user tables from SQLite
# tables = pd.read_sql("""
# SELECT name FROM sqlite_master
# WHERE type='table' AND name NOT LIKE 'sqlite_%';
# """, conn)

# # Loop through tables and dump to CSV
# for table in tables['name']:
#     df = pd.read_sql(f"SELECT * FROM {table}", conn)
#     csv_file = f"{output_dir}/{table}.csv"
#     df.to_csv(csv_file, index=False)
#     print(f"✅ {table}.csv created")

# # Close connection
# conn.close()


# PostgreSQL connection
from sqlalchemy import create_engine

 #Absolute path to CSV folder
csv_folder = r"C:\csv_dump"
pg_engine = create_engine(
    'postgresql+psycopg2://postgres:test@localhost:5432/hell'
)

#  Check folder exists
if not os.path.isdir(csv_folder):
    raise Exception(f"Folder not found: {csv_folder}")

#  Loop over CSV files
for csv_file in os.listdir(csv_folder):
    if csv_file.endswith(".csv"):
        table_name = csv_file.replace(".csv", "").lower()
        csv_path = os.path.join(csv_folder, csv_file)

        print(f"Loading {csv_path} → {table_name}")

        df = pd.read_csv(csv_path)

        df.to_sql(
            table_name,
            pg_engine,
            if_exists="replace",
            index=False,
            method="multi"
        )

        print(f"✅ {table_name} loaded successfully")

