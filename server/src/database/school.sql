USE school;

DROP TABLE Users;

CREATE TABLE users (id int, name varchar(50), lastname varchar(5), role varchar(5), profile varchar(5), subjects varchar(300), enrollment date);

SHOW FIELDS FROM users;