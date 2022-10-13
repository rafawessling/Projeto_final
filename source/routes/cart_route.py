import json
from bson import ObjectId
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from extras.description_swagger.description_cart import (
    CREATE_CART,
    GET_CART_BY_USER_ID,
    DELETE_CART,
    ADD_PRODUCT,
    GET_ALL_PRODUCTS,
    REMOVE_PRODUCT
)
from schemas.cart_schema import CartSchema
from controllers.cart_controller import (
    create_cart,
    delete_cart_user,
    get_cart_by_user,
    add_product,
    get_all_products,
    remove_product
)
from schemas.order_items_schema import OrderItemsSchema
from bson import json_util

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
async def get_cart(user_id):
    cart = await get_cart_by_user(ObjectId(user_id))
    cart = json.loads(json_util.dumps(cart))
    return JSONResponse(status_code=200, content=cart)

@router.post('/add_product',
        summary="Adicionar produto ao carrinho",
                description=ADD_PRODUCT
)
async def addProduct(order_item:OrderItemsSchema):
    cart = await add_product(order_item)
    cart = json.loads(json_util.dumps(cart))
    return JSONResponse(status_code=200, content=cart)

@router.get('/all_products/{cartId}',
        summary="Pesquisar produtos do carrinho",
                description=GET_ALL_PRODUCTS
)
async def getAllProducts(cartId):
    cart = await get_all_products(ObjectId(cartId))
    cart = json.loads(json_util.dumps(cart))
    return JSONResponse(status_code=200, content=cart)

@router.delete('/remove_product',
        summary="Remove produto do carrinho",
                description=REMOVE_PRODUCT
)
async def removeProduct(order_item:OrderItemsSchema):
    cart = await remove_product(order_item)
    cart = json.loads(json_util.dumps(cart))
    return JSONResponse(status_code=200, content=cart)

@router.delete('/{user_id}',
        summary="Deletar carrinho de usuário",
                description=DELETE_CART
)
async def delete_cart(user_id):
    delete_cart = await delete_cart_user(ObjectId(user_id))
    delete_cart = json.loads(json_util.dumps(delete_cart))
    return JSONResponse(status_code=200, content=delete_cart)