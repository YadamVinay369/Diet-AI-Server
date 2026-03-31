import bcrypt
from schemas.user import UserCreate, UserPublic, UserLogin
from utils.db_utils.db import db
from bson import ObjectId
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from utils.auth_utils.jwt_create_validate import create_access_token

router = APIRouter()

def hash_password(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode('utf-8'), 
        hashed_password.encode('utf-8')
    )

@router.post("/signup") 
async def signup(user: UserCreate):
    if user.username:
        existing_user = await db.users.find_one({
            "$or": [
                {"username": user.username},
                {"email": user.email}
            ]
        })
    else:
        # Case 2: only email
        existing_user = await db.users.find_one({
            "email": user.email
        })

    if existing_user:
        if user.username and existing_user.get("username") == user.username:
            raise HTTPException(
                status_code=400,
                detail="User already exists with the same username"
            )
        
        if existing_user.get("email") == user.email:
            raise HTTPException(
                status_code=400,
                detail="User already exists with the same email"
            )
    
    hashed_pw = hash_password(user.password)
    
    user_dict = user.dict()
    user_dict["hashed_password"] = hashed_pw
    user_dict["overall_nutrient_sheet"] = {}
    user_dict["attendance"] = []
    user_dict["frequency"] = []
    
    del user_dict["password"]
    result = await db.users.insert_one(user_dict)
    user_id = str(result.inserted_id)
    
    access_token = create_access_token(data={"sub": user_id})
    
    response = JSONResponse(content={
        "message": "Signup successful!",
        "user": {
            "id": user_id,
            "username": user.username,
            "email": user.email,
            "overall_nutrients_sheet": user_dict["overall_nutrient_sheet"]
        }
    })
    
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite="None",
        secure=True,
        max_age=60*60*24,
        path="/",
    )
    return response

@router.post("/login")
async def login(user: UserLogin):
    db_user = await db.users.find_one({
        "$or": [
            {"username": user.user_name_or_email},
            {"email": user.user_name_or_email}
        ]
    })
    
    if not db_user or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid Credentials") 
    
    access_token = create_access_token(data={"sub": str(db_user["_id"])})
    
    response = JSONResponse(content={
        "message": "login successful!",
        "user": {
            "id": str(db_user["_id"]),
            "username": db_user["username"],
            "email": db_user["email"],
            "overall_nutrients_sheet": db_user.get("overall_nutrient_sheet", {}),
            "time_frame": db_user.get("time_frame")
        }
    })
    
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite="None",
        secure=True,
        max_age=60*60*24,
        path="/",
    )
    return response

@router.get("/logout")
async def logout():
    response = JSONResponse(content={"message": "Logged out successfully!"})
    response.delete_cookie(
        key="access_token",
        path="/",
        httponly=True,
        samesite="None",
        secure=True,
    )
    
    return response