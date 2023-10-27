import faker
import os

os.chdir('D:\PROJECTS\Cinema_DBS_DWH_PBI\InsertFakeSQL')
fake = faker.Faker()

films = []
for i in range(500000):
    film = {
        'film_id': i + 1,
        'finame_en': fake.word(),
        'finame_uk': fake.word(),
        'finame_de': fake.word(),
        'descr_en': fake.word(),
        'descr_uk': fake.word(),
        'descr_de': fake.word(),
        'technology': fake.random_element(elements=('2D', '3D', 'IMAX')),
        'duration': fake.random_int(min=60, max=180),
        'genres': fake.random_element(elements=('Action', 'Adventure', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Thriller')),
        'categories': ', '.join(fake.random_elements(elements=('Blockbuster', 'Independent', 'Documentary'), length=2))
    }
    films.append(film)

insert_queries = []
for film in films:
    insert_query = """
    INSERT INTO films (film_id, finame_en, finame_uk, finame_de, descr_en, descr_uk, descr_de, technology, duration, genres, categories)
    VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, '{}', '{}');
    """.format(
        film['film_id'], film['finame_en'], film['finame_uk'], film['finame_de'],
        film['descr_en'], film['descr_uk'], film['descr_de'], film['technology'],
        film['duration'], film['genres'], film['categories']
    )
    insert_queries.append(insert_query)

with open('500k_films_queries.sql', 'w') as f:
    for insert_query in insert_queries:
        f.write(insert_query + '\n')
