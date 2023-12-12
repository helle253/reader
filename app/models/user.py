from passlib.hash import sha256_crypt;
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
        digest = sha256_crypt.hash(password)
        cursor.execute("INSERT INTO users (email, password_digest) VALUES (%s, %s)", (email, digest))
      conn.commit()
    return cls(email, digest)

  @classmethod
  def authenticate(cls, email: str, password: str) -> 'User':
      with open_connection() as conn:
        with conn.cursor() as cursor:
          cursor.execute("SELECT password_digest FROM users WHERE email = %s", (email,))
          row = cursor.fetchone()
          if not row or sha256_crypt.verify(password, row[0]):
            raise Exception("Invalid email or password")
          return cls(email, row[0])
