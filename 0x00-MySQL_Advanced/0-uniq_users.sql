-- Script that create a tablr users
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255)NOT NULL UNIQUE,
    name VARCHAR(255)
);
