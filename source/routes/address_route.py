from fastapi import APIRouter
from schemas.address_schema import Address
from controllers import address_controler
from bson.objectid import ObjectId
from extras.description_swagger.description_address import (
    CREATE_ADDRESS,
    GET_ADDRESS,
    GET_ALL_ADDRESSES,
    DELETE_ADDRESS,
    DELETE_ALL_ADDRESSES
)


router = APIRouter(
    prefix="/address",
    tags=["address"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_root():
    return "funcionou amigo!"

@router.post("/",
        summary = "Cadastrar endereço",
        description=CREATE_ADDRESS)
async def create_address(address:Address):
    return await address_controler.create_address(address)

@router.get("/{id}/", 
        summary = "Buscar endereço",
        description=GET_ADDRESS)
async def get_address(id:str):
    return await address_controler.get_address(ObjectId(id))

@router.get("/get_all_addresses/{id}/",
        summary = "Buscar lista de endereços",
        description=GET_ALL_ADDRESSES)
async def get_all_addresses(id:str):
    return await address_controler.get_all_addresses(ObjectId(id))

@router.delete("/delete_address/",
        summary = "Deletar endereço",
        description=DELETE_ADDRESS)
async def delete_address(id:str):
    return await address_controler.delete_address(ObjectId(id))

@router.delete("/delete_all_addresses/",
        summary = "Deletar todos os endereços",
        description=DELETE_ALL_ADDRESSES)
async def delete_all_addresses(id:str):
    return await address_controler.delete_all_addresses(ObjectId(id))
