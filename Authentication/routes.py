from auth import authenticate_user
from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/protected")
def protected_route(username: str = Depends(authenticate_user)):
    return {"message": f"Hello {username}!"}