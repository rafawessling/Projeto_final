from fastapi import APIRouter
from fastapi.responses import JSONResponse
from extras.description_swagger.description_product import (
    CREATE_PRODUCT,
    GET_PRODUCT_NAME,
    GET_PRODUCT_CODE,
    DELETE_PRODUCT,
    UPDATE_PRODUCT
)
from source.schemas.product_schema import ProductSchema, ProductUpdateSchema
from source.controllers.product_controller import (
    create_product,
    get_product_by_name,
    get_product_by_code,
    delete_product_by_code,
    update_product_by_code
)

router = APIRouter(tags=['Products'], prefix='/products')

@router.post('/',
        summary="Cadastro novo produto",
        description=CREATE_PRODUCT
)
async def post_product(product: ProductSchema):
    add_product = await create_product(product)
    return JSONResponse(status_code=200, content=add_product)


@router.get('/search',
        summary="Pesquisar produtos pelo nome",
        description=GET_PRODUCT_NAME,
)
async def get_product_name(name: str):
    products = await get_product_by_name(name)
    return JSONResponse(status_code=200, content=products)

@router.get('/{code}',
        summary="Pesquisar produto pelo código",
        description=GET_PRODUCT_CODE,
)
async def get_product_code(code: str):
    product = await get_product_by_code(code)
    return JSONResponse(status_code=200, content=product)

@router.delete('/{code}',
        summary="Deletar produto",
        description=DELETE_PRODUCT,
)
async def delete_product(code: str):
    deleted_product = await delete_product_by_code(code)
    return JSONResponse(status_code=200, content=deleted_product)

@router.put('/{code}',
          summary="Atualizar produto",
          description=UPDATE_PRODUCT,
)
async def update_product(code, product: ProductUpdateSchema):
    update_product = await update_product_by_code(code, product)
    return JSONResponse(status_code=200, content=update_product)