CREATE TABLE users (
    id serial primary key NOT NULL,
    email varchar(255),
    password_digest varchar(255)
)
