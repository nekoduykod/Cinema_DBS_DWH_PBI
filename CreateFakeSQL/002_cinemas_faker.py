import faker
import os

os.chdir('D:\PROJECTS\Cinema_DBS_DWH_PBI\InsertFakeSQL')

fake = faker.Faker()
id = 1

cinemas = []
for i in range(9):
    cinema = {
        'cin_id': id,
        'ciname_en': fake.company(),
        'ciname_uk': fake.company_suffix(),
        'ciaddress_en': fake.address(),
        'ciaddress_uk': fake.address(),
        'status_active': fake.random_element(elements=(True, False)),
        'avail_seats': fake.random_int(min=50, max=200)  # Adjust the range as needed
    }
    cinemas.append(cinema)

    id += 1
    
insert_queries = []
for cinema in cinemas:
    insert_query = """
    INSERT INTO cinemas (cin_id, ciname_en, ciname_uk, ciaddress_en, ciaddress_uk, status_active, avail_seats)
    VALUES ({}, '{}', '{}', '{}', '{}', {}, {});
    """.format(
        cinema['cin_id'], cinema['ciname_en'], cinema['ciname_uk'], cinema['ciaddress_en'], 
        cinema['ciaddress_uk'], cinema['status_active'], cinema['avail_seats']
    )
    insert_queries.append(insert_query)

with open('002_cinema_queries.sql', 'w') as f:
    for insert_query in insert_queries:
        f.write(insert_query + '\n')