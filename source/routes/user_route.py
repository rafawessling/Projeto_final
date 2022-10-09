from fastapi import APIRouter
from fastapi.responses import JSONResponse

from source.schemas.user_schema import UserSchema, UpdateUser
from extras.description_swagger.description_user import(
    CREATE_USER,
    GET_USER_NAME,
    GET_USER_CODE,
    DELETE_USER
)

router = APIRouter(tags=['User'], prefix='/user')

@router.post('/',
        summary="Cadastro de novo usuário",
        description=CREATE_USER
)
async def post_user(user: UserSchema):
    add_user = await create_user(user)
    return JSONResponse(status_code=200, content=add_user)


@router.get('/search',
        summary="Pesquisar usuário pelo nome",
        description=GET_USER_NAME,
)
async def get_user_name(name: str):
    user = await get_user_by_name(name)
    return JSONResponse(status_code=200, content=user)

@router.get('/{code}',
        summary="Pesquisar usuário pelo código",
        description=GET_USER_CODE,
)
async def get_user_code(code: str):
    user = await get_user_by_code(code)
    return JSONResponse(status_code=200, content=user)

@router.delete('/{code}',
        summary="Deletar usuário",
        description=DELETE_USER,
)
async def delete_user(code: str):
    deleted_user = await delete_user_by_code(code)
    return JSONResponse(status_code=200, content=deleted_user)

@router.put('/{code}',
          summary="Atualizar usuário",
          description=UPDATE_user,
)
async def update_user(code, user: userUpdateSchema):
    update_user = await update_user_by_code(code, user)
    return JSONResponse(status_code=200, content=update_user)