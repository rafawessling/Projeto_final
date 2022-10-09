from server.database import DataBase
from schemas.user_schema import User
from controllers.address_controler import create_address

async def create_user(user):
    try:
        db = DataBase()
        await db.connect_db()
        user_awaited = await db.users_collection.insert_one(user.dict())
        return User.parse_obj(await get_user(user_awaited.inserted_id))
    except Exception as e:
        print(f'create_user.error: {repr(e)}')
        
async def get_user(id):
    try:
        db = DataBase()
        await db.connect_db()
        data = await db.users_collection.find_one({"_id": id})
        if data:
            return User.parse_obj(data)
        else:
            return {'result': f'Usuario {id} nao foi encontrado!'}
    except Exception as e:
        print(f'get_user.error: {e}')

async def get_users():
    try:
        db = DataBase()
        await db.connect_db()
        user_cursor = db.users_collection.find()
        user_count = await db.users_collection.count_documents(filter={})
        users = await user_cursor.to_list(length=user_count)
        lista = [User.parse_obj(u) for u in users]
        return lista
    except Exception as e:
        print(f'get_users.error: {e}')
        
async def get_user_by_email(email):
    db = DataBase()
    await db.connect_db()
    user = await db.users_collection.find_one({'email': email})
    if user:
        return User.parse_obj(user)
    else:
        return {'result': f'Usuario com email {email} nao foi encontrado!'}

async def update_user(user_id, user_data):
    '''`user_id`: Id do usuario\n`user_data:` Lista de Tuplas List[(x,y)]
    \n\nReturns: `dict`'''
    try:
        
        db = DataBase()
        await db.connect_db()
        
        filtro = {"_id":user_id}
        new_values = { "$set": user_data.dict() }
        
        user = await db.users_collection.update_one(filtro, new_values)
        if user.modified_count:
            return {'result' : True, 'modified_count' : user.modified_count}
        return {'result' : False, 'modified_count' : 0}
    
    except Exception as e:
        print(f'update_user.error: {e}')
        
async def delete_user(user_id):
    try:
        db = DataBase()
        await db.connect_db()
        user = await db.users_collection.delete_one({'_id': user_id})
        if user.deleted_count > 0:
            return {'status': 'User deleted'}
        else:
            return {'status': 'Nothing to delete'}
    except Exception as e:
        print(f'delete_user.error: {e}')