
from fastapi import HTTPException
from server.database import Database
from schemas.user_schema import User
import logging

logger = logging.getLogger(__name__)

async def create_user(user):
    ''' Método responsável pela criação do usuário 

    `Args`:
        user: dict
    `Raises`:
        HTTPException: status_code=422
    `Returns`:
        `type`: dict("status": status, "user": user)
    '''
    try:
        db = Database()
        
        user_awaited = db.users_collection.insert_one(user.dict())
        return User.parse_obj(await get_user(user_awaited.inserted_id))
    except Exception as e:
        logger.exception(f'create_user.error: {repr(e)}')
        raise HTTPException(status_code=422)
        
async def get_user(id):
    ''' Busca usuário no banco de dados pelo id do usuário 

    `Args`:
        id: object
    `Raises`:
        HTTPException: status_code=400
    `Returns`:
        `type`: dict("status": status, "user": user)
        obs: caso não exista usuário com o id inserido, retorna-se uma mensagem de aviso'''
    try:
        db = Database()
        
        data =  db.users_collection.find_one({"_id": id})
        if data:
            return User.parse_obj(data)
        else:
            return {'result': f'Usuario {id} nao foi encontrado!'}
    except Exception as e:
        logger.exception(f'get_user.error: {e}')
        raise HTTPException(status_code=400)

async def get_users():
    ''' Busca lista de usuários no banco de dados

    `Raises`:
        HTTPException: status_code=400
    `Returns`:
        `type`: list("status": status, "user": user)
        obs: caso não tenha nenhum usuário no bando de dados, retorna-se uma lista vazia'''
    try:
        db = Database()
        
        user_cursor = db.users_collection.find()
        users = list(user_cursor)
        lista = [User.parse_obj(u) for u in users]
        return lista
    except Exception as e:
        logger.exception(f'get_users.error: {e}')
        raise HTTPException(status_code=400)
        
async def get_user_by_email(email):
    ''' Busca usuário pelo email do usuário 

    `Args`:
        email: Emailstr
    `Raises`:
        HTTPException: status_code=400
    `Returns`:
        `type`: dict("status": status, "user": user)
    '''
    db = Database()
    try:
        user = db.users_collection.find_one({'email': email})
        if user:
            return User.parse_obj(user)
        else:
            return {'result': f'Usuario com email {email} nao foi encontrado!'}
    except Exception as e:
        logger.exception(f'get_user_by_email.error: {e}')
        raise HTTPException(status_code=400)
    
async def update_user(user_id, user_data):
    ''' Atualiza dados do usuário no banco de dados  

    `Args`:
        user_id: object
        user_data: dict
    `Raises`:
        HTTPException: status_code=422
    `Returns`:
        `type`: bool, int("status": status, "user": user)
        obs: caso nenhum dado tenha sido atualizado,
        retorna-se o bool false e o int 0, indicando que nenhum dado foi modificado'''
    try: 
        db = Database()
        
        
        filtro = {"_id":user_id}
        new_values = { "$set": user_data.dict() }
        
        user = db.users_collection.update_one(filtro, new_values)
        if user.modified_count:
            return {'result' : True, 'modified_count' : user.modified_count}
        return {'result' : False, 'modified_count' : 0}
    except Exception as e:
        logger.exception(f'update_user.error: {e}')
        raise HTTPException(status_code=422)
        
async def delete_user(user_id):
    '''Deleta o usuário do banco de dados pelo id do usuário  

    `Args`:
        user_id: object
    `Raises`:
        HTTPException: status_code=422
    `Returns`:
        `type`: str("status": status, "user": user)
        obs: caso não haja usuário com id inserido, retorna-se uma mensagem de aviso'''
    try:
        db = Database()
        
        user = db.users_collection.delete_one({'_id': user_id})
        if user.deleted_count > 0:
            return {'status': 'User deleted'}
        else:
            return {'status': 'Nothing to delete'}
    except Exception as e:
        logger.exception(f'delete_user.error: {e}')
        raise HTTPException(status_code=422)
    

    