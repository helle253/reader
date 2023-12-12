GRANT USAGE ON SCHEMA reader_db TO nathan;
GRANT ALL ON ALL TABLES IN SCHEMA reader_db TO nathan;

INSERT INTO ops (op) VALUES ('grants nathan');
