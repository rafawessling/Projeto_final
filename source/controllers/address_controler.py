import logging
from bson import ObjectId
from fastapi.exceptions import HTTPException
from server.database import Database
from schemas.address_schema import Address


logger = logging.getLogger(__name__)


async def create_address(address):
    ''' Método responsável pela criação do endereço do usuário

    `Args`:
        address: dict
    `Raises`:
        HTTPException: status_code=422
    `Returns`:
        `type`: dict("status": status, "address": address)
    '''
    try:
        db = Database()
        
        user = db.users_collection.find_one({'_id': ObjectId(address.userId)})
        if user == None:
            raise Exception(f'Usuario não encontrado: id: {address.userId}')
        
        address.userId = user['_id']
        address_awaited = db.address_collection.insert_one(address.dict())
        return Address.parse_obj(await get_address(address_awaited.inserted_id))
    except Exception as e:
        logger.exception(f'create_address.error: {e}')
        raise HTTPException(status_code=422)

async def get_address(id):
    ''' Busca endereço no banco de dados pelo id do endereço

    `Args`:
        id: object
    `Raises`:
        HTTPException: status_code=400
    `Returns`:
        `type`: dict("status": status, "address": address)
     obs: caso não exista endereço com o id inserido, retorna-se uma mensagem de aviso
    '''
    try:
        db = Database()
        
        data = db.address_collection.find_one({"_id": id})
        if data:
            return Address.parse_obj(data)
        else:
            return {'result': f'Endereco {id} nao foi encontrado!'}
    except Exception as e:
        logger.exception(f'get_address.error: {e}')
        raise HTTPException(status_code=400)

async def get_all_addresses(userId):
    ''' Busca lista de endereços vínculados ao usuário pelo id do usuário

    `Args`:
        userId: object
    `Raises`:
        HTTPException: status_code=400
    `Returns`:
        `type`: list("status": status, "product": product)
        obs: caso o usuário não tenha nenhum endereço vinculado, retorna-se uma lista vazia'''
    try:
        db = Database()
        
        address_cursor = db.address_collection.find({"userId": userId})
        address =  list(address_cursor)
        lista = [Address.parse_obj(a) for a in address]
        return lista
    except Exception as e:
        logger.exception(f'get_address.error: {e}')
        raise HTTPException(status_code=400)
        
async def delete_address(id):
    ''' Deleta endereço do banco de dados pelo id do endereço

    `Args`:
        id: object
    `Raises`:
        HTTPException: status_code=422
    `Returns`:
        `type`: str("status": status, "address": address)
        obs: caso não haja endereço a ser deletado, retorna-se uma mensagem de aviso'''
    try:
        db = Database()
        
        result =  db.address_collection.delete_one({"_id": id})
        if result.deleted_count > 0:
            return {'status': 'address deleted'}
        else:
             return {'status': 'Nothing to delete'}
    except Exception as e:
        logger.exception(f'delete.error: {e}')
        raise HTTPException(status_code=422)
        
async def delete_all_addresses(userId):
    ''' Deleta lista de endereços vínculados ao usuário pelo id do usuário

    `Args`:
        userId: object
    `Raises`:
        HTTPException: status_code=422
    `Returns`:
        `type`: str("status": status, "address": address)
        obs: caso não haja endereço a ser deletado, retorna-se uma mensagem de aviso'''
    try:
        db = Database()
        
        result =  db.address_collection.delete_many({"userId": userId})
        if result.deleted_count > 0:
            return {'status': 'addresses deleted'}
        else:
             return {'status': 'Nothing to delete'}
    except Exception as e:
        logger.exception(f'delete.error: {e}')
        raise HTTPException(status_code=422)
        
        
