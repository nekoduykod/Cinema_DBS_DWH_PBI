from db_conn import mysql_db_conn, connect_reddev, merge_tables
import pandas as pd

db_connections = mysql_db_conn()

query = "SELECT * FROM "
films_df = pd.read_sql_query(f"{query}films", db_connections)
cinemas_df = pd.read_sql_query(f"{query}users", db_connections)
timetable_df = pd.read_sql_query(f"{query}timetable", db_connections)
tickets_df = pd.read_sql_query(f"{query}tickets", db_connections)
users_df = pd.read_sql_query(f"{query}users", db_connections)

final_df2 = merge_tables(films_df, cinemas_df, timetable_df, tickets_df, users_df)

conn_reddev = connect_reddev()
final_df2.to_sql('cinema_dwh', conn_reddev, if_exists='append', index=False)

"""  
redshift_url = "postgresql://your_red_user:your_red_pswd@redshift_host:5439/your_redshift_db" 
conn_redshift = create_engine(redshift_url)
final_df.to_sql('cinema_data', conn_redshift, if_exists='replace', index=False)

"""