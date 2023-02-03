DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS countries;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    capital VARCHAR (255),
    currency VARCHAR (255),
    review text,
    user_id INT NOT NULL REFERENCES users(id)

);

