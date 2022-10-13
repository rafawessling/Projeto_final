from fastapi.exceptions import HTTPException
from bson import ObjectId, json_util
import json
import logging
from schemas.cart_schema import CartSchema
from server.database import db
from schemas.order_items_schema import OrderItemsSchema

logger = logging.getLogger(__name__)

async def create_cart(cart: CartSchema):
    """ Método responsável por criar um carrinho para o usuário

    `Args`:
        cart (CartSchema)
    `Raises`:
        HTTPException: status_code=422
    `Returns`:
        type: dict("status": status, "cart": cart)
    """
    try:
        
        cart = cart.dict()
        cart['user_id'] = ObjectId(cart['user_id'])
        
        #Verifica se o usuário já possui carrinho
        cart_existing = await get_cart_by_user(cart["user_id"])
        
        # Se o usuário não possui carrinho, verifica se o código do produto informado existe no banco de dados
        if 'result' in cart_existing.keys():
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

async def add_product(order_item):
    ''' Método que adiciona produto no carrinho
    
        `Args`:
        order_item: dict
    `Raises`:
        HTTPException: status_code=422
    `Returns`:
        type: dict("status": status, "order_item": order_item)
    '''
    try:
        product = db.product_collection.find_one({"code":order_item.product_code})
        order_item.cartId = ObjectId(order_item.cartId) 
        cart = db.cart_collection.find_one({'_id': order_item.cartId})
        if cart:
            db.order_item_collection.insert_one(order_item.dict())
            db.cart_collection.update_one({"_id":order_item.cartId}, {'$inc':{"total_price": product["price"] * order_item.quantity}})
            
            return db.cart_collection.find_one(order_item.cartId)
        return {'result': f'Carrinho nao foi encontrado!'}
    except Exception as e:
        logger.exception(f'add_product.error: {e}')
        raise HTTPException(status_code=422)

async def get_all_products(cartId):
    ''' Busca lista de produtos vínculados ao usuário pelo id do carrinho

    `Args`:
        userId: object
    `Raises`:
        HTTPException: status_code=422
    `Returns`:
        `type`: list("status": status, "product": product)
        obs: caso o usuário não tenha nenhum endereço vinculado, retorna-se uma lista vazia'''
    try:
        
        order_item_cursor = db.order_item_collection.find({"cartId": cartId})
        
        order_items =  list(order_item_cursor)
        lista = [OrderItemsSchema.parse_obj(o) for o in order_items]
        return lista
    except Exception as e:
        logger.exception(f'get_address.error: {e}')
        raise HTTPException(status_code=422)
    
async def remove_product(order_item):
    ''' Método que deleta produto do carrinho
    
        `Args`:
        order_item: dict
    `Raises`:
        HTTPException: status_code=422
    `Returns`:
        type: dict("status": status, "order_item": order_item)
    '''
    try:
        product = db.product_collection.find_one({"code":order_item.product_code})
        cartId = ObjectId(order_item.cartId)
        order_item_banco = await get_order_item(order_item.product_code, cartId)
        db.order_item_collection.delete_one({'product_code':product['code'], 'cartId':cartId})
        db.cart_collection.update_one({"_id":cartId}, {'$inc':{"total_price": -(product["price"] * order_item_banco['quantity'])}})
        
        
        return db.cart_collection.find_one(cartId)
    except Exception as e:
        logger.exception(f'remove_product.error: {e}')
        raise HTTPException(status_code=422)
    
async def get_order_item(code, cartId):
    ''' Busca order_item
    
        `Args`:
        order_item: dict
        code: int
    `Raises`:
        HTTPException: status_code=422
    `Returns`:
        type: dict("status": status, "order_item": order_item)
    '''
    try:
        product = db.order_item_collection.find_one({"product_code":code, 'cartId': cartId})
             
        return product
    except Exception as e:
        logger.exception(f'get_order_item.error: {e}')
        raise HTTPException(status_code=422)   

async def get_cart_by_user(user_id):
    """ Obtêm um carrinho baseado no id do usuário
    
    `Args`:
        user_id: object
    `Raises`:
        HTTPException: status_code=400
    `Returns`:
        type: dict("status": status, "product": product)
        obs: product somente é retornado se o elemento for encontrado,
             caso contrário, apenas o status informando a ausência será
             retornado
    """
    try:
        # Verifica se o usuário pesquisado possui carrinho vinculado a ele
        cart = db.cart_collection.find_one({"user_id": user_id})
        if cart:
            return cart
        else:
            return {'result': f'Carrinho com {user_id} nao foi encontrado!'}
    except Exception as e:
        logger.exception(f'get_cart_by_user.error: {e}')
        raise HTTPException(status_code=400)


async def delete_cart_user(user_id):
    """ Deleta um carrinho baseado no parâmetro `user_id` como chave de busca

        `Args`:
            user_id: object
        `Raises`:
            HTTPException: status_code=422
        `Returns`:
            type: dict("status": status, "cart": cart)
    """
    try:
        # Verifica se o usuário possui carrinho vinculado a ele
        cart = await get_cart_by_user(user_id)
        
        # Caso possua, deleta o carrinho existente
        if 'result' not in cart.keys():
            db.order_item_collection.delete_many({'cartId':cart['_id']})
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