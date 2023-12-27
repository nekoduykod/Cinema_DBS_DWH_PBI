CREATE DATABASE movies;
 
CREATE DATABASE schedules;

CREATE DATABASE redshift_dev;
 
-- Налаштуйте user owner. Обрав 'postgres' user з паролем, який треба для .py-script`s connection   
-- Коли таблиці створите, наповніть даними з InsertFakeSQL папки
-- до речі, cinemas table можна в іншій базі даних створити, якщо треба. Відповідно, .py-скрипт відкорегувати
-- Далі, .py скрипт - до ваших послуг '''