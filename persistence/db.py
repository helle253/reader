import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg

class DB:
  __instance = None

  @staticmethod
  def initialize(app: Flask):
    DB.__instance = SQLAlchemy(app)

  @staticmethod
  def get():
    if DB.__instance is None:
      raise Exception("DB not initialized")
    return DB.__instance

  @staticmethod
  def open_connection():
    return psycopg.connect(os.getenv('DB_CONNECTION'));
