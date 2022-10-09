from source.server.database import DataBase
from schemas.address_schema import Address

async def create_address(address):
    try:
        db = DataBase()
        await db.connect_db()
        if isinstance(address, dict):
            address_awaited = await db.address_collection.insert_one(address)
            return address_awaited.inserted_id
        else:
            address_awaited = await db.address_collection.insert_one(address.dict())
        return Address.parse_obj(await get_address(address_awaited.inserted_id))
    except Exception as e:
        print(f'create_address.error: {e}')

async def get_address(id):
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

async def get_all_addresses():
    try:
        db = DataBase()
        await db.connect_db()
        # address_cursor = db.address_collection.find({"userId": userId}).skip(int(skip)).limit(int(limit))
        address_cursor = db.address_collection.find()
        address_count = await db.address_collection.count_documents(filter={})
        address = await address_cursor.to_list(length = address_count)
        lista = [Address.parse_obj(a) for a in address]
        return lista
    except Exception as e:
        print(f'get_address.error: {e}')
        
async def delete_address(id):
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
