
from bson import ObjectId
from server.database import DataBase
from schemas.address_schema import Address

async def create_address(address):
    '''`função`: criar endereço\n`address`: novo endereço do usuário
    \n\nreturn1: retorna novo endereço inserido no banco de dados'''
    try:
        db = DataBase()
        await db.connect_db()
        user = await db.users_collection.find_one({'_id':ObjectId(address.userId)})
        print(user)
        if user == None:
            raise Exception(f'Usuario não encontrado: id: {address.userId}')
        
        address.userId = user['_id']
        address_awaited = await db.address_collection.insert_one(address.dict())
        return Address.parse_obj(await get_address(address_awaited.inserted_id))
    except Exception as e:
        print(f'create_address.error: {e}')

async def get_address(id):
    '''`função`: buscar o endereço do usuário no banco de dados pelo id\n`id`: id do usuário retirado do banco de dados
    \n\nreturn: endereço conectado ao id'''
    try:
        db = DataBase()
        await db.connect_db()
        data = await db.address_collection.find_one({"_id": id})
        if data:
            return Address.parse_obj(data)
        else:
            return {'result': f'Endereco {id} nao foi encontrado!'}
    except Exception as e:
        print(f'get_address.error: {e}')

async def get_all_addresses(userId):
    '''`função`: buscar `lista` de endereços vínculados ao usuário\n\nreturn: `lista` de endereços vículados ao usuário convertidos a dicionários'''
    try:
        db = DataBase()
        await db.connect_db()
        address_cursor = db.address_collection.find({"userId": userId})
        address_count = await db.address_collection.count_documents(filter={})
        address = await address_cursor.to_list(length = address_count)
        lista = [Address.parse_obj(a) for a in address]
        return lista
    except Exception as e:
        print(f'get_address.error: {e}')
        
async def delete_address(id):
    '''`função`: deletar endereço pelo id do endereço\n`id`: id do endereço
    \n\nreturn: mensagem de delete confirmado'''
    try:
        db = DataBase()
        await db.connect_db()
        result = await db.address_collection.delete_one({"_id": id})
        if result.deleted_count > 0:
            return {'status': 'address deleted'}
        else:
             return {'status': 'Nothing to delete'}
    except Exception as e:
        print(f'delete.error: {e}')
        
async def delete_all_address(userId):
    '''`função`: deletar todos os endereços pelo id do usuário\n`id`: id do usuário
    \n\nreturn: mensagem de delete confirmado'''
    try:
        db = DataBase()
        await db.connect_db()
        result = await db.address_collection.delete_many({"userId": userId})
        if result.deleted_count > 0:
            return {'status': 'addresses deleted'}
        else:
             return {'status': 'Nothing to delete'}
    except Exception as e:
        print(f'delete.error: {e}')
        
        
