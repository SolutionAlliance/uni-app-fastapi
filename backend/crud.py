from sqlalchemy.orm import Session
from models import User, Base
from schemas import UserCreate, UserResponse
from bcrypt import hashpw, gensalt, checkpw

# Hash password
def hash_password(password: str) -> str:
    return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')

# Verify password
def verify_password(password: str, hashed_password: str) -> bool:
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Create user
def add_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get user by username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()