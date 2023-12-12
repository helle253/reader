from werkzeug.security import check_password_hash, generate_password_hash;

from persistence.db import open_connection;
from app import db;

class UserModel(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(255), unique=True)
  password_digest = db.Column(db.String(255))

  def __init__(self, email: str, password_digest: str):
    self.email = email
    self.password_digest = password_digest

class User(UserModel):
  @classmethod
  def create(cls, email: str, password: str) -> 'User':
    with open_connection() as conn:
      with conn.cursor() as cursor:
        digest = generate_password_hash(password)
        cursor.execute("INSERT INTO users (email, password_digest) VALUES (%s, %s)", (email, digest))
      conn.commit()
    return cls(email, digest)

  @classmethod
  def authenticate(cls, email: str, password: str) -> 'User':
      with open_connection() as conn:
        with conn.cursor() as cursor:
          cursor.execute("SELECT password_digest FROM users WHERE email = %s", (email,))
          row = cursor.fetchone()
          if not row or check_password_hash(row[0], password):
            raise Exception("Invalid email or password")
          return cls(email, row[0])

  def change_password(self, new_password: str) -> None:
    new_digest = generate_password_hash(new_password)
    with open_connection() as conn:
      with conn.cursor() as cursor:
        cursor.execute("UPDATE users SET password_digest = %s WHERE email = %s", (new_digest, self.email))
    self.password_digest = new_digest


  def change_email(self, new_email: str) -> None:
    with open_connection() as conn:
      with conn.cursor() as cursor:
        cursor.execute("UPDATE users SET email = %s WHERE email = %s", (new_email, self.email))
    self.email = new_email
