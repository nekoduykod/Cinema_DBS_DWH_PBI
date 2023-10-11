from sqlalchemy import create_engine
import pandas as pd

         # Визначаємо URLs для PostgreSQL redshift_dev, movies, schedules, users баз даних
movies_url = "postgresql://postgres:123@localhost:5432/movies"
sched_url = "postgresql://postgres:123@localhost:5432/schedules"
reddev_url = "postgresql://postgres:123@localhost:5432/redshift_dev"

         # Створюємо SQLAlchemy з'єднання для кожної бази 
conn_reddev = create_engine(reddev_url)
conn_movies = create_engine(movies_url)
conn_schedules = create_engine(sched_url)

         # Витягаємо дані з джерел
films_df = pd.read_sql_query("SELECT * FROM films", movies_url)
timetable_df = pd.read_sql_query("SELECT * FROM timetable", sched_url)
cinemas_df = pd.read_sql_query("SELECT * FROM cinemas", sched_url)
tickets_df = pd.read_sql_query("SELECT * FROM tickets", sched_url)
users_df = pd.read_sql_query("SELECT * FROM users", sched_url)

 
         # "films" + "timetable" 
print("films_df:")
print(films_df.shape)
films_timetable_df = films_df.merge(timetable_df, on='film_id', how='left') 
print("films_timetable_df:")
print(films_timetable_df.shape)
         # cinemas + films_timetable 
cinemas_films_timetable_df = cinemas_df.merge(films_timetable_df, on='cin_id', how='left')
print("cinemas_films_timetable:")
print(cinemas_films_timetable_df.shape)
         # tickets + cinemas_films_timetable 
final_df = cinemas_films_timetable_df.merge(
    tickets_df, on=['schedule_id', 'cin_id', 'cinhall_id'], how='left')
print("final_df:")
print(final_df.shape)
         # users + final_df   
final_df = final_df.merge(users_df, on='customer_id', how='left')
print("final_df2:")
print(final_df.shape) 

        # Загружаємо у PostgreSQL DB redshift_dev 
final_df.to_sql('test_warehouse', conn_reddev, if_exists='replace', index=False) 