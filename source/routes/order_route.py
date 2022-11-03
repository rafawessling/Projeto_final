from fastapi import APIRouter
from schemas.order_schema import OrderSchema
from controllers import order_controller 
from bson.objectid import ObjectId
from extras.description_swagger.description_order import (
    CREATE_ORDER,
    GET_ORDER
)


router = APIRouter(
    prefix="/order",
    tags=["Order"],
    responses={404: {"description": "Not found"}},
)

@router.post("/",
        summary = "Criar order",
        description=CREATE_ORDER
        )
async def create_order(order:OrderSchema):
    return await order_controller.create_order(order)

@router.get("/{id}/", 
        summary = "Buscar order",
        description=GET_ORDER
        )
async def get_order(id):
    return await order_controller.get_order(ObjectId(id))