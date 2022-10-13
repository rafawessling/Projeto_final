from fastapi import APIRouter
from schemas.user_schema import User
from controllers import user_controller
from bson.objectid import ObjectId
from extras.description_swagger.description_user import (
    CREATE_USER,
    GET_USER,
    GET_USERS,
    GET_USERS_BY_EMAIL,
    UPDATE_USER,
    DELETE_USER
)


router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_root():
    return "funcionou amigo!"

@router.post("/", 
        summary="Cadastro novo usuário",
        description=CREATE_USER)
async def create_user(user:User):
    return await user_controller.create_user(user)

@router.get("/{id}/", 
        summary="Buscar usuário pelo id",
        description=GET_USER)
async def get_user(id:str):
    return await user_controller.get_user(ObjectId(id))

@router.get("/get_all_users",
        summary="Buscar usuário",
        description=GET_USERS)
async def get_users():
    return await user_controller.get_users()

@router.get("/get_user_by_email",
        summary="Buscar usuário pelo email",
        description=GET_USERS_BY_EMAIL)
async def get_user_by_email(email:str):
    return await user_controller.get_user_by_email(email)

@router.put("/update_user/{id}",
        summary="Atualizar usuário",
        description=UPDATE_USER)
async def update_user(id:str, user:User):
    return await user_controller.update_user(user_id=ObjectId(id), user_data=user)

@router.delete("/delete_user", 
        summary="Deletar usuário",
        description=DELETE_USER)
async def delete_user(id:str):
    return await user_controller.delete_user(ObjectId(id))
