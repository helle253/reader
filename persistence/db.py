import os
import psycopg

def open_connection() -> psycopg.connection:
  return psycopg.connect(os.getenv('DB_CONNECTION'));
