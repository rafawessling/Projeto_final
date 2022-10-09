import re
from fastapi.exceptions import HTTPException
from source.schemas.user_schema import UserSchema
import logging
from source.server.database import db

logger = logging.getLogger(__name__)

async def create_user(email: UserSchema):
    if UserSchema.email == email:
        raise TypeError("E-mail já cadastrado.")
    else: 
        user = db.users_collection.insert_one(user.dict())
        return{
            "status": "Usuário cadastrado com suceso!",
            "usuario": user.dict()
        }

async def validate_email(email: UserSchema):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if len(email) < 3:
        raise TypeError("E-mail inválido!")
    if (re.search(regex, email)):
        return None
    else:
        return ("E-mail inválido!")

async def get_user_by_email(email: UserSchema):
    if UserSchema.email in db.users_collection:
        return UserSchema
    else:
        return("Usuário não encontrado!")