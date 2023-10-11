import faker
import os

# Change the current working directory to the directory where you want to save the SQL queries
os.chdir('D:\projects\databases_to_DWH\data_filler')

# Create a Faker object
fake = faker.Faker()

# Generate a list of 1000 fake films
films = []
for i in range(1000):
    film = {
        'film_id': i + 1,   
        'finame_en': fake.sentence(nb_words=3).rstrip('.'),
        'finame_uk': fake.sentence(nb_words=3).rstrip('.'),
        'finame_de': fake.sentence(nb_words=3).rstrip('.'),
        'descr_en': fake.text(max_nb_chars=1000).rstrip('.'),
        'descr_uk': fake.text(max_nb_chars=1000).rstrip('.'),
        'descr_de': fake.text(max_nb_chars=1000).rstrip('.'),
        'technology': fake.random_element(elements=('2D', '3D', 'IMAX')),
        'duration': fake.random_int(min=60, max=180),
        'genres': fake.random_element(elements=('Action', 'Adventure', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Thriller')),
        'categories': ', '.join(fake.random_elements(elements=('Blockbuster', 'Independent', 'Documentary'), length=2))
    }
    films.append(film)

# Generate insert queries for each film
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

# Write the insert queries to a file
with open('films_queries.sql', 'w') as f:
    for insert_query in insert_queries:
        f.write(insert_query + '\n')
