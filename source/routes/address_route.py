from fastapi import APIRouter
from schemas.address_schema import Address
from controllers import address_controler
from bson.objectid import ObjectId


router = APIRouter(
    prefix="/address",
    tags=["address"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_root():
    return "funcionou amigo!"

@router.post("/")
async def create_address(address:Address):
    return await address_controler.create_address(address)

@router.get("/{id}/")
async def get_address(id:str):
    return await address_controler.get_address(ObjectId(id))

@router.get("/get_all_addresses")
async def get_all_addresses():
    return await address_controler.get_all_addresses()

@router.delete("/delete_address")
async def delete_address(id:str):
    return await address_controler.delete_address(ObjectId(id))