from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse
from app.models.user import User
from app.db.deps import get_db
from app.core.security import hash_password


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):

    # check if user exists
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # hash password
    hashed_password = hash_password(user.password)

    # create user object
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password
    )

    # save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


from app.schemas.user import UserLogin, Token
from app.core.security import verify_password, create_access_token

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        data={"user_id": db_user.id}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }