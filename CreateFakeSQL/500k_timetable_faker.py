import faker
import os
import random
from datetime import datetime, timedelta

os.chdir('D:\PROJECTS\Cinema_DBS_DWH_PBI\InsertFakeSQL')
fake = faker.Faker()
timetable_entries = []

start_date = datetime.now() - timedelta(days=30)
end_date = datetime.now() + timedelta(days=30)

cin_id_counter = 1
cinhall_id_counter = 1

while len(timetable_entries) < 500000:
    minutes = random.randint(80, 140)

    start_time = fake.date_time_between(start_date=start_date, end_date=end_date)
    end_time = start_time + timedelta(minutes=minutes)

    entry = {
        'schedule_id': len(timetable_entries) + 1,  # Можна встановити до максимум 10 sched_id, по принципу cin_id, 
        'film_id': len(timetable_entries) + 1,      # щоб не було 500 тисяч schedule_id. Так само для фільмів, тощо
        'start_time': start_time,
        'end_time': end_time,
        'cin_id': cin_id_counter,
        'cinhall_id': cinhall_id_counter,
        'date': fake.date_between(start_date=start_date, end_date=end_date),
        'price': round(random.uniform(5, 15), 2),
        'is_3d': fake.random_element(elements=(True, False))
    }
    timetable_entries.append(entry)

    cinhall_id_counter += 1
    if cinhall_id_counter > 7:
        cinhall_id_counter = 1
        cin_id_counter += 1
        if cin_id_counter > 9:
            cin_id_counter = 1

insert_queries = []
for entry in timetable_entries:
    insert_query = """
    INSERT INTO timetable (schedule_id, film_id, start_time, end_time, cin_id, cinhall_id, date, price, is_3d)
    VALUES ({}, {}, '{}', '{}', {}, {}, '{}', {}, {});
    """.format(
        entry['schedule_id'], entry['film_id'], entry['start_time'], entry['end_time'], entry['cin_id'],
        entry['cinhall_id'], entry['date'], entry['price'], entry['is_3d']
    )
    insert_queries.append(insert_query)

with open('500k_timetable_queries.sql', 'w') as f:
    for insert_query in insert_queries:
        f.write(insert_query + '\n')