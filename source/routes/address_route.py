from fastapi import APIRouter
from typing import Optional
from fastapi import Query
from schemas.address_schema import Address
from controllers import address_controler

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/endereco",
    tags=["endereco"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_root():
    return "funcionou amigo!"

@router.post("/cadastro")
async def create_address(endereco:Address):
    return address_controler.create_address(endereco)

@router.get("/")
async def get_address():
    return "funcionou amigo!"