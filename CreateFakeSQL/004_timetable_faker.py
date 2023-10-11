import faker
import os
import random
from datetime import datetime, timedelta

# Change the current working directory to the desired directory
os.chdir('D:\projects\databases_to_DWH\data_filler')

# Create a Faker object
fake = faker.Faker()

# Generate a list of fake timetable entries with your specified pattern
timetable_entries = []

# Define a time window for scheduling, let's say 30 days ago to 30 days in the future
start_date = datetime.now() - timedelta(days=30)
end_date = datetime.now() + timedelta(days=30)

# Initialize counters for cin_id and cinhall_id
cin_id_counter = 1
cinhall_id_counter = 1

# Continue generating entries until we reach 1000 inserts
while len(timetable_entries) < 1000:
    # Generate random minutes in the range of 80 to 140
    minutes = random.randint(80, 140)

    # Calculate end time by adding the minutes to start_time
    start_time = fake.date_time_between(start_date=start_date, end_date=end_date)
    end_time = start_time + timedelta(minutes=minutes)

    entry = {
        'schedule_id': len(timetable_entries) + 1,
        'film_id': len(timetable_entries) + 1,
        'start_time': start_time,
        'end_time': end_time,
        'cin_id': cin_id_counter,
        'cinhall_id': cinhall_id_counter,
        'date': fake.date_between(start_date=start_date, end_date=end_date),
        'price': round(random.uniform(5, 15), 2),
        'is_3d': fake.random_element(elements=(True, False))
    }
    timetable_entries.append(entry)

    # Update cin_id and cinhall_id counters, and start over if needed
    cinhall_id_counter += 1
    if cinhall_id_counter > 7:
        cinhall_id_counter = 1
        cin_id_counter += 1
        if cin_id_counter > 9:
            cin_id_counter = 1

# Generate insert queries for each timetable entry
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

# Write the insert queries to a file
with open('timetable_queries.sql', 'w') as f:
    for insert_query in insert_queries:
        f.write(insert_query + '\n')
