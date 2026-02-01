
import sqlite3    # Allows Python to read SQLite (.db) files
import pandas as pd 
from sqlalchemy import create_engine # Creates a database engine and Handles connection pooling & SQL execution

# SQLite
sqlite_conn = sqlite3.connect("chinook.db")

# PostgreSQL
pg_engine = create_engine(
    'postgresql+psycopg2://postgres:test@localhost:5432/test'
)

tables = pd.read_sql("""
SELECT name FROM sqlite_master 
WHERE type='table' AND name NOT LIKE 'sqlite_%';
""", sqlite_conn)
# To access every table using for loop
for table in tables['name']:
    df = pd.read_sql(f"SELECT * FROM {table}", sqlite_conn)
    df.to_sql(table.lower(), pg_engine, if_exists="replace", index=False)
    print(f"✅ {table} migrated")