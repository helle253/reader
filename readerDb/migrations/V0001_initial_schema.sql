CREATE SCHEMA foo;

CREATE TABLE foo.foo (
    id BIGINT PRIMARY KEY,
    source TEXT NOT NULL,
    path TEXT NOT NULL,
);

INSERT INTO ops (op) VALUES ('migration V0001__Initial_schema.sql');
