
from bson import ObjectId
from server.database import Database
from schemas.order_items_schema import OrderItemsSchema
import logging
from fastapi.exceptions import HTTPException

from schemas.order_schema import OrderSchema
from controllers.cart_controller import get_all_products
from controllers.cart_controller import delete_cart_user

logger = logging.getLogger(__name__)

async def create_order(order:OrderSchema):
    ''' Método que cria o order
    
        `Args`:
        order: (OrderSchema)
    `Raises`:
        HTTPException: status_code=422
    `Returns`:
        type: dict("status": status, "order": order)
    '''
    try:
        db = Database()
        
        address = db.address_collection.find_one({'_id': ObjectId(order.addressId)})
        cart = db.cart_collection.find_one({'user_id': ObjectId(order.userId)})
        order.order_item = await get_all_products(cart['_id'])
        order.price = cart['total_price']
        order.addressId = address
        
        order_awaited = db.order_collection.insert_one(order.dict())
        if order_awaited.inserted_id:
            await delete_cart_user(cart['user_id'])
            return OrderSchema.parse_obj(await get_order(order_awaited.inserted_id))
        
    except Exception as e:
        logger.exception(f'create_order.error: {e}')
        raise HTTPException(status_code=422)
    
    
async def get_order(id):
    ''' Busca order com o seu id
    
        `Args`:
        id: object
    `Raises`:
        HTTPException: status_code=400
    `Returns`:
        type: dict("status": status, "order": order)
    '''
    try:
        db = Database()
        
        data = db.order_collection.find_one({"_id": id})
        if data:
            return OrderSchema.parse_obj(data)
        else:
            return {'result': f'Order {id} nao foi encontrado!'}
    except Exception as e:
        logger.exception(f'get_order.error: {e}')
        raise HTTPException(status_code=400)
