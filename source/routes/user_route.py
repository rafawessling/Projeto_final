from fastapi import APIRouter
from schemas.user_schema import User
from controllers import user_controller
from bson.objectid import ObjectId


router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_root():
    return "funcionou amigo!"

@router.post("/")
async def create_user(user:User):
    return await user_controller.create_user(user)

@router.get("/{id}/")
async def get_user(id:str):
    return await user_controller.get_user(ObjectId(id))

@router.get("/get_all_users")
async def get_all_users():
    return await user_controller.get_users()

@router.get("/get_user_by_email")
async def get_user_by_email(email:str):
    return await user_controller.get_user_by_email(email)

@router.put("/update_user/{id}")
async def update_user(id:str, user:User):
    return await user_controller.update_user(user_id=ObjectId(id), user_data=user)

@router.delete("/delete_user")
async def delete_user(id:str):
    return await user_controller.delete_user(ObjectId(id))