import faker
import os

os.chdir('D:\PROJECTS\Cinema_DBS_DWH_PBI\InsertFakeSQL')

fake = faker.Faker()
 
user_entries = []
for i in range(1000):  # Adjust the number of entries as needed
    ph_num = fake.bothify(text='##########')
    entry = {
        'customer_id': i + 1,  
        'ph_num': ph_num,
        'email': fake.email(),
        'is_conf': fake.random_element(elements=(True, False)),
        'profile1': fake.sentence(nb_words=3).rstrip('.'),
        'profile2': fake.sentence(nb_words=3).rstrip('.'),
        'orders': i + 1,  
        'transactions': i + 1
    }
    user_entries.append(entry)

insert_queries = []
for entry in user_entries:
    insert_query = """
    INSERT INTO users (customer_id, ph_num, email, is_conf, profile1, profile2, orders, transactions)
    VALUES ({}, '{}', '{}', {}, '{}', '{}', '{}', '{}');
    """.format(
        entry['customer_id'], entry['ph_num'], entry['email'], entry['is_conf'], entry['profile1'],
        entry['profile2'], entry['orders'], entry['transactions']
    )
    insert_queries.append(insert_query)

with open('005_users_queries.sql', 'w') as f:
    for insert_query in insert_queries:
        f.write(insert_query + '\n')