# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User,Base
from schemas import UserCreate, UserResponse
from crud import get_user_by_username,verify_password,add_user
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost:8080",  # Add your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/auth/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username=user.username)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="user password incorrect")
    return {"message": "Login successful"}

@app.post("/users/create", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return add_user(db, user=user)

@app.get("/users", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}
