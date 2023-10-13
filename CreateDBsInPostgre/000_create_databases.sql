-- Для films таблиці 
CREATE DATABASE movies;

-- Для tickets, timetable, users, cinemas таблиці    
CREATE DATABASE schedules;

-- Для кінцевої об'єднаної таблиці aka cinena_data "data warehouse"
CREATE DATABASE redshift_dev;
 

-- Налаштуйте user owner. Обрав 'postgres' user з паролем, який треба для .py-script`s connection   
-- Коли таблиці створите, наповніть даними з InsertFakeSQL папки
-- Далі, .py скрипт - до ваших послуг '''