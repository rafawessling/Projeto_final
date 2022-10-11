from fastapi.exceptions import HTTPException
from bson import json_util
import json
import logging
from source.controllers.product_controller import get_product_by_code
from source.schemas.cart_schema import CartSchema
from source.server.database import db

logger = logging.getLogger(__name__)

async def create_cart(cart: CartSchema):
    """ Método responsável por criar um carrinh para o usuário

    Args:
        cart (CartSchema)
    Raises:
        HTTPException: status_code=422
    Returns:
        type: dict("status": status, "cart": cart)
    """
    try:
        cart = cart.dict()
        #Verifica se o usuário já possui carrinho
        cart_existing = await get_cart_by_user(cart["user_id"])

        # Se o usuário não possui carrinho, verifica se o código do produto informato existe no banco de dados
        if not cart_existing:
            product_exist = await get_product_by_code(cart["order_items"][0]["product_code"])
            
            # Se o produto existe, cria carrinho com o produto informado
            if 'status' not in product_exist.keys():
                add_cart = db.cart_collection.insert_one(cart)
                
                # Verifica se o carrinho foi inserido corretamente
                if add_cart.inserted_id:
                    return {
                        "status":"Cart has been created",
                        "cart": json.loads(json_util.dumps(cart))
                    }
        return {"status": "Error to create cart"}
    except Exception as e:
        logger.exception(f'create_cart.error: {e}')
        raise HTTPException(status_code=422)

async def get_cart_by_user(user_id: str):
    """ Obtêm um carrinho baseado no id do usuário
    Args:
        user_id: str
    Raises:
        HTTPException: status_code=400
    Returns:
        type: dict("status": status, "product": product)
        obs: product somente é retornado se o elemento for encontrado,
             caso contrário, apenas o status informando a ausência será
             retornado
    """
    try:
        # Verifica se o usuário pesquisado possui carrinho vinculado a ele
        cart = db.cart_collection.find_one({"user_id": user_id})
        if cart:
            return json.loads(json_util.dumps(cart))
        return None
    except Exception as e:
        logger.exception(f'get_cart_by_user.error: {e}')
        raise HTTPException(status_code=400)


async def delete_cart_user(user_id: str):
    """ Deleta um carrinho baseado no parâmetro `user_id` como chave de busca

        Args:
            user_id: int
        Raises:
            HTTPException: status_code=400
        Returns:
            type: dict("status": status, "cart": cart)
    """
    try:
        # Verifica se o usuário possui carrinho vinculado a ele
        cart = await get_cart_by_user(user_id)
        
        # Caso possua, deleta o carrinho existente
        if cart:
            deleted_cart = db.cart_collection.delete_one({"user_id": user_id})
            
            # Verifica se o carrinho foi deletado corretamente
            if deleted_cart.deleted_count:
                return {
                    "status":"Cart has been deleted",
                    "cart": cart
                }
        return {"status": "It was not possible to delete the cart"}
    except Exception as e:
        logger.exception(f'delete_cart_user.error: {e}')
        raise HTTPException(status_code=422)