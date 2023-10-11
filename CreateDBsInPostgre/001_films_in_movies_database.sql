CREATE table films (
  film_id INT NOT NULL,
  finame_en VARCHAR(255) NOT NULL,
  finame_uk VARCHAR(255) NOT NULL,
  finame_de VARCHAR(255) NOT NULL,
  descr_en VARCHAR(1000) NOT NULL,
  descr_uk VARCHAR(1000) NOT NULL,
  descr_de VARCHAR(1000) NOT NULL,
  technology VARCHAR(255) NOT NULL,
  duration INT NOT NULL,
  genres VARCHAR(255) NOT NULL,
  categories VARCHAR(255) NOT NULL
);