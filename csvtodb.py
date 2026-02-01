import pandas as pd 
from sqlalchemy import create_engine # Creates a database engine and Handles connection pooling & SQL execution

# # SQLite
# sqlite_conn = sqlite3.connect("chinook.db")

# PostgreSQL
pg_engine = create_engine(
    'postgresql+psycopg2://postgres:test@localhost:5432/hell'
)

df_school = pd.read_csv(r'F:\smapledata\schools.csv')

df_school.to_sql('heaven', pg_engine , if_exists='replace' , index= False)
print('convert done')
