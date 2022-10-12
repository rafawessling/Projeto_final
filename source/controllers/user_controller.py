
from server.database import Database
from schemas.user_schema import User

async def create_user(user):
    '''`função`: criar usuário\n`user`: dados do usuário
    \n\nreturn: usuário convertido a `dict`'''
    try:
        db = Database()
        
        user_awaited = db.users_collection.insert_one(user.dict())
        return User.parse_obj(await get_user(user_awaited.inserted_id))
    except Exception as e:
        print(f'create_user.error: {repr(e)}')
        
async def get_user(id):
    '''`função`: buscar usuário no banco de dados\n`id`: id do usuário
    \n\nreturn: dados do usuário'''
    try:
        db = Database()
        
        data =  db.users_collection.find_one({"_id": id})
        if data:
            return User.parse_obj(data)
        else:
            return {'result': f'Usuario {id} nao foi encontrado!'}
    except Exception as e:
        print(f'get_user.error: {e}')

async def get_users():
    '''`função`: buscar usuários\n\nreturn: `lista` de usuários com dados convertidos a dicionarios'''
    try:
        db = Database()
        
        user_cursor = db.users_collection.find()
        users = list(user_cursor)
        lista = [User.parse_obj(u) for u in users]
        return lista
    except Exception as e:
        print(f'get_users.error: {e}')
        
async def get_user_by_email(email):
    '''`função`: buscar usuário pelo email\n`email`: email do usuário
    \n\nreturn: usuáro vínculado ao email'''
    db = Database()
    
    user = db.users_collection.find_one({'email': email})
    if user:
        return User.parse_obj(user)
    else:
        return {'result': f'Usuario com email {email} nao foi encontrado!'}

async def update_user(user_id, user_data):
    '''`função`: atualizar dados do usuário\n`user_id`: Id do usuario\n`user_data`: dados do usuário 
    \n\nReturns: `dict` com dados atualizados'''
    try: 
        db = Database()
        
        
        filtro = {"_id":user_id}
        new_values = { "$set": user_data.dict() }
        
        user = db.users_collection.update_one(filtro, new_values)
        if user.modified_count:
            return {'result' : True, 'modified_count' : user.modified_count}
        return {'result' : False, 'modified_count' : 0}
    except Exception as e:
        print(f'update_user.error: {e}')
        
async def delete_user(user_id):
    '''`função`: deletar usuário\n`user_id`: id do usuário
    \n\nreturn: mensagem de delete confirmado'''
    try:
        db = Database()
        
        user = db.users_collection.delete_one({'_id': user_id})
        if user.deleted_count > 0:
            return {'status': 'User deleted'}
        else:
            return {'status': 'Nothing to delete'}
    except Exception as e:
        print(f'delete_user.error: {e}')
    

    