
# from os import environ
# from motor.motor_asyncio import AsyncIOMotorClient

# class DataBase:
#     client: AsyncIOMotorClient = None
#     database_uri = environ.get("DATABASE_URI_TEST")
#     users_collection = None
#     address_collection = None
#     product_collection = None
#     cart_collection = None
#     order_items_collection = None
    
# db = DataBase()

# async def connect_db():
#     db.client = AsyncIOMotorClient(
#         db.database_uri,
#         maxPoolSize=10,
#         minPoolSize=10,
#         tls=False,
#         tlsAllowInvalidCertificates=True
#     )
#     db.users_collection = db.client.shopping_cart.users
#     db.address_collection = db.client.shopping_cart.address
#     db.product_collection = db.client.shopping_cart.products
#     db.cart_collection = db.client.shopping_cart.orders
#     db.order_items_collection = db.client.shopping_cart.order_items

# async def disconnect_db():
#     db.client.close()

from os import environ
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

class Database():
    def __init__(self):
        self.client = MongoClient(environ.get('DATABASE_URI'))
        self.db = self.client['shopping_cart']
        self.users_collection = self.db['users']
        self.product_collection = self.db['product']
        self.address_collection = self.db['address']
        self.cart_collection = self.db['cart']
        self.order_items_collection = self.db['order_items']

db = Database()