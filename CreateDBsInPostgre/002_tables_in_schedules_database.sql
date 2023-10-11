CREATE TABLE timetable (
  schedule_id INT NOT NULL,
  film_id INT NOT NULL,
  start_time TIMESTAMP NOT NULL,
  end_time TIMESTAMP NOT NULL,
  cin_id INT NOT NULL,
  cinhall_id INT NOT NULL,
  date DATE NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  is_3d BOOLEAN NOT NULL,
  PRIMARY KEY (schedule_id)
);
 
CREATE TABLE cinemas (
  cin_id INT NOT NULL,
  ciname_en VARCHAR(255) NOT NULL,
  ciname_uk VARCHAR(255) NOT NULL,
  ciaddress_en VARCHAR(255) NOT NULL,
  ciaddress_uk VARCHAR(255) NOT NULL,
  status_active BOOLEAN NOT NULL,
  avail_seats INT NOT NULL,
  PRIMARY KEY (cin_id)
);

CREATE TABLE tickets (
  ticket_id INT PRIMARY KEY,
  customer_id INT NOT NULL,
  schedule_id INT NOT NULL,
  row INT NOT NULL,
  seat INT NOT NULL,
  customer_name VARCHAR(255) NOT NULL,
  cin_id INT NOT NULL,
  cinhall_id INT NOT NULL,
  purch_date TIMESTAMP NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES users(customer_id),
  FOREIGN KEY (schedule_id) REFERENCES timetable(schedule_id) 
); 

CREATE TABLE users (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  ph_num VARCHAR(20) NOT NULL,
  email VARCHAR(255) NOT NULL,
  is_conf BOOLEAN NOT NULL,
  profile1 VARCHAR(255) NOT NULL,
  profile2 VARCHAR(255) NOT NULL,
  orders TEXT NOT NULL,
  transactions TEXT NOT NULL
);
