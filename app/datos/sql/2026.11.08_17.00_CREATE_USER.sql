USE db_test;

CREATE USER 'db_test'@'localhost' IDENTIFIED BY 'db_test';

GRANT ALL PRIVILEGES ON db_test.* TO 'db_test'@'localhost';

FLUSH PRIVILEGES;