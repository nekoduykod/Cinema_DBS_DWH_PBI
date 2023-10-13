import faker
import os

# Directory to load
os.chdir('D:\PROJECTS\Cinema_DBS_DWH_PBI\InsertFakeSQL')

# Create a Faker object
fake = faker.Faker()

# Initialize the 'id' variable
id = 1

# Generate a list of fake tickets
tickets = []
cin_id_values = list(range(1, 10))  
cinhall_id_values = list(range(1, 8))  

# Initialize counters for cin_id and cinhall_id
cin_id_counter = 1
cinhall_id_counter = 1

# Continue generating entries until we reach 1000 inserts
while id <= 1000:
    cin_id = cin_id_counter
    cinhall_id = cinhall_id_counter

    ticket = {
        'ticket_id': id,
        'customer_id': id,
        'schedule_id': id,
        'row': fake.random_int(min=1, max=18),
        'seat': fake.random_int(min=1, max=31),
        'customer_name': fake.name(),
        'cin_id': cin_id,
        'cinhall_id': cinhall_id,
        'purch_date': fake.date_time_this_decade()
    }
    tickets.append(ticket)

    # Increment 'id' for the next record
    id += 1

    # Update cin_id and cinhall_id counters, and start over if needed
    cinhall_id_counter += 1
    if cinhall_id_counter > 7:
        cinhall_id_counter = 1
        cin_id_counter += 1
        if cin_id_counter > 9:
            cin_id_counter = 1

# Generate insert queries for each ticket
insert_queries = []
for ticket in tickets:
    insert_query = """
    INSERT INTO tickets (ticket_id, customer_id, schedule_id, row, seat, customer_name, cin_id, cinhall_id, purch_date)
    VALUES ({}, {}, {}, {}, {}, '{}', {}, {}, '{}');
    """.format(
        ticket['ticket_id'], ticket['customer_id'], ticket['schedule_id'], ticket['row'], ticket['seat'],
        ticket['customer_name'], ticket['cin_id'], ticket['cinhall_id'], ticket['purch_date']
    )
    insert_queries.append(insert_query)

# Write the insert queries to a file
with open('003_ticket_queries.sql', 'w') as f:
    for insert_query in insert_queries:
        f.write(insert_query + '\n')
