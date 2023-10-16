from sqlalchemy import create_engine
import pandas as pd

         # URLs для MySQL movies, schedules, users БД, та PostgreSQL БД
MySQL_URL_1 = "mysql+pymysql://YOUR_USER:YOUR_PASS@localhost:3306/movies"
MySQL_URL_2 = "mysql+pymysql://YOUR_USER:YOUR_PASS@localhost:3306/cinemas"
MySQL_URL_3 = "mysql+pymysql://YOUR_USER:YOUR_PASS@localhost:3306/schedules"
reddev_url = "postgresql://postgres:YOUR_PASS@localhost:5432/redshift_dev"
 
         # Створюємо SQLAlchemy-з'єднання для БД
conn_movies = create_engine(MySQL_URL_1)
conn_mysql = create_engine(MySQL_URL_2)
conn_schedules = create_engine(MySQL_URL_3)
conn_reddev = create_engine(reddev_url)
 
         # Витягаємо дані з джерел
films_df = pd.read_sql_query("SELECT * FROM films", MySQL_URL_1)
cinemas_df = pd.read_sql_query("SELECT * FROM users", MySQL_URL_2)
timetable_df = pd.read_sql_query("SELECT * FROM timetable", MySQL_URL_3)
tickets_df = pd.read_sql_query("SELECT * FROM tickets", MySQL_URL_3)
users_df = pd.read_sql_query("SELECT * FROM users", MySQL_URL_3)
 
         # "films" + "timetable" з'єднуємо
films_timetable_df = films_df.merge(timetable_df, on='film_id', how='left') 

         # cinemas + films_timetable 
cinemas_films_timetable_df = cinemas_df.merge(films_timetable_df, on='cin_id', how='left')

         # tickets + cinemas_films_timetable 
final_df = cinemas_films_timetable_df.merge(
    tickets_df, on=['schedule_id', 'cin_id', 'cinhall_id'], how='left')
 
         # users + final_df   
final_df = final_df.merge(users_df, on='customer_id', how='left')
 
         # Загружаємо у redshift_dev (PostgreSQL БД)   
final_df.to_sql('cinema_data', conn_reddev, if_exists='replace', index=False)

""" 
До відома, Amazon Redshift з'єднання за допомогою SQLAlchemy.  

# 001 redshift_url = "postgresql://your_redshift_user:your_redshift_password@your_redshift_host:5439/your_redshift_db" 
# 002 conn_redshift = create_engine(redshift_url)
# 003 final_df.to_sql('cinema_data', conn_redshift, if_exists='replace', index=False)

З psycopg2 отримаєте lower-level abstraction, але - повільніша.
"""

