from fastapi import APIRouter
from fastapi.responses import JSONResponse
from extras.description_swagger.description_cart import (
    CREATE_CART,
    GET_CART_BY_USER_ID,
    DELETE_CART
)
from source.schemas.cart_schema import CartSchema
from source.controllers.cart_controller import (
    create_cart,
    delete_cart_user,
    get_cart_by_user
)

router = APIRouter(tags=['Cart'], prefix='/cart')

@router.post('/',
        summary="Cadastro novo carrinho para usuário",
        description=CREATE_CART
)
async def post_cart(cart: CartSchema):
    add_cart = await create_cart(cart)
    return JSONResponse(status_code=200, content=add_cart)

@router.get('/{user_id}',
        summary="Pesquisar carrinho de usuário",
                description=GET_CART_BY_USER_ID
)
async def get_cart(user_id: str):
    cart = await get_cart_by_user(user_id)
    return JSONResponse(status_code=200, content=cart)

@router.delete('/{user_id}',
        summary="Deletar carrinho de usuário",
                description=DELETE_CART
)
async def delete_cart(user_id: str):
    delete_cart = await delete_cart_user(user_id)
    return JSONResponse(status_code=200, content=delete_cart)