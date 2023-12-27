import faker
import os

fake = faker.Faker()

os.chdir('D:\PROJECTS\Cinema_DBS_DWH_PBI\InsertFakeSQL')

cin_id_counter = 1
cinhall_id_counter = 1

user_entries = []
tickets = []

for i in range(500000):  # Generate 500k records
    ph_num = fake.bothify(text='##########')
    
    user_entry = {
        'customer_id': i + 1,
        'ph_num': ph_num,
        'email': fake.email(),
        'is_conf': fake.random_element(elements=(True, False)),
        'profile1': fake.word(),
        'profile2': fake.word(),
        'orders': i + 1,  # Or generate some unique value
        'transactions': i + 1  
    }
    user_entries.append(user_entry)
 
    cin_id_values = list(range(1, 10))  
    cinhall_id_values = list(range(1, 8))  

    cin_id = cin_id_counter
    cinhall_id = cinhall_id_counter
    ticket_entry = {
        'ticket_id': i + 1,
        'customer_id': i + 1,
        'schedule_id': i + 1,
        'row': fake.random_int(min=1, max=18),
        'seat': fake.random_int(min=1, max=31),
        'customer_name': fake.name(),
        'cin_id': cin_id,
        'cinhall_id': cinhall_id,
        'purch_date': fake.date_time_this_decade()
    }
    tickets.append(ticket_entry)
        
    cinhall_id_counter += 1
    if cinhall_id_counter > 7:
        cinhall_id_counter = 1
        cin_id_counter += 1
        if cin_id_counter > 9:
            cin_id_counter = 1

with open('500k_users_queries.sql', 'w') as f:
    for entry in user_entries:
        insert_query = """
        INSERT INTO users (customer_id, ph_num, email, is_conf, profile1, profile2, orders, transactions)
        VALUES ({}, '{}', '{}', {}, '{}', '{}', '{}', '{}');
        """.format(
            entry['customer_id'], entry['ph_num'], entry['email'], entry['is_conf'],
            entry['profile1'], entry['profile2'], entry['orders'], entry['transactions']
        )
        f.write(insert_query + '\n')

with open('500k_tickets_queries.sql', 'w') as f:
    for entry in tickets:
        insert_query = """
        INSERT INTO tickets (ticket_id, customer_id, schedule_id, row, seat, customer_name, cin_id, cinhall_id, purch_date)
        VALUES ({}, {}, {}, {}, {}, '{}', {}, {}, '{}');
        """.format(
            entry['ticket_id'], entry['customer_id'], entry['schedule_id'], entry['row'], entry['seat'],
            entry['customer_name'], entry['cin_id'], entry['cinhall_id'], entry['purch_date']
        )
        f.write(insert_query + '\n')