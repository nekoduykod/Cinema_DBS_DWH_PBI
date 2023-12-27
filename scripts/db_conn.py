from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def mysql_db_conn(database_names=None):
    if database_names is None:
         database_names = ["/movies", "/cinemas", "/schedules"]
    
    mysql_url = os.getenv("MYSQL_URL")
    connections = {}
    
    for db_name in database_names:
            db_url = f"{mysql_url}{db_name}"
            connections[db_name] = create_engine(db_url)
    return connections

def postgre_db_conn(database_names=None):
    if database_names is None:
        database_names = ["/movies", "/schedules"]
    pg_url = os.getenv("PG_URL")
    connections = {}

    for db_name in database_names:
        db_url = f"{pg_url}{db_name}"
        connections[db_name] = create_engine(db_url)
    return connections

def connect_reddev():
    reddev_url = os.getenv("REDSHIFT")
    conn_reddev = create_engine(reddev_url)
    return conn_reddev

def merge_tables(films_df, cinemas_df, timetable_df, tickets_df, users_df):
    films_timetable_df = films_df \
        .merge(timetable_df, on='film_id', how='left') 
    cinemas_films_timetable_df = cinemas_df \
        .merge(films_timetable_df, on='cin_id', how='left')
    final_df1 = cinemas_films_timetable_df \
        .merge(tickets_df, on=['schedule_id', 'cin_id', 'cinhall_id'], how='left')
    final_df2 = final_df1.merge(users_df, on='customer_id', how='left')
    return final_df2