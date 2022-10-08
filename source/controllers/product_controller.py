from fastapi.exceptions import HTTPException
from bson import ObjectId, json_util
import json
import logging
from source.schemas.product_schema import ProductSchema, ProductUpdateSchema
from source.server.database import db

logger = logging.getLogger(__name__)

async def create_product(product: ProductSchema):
    try:
        # Verifica se o código já existe
        existing_product = await get_product_by_code(product.code)

        # Se nenhum produto com o código informado for encontrado, ele é cadastrado
        if 'status' in existing_product.keys():
            add_product = db.product_db.insert_one(product.dict())
            
            # Verifica se o produto foi inserido corretamente
            if add_product.inserted_id:
                return {
                    "status":"Product has been created",
                    "product": product.dict()
                }
        return {"status": "Product already exists"}
    except Exception as e:
        logger.exception(f'create_product.error: {e}')
        raise HTTPException(status_code=422)

async def get_product_by_name(name):
    try:
        query = {
            "name": {
                "$regex": name,
                "$options": "i"
            }
        }
        # Verifica se algum produto possui o termo pesquisado no campo "name"
        products = list(db.product_db.find(query))
        if products:
            return json.loads(json_util.dumps(products))
        
        return {'status': 'No products found'}
    except Exception as e:
        logger.exception(f'get_product_by_name.error: {e}')
        raise HTTPException(status_code=400)
    
async def get_product_by_code(code):
    try:
        # Verifica se existe produto com o código pesquisado
        product = db.product_db.find_one({'code': code})
        if product:
            return json.loads(json_util.dumps(product))
        
        return {'status': 'Product not found'}
    except Exception as e:
        logger.exception(f'get_product_by_code.error: {e}')
        raise HTTPException(status_code=400)

async def delete_product_by_code(code):
    try:
        # Verifica se o código já existe
        existing_product = await get_product_by_code(code)
 
        # Verifica se o existe, e então deleta produto
        if 'status' not in existing_product.keys():
            delete_product = db.product_db.delete_one({"_id": ObjectId(existing_product["_id"]["$oid"])})
            
            # Verifica se o produto foi deletado corretamente
            if delete_product.deleted_count:
                return {'status': 'Deleted product'}
            
        return {"status": "Product not found"}
    except Exception as e:
        logger.exception(f'delete_product_by_code.error: {e}')
        raise HTTPException(status_code=400)

async def update_product_by_code(code, product: ProductUpdateSchema):
    try:
        # Verifica se o código já existe
        existing_product = await get_product_by_code(code)
        
        # Caso o produto exista, atualiza os dados informados (se forem diferentes dos existentes)
        if existing_product:
            product = {k: v for k, v in product if v is not None}
            update_product = db.product_db.update_one(
                {'code': code},
                {'$set': product}
            )
            
            # Verifica se o produto foi atualizado corretamente
            if update_product.modified_count:
                return {'status': 'Updated product'}

        return {'status': 'Product could not be updated'}
    except Exception as e:
        logger.exception(f'update_product_by_code.error: {e}')
        raise HTTPException(status_code=400)
