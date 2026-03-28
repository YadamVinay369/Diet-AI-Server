from fastapi import Request, HTTPException, Depends
from bson import ObjectId
from utils.db_utils.db import db
from utils.auth_utils.jwt_create_validate import verify_access_token

def get_token_from_cookie(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(
            status_code=401, 
            detail="Not authenticated - Missing access_token cookie"
        )
    return token
async def get_current_user(token: str = Depends(get_token_from_cookie)):
    try:
        payload = verify_access_token(token)
        user_id = payload.get("sub")
        
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        
        user = await db.users.find_one({"_id": ObjectId(user_id)})
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
            
        return user_id     
    except Exception as e:
        print(f"Auth Error: {str(e)}")
        raise HTTPException(
            status_code=403, 
            detail="Could not validate credentials"
        )