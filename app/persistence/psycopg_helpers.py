import os
import psycopg

def open_connection() -> psycopg.connection:
  return psycopg.connect(conninfo=os.getenv('DB_CONNECTION'));
