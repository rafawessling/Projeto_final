from os import environ
from motor.motor_asyncio import AsyncIOMotorClient

class DataBase:
    
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = None
        self.database_uri = environ.get("DATABASE_URI_TESTE")
        self.users_collection = None
        self.address_collection = None
        self.product_collection = None
        self.cart_collection = None
        self.order_items_collection = None
    
    async def connect_db(self):
        self.client = AsyncIOMotorClient(
            self.database_uri,
            maxPoolSize=10,
            minPoolSize=10,
            tls=False,
            tlsAllowInvalidCertificates=True
        )
        self.users_collection = self.client.shopping_cart.users
        self.address_collection = self.client.shopping_cart.address
        self.product_collection = self.client.shopping_cart.products
        self.cart_collection = self.client.shopping_cart.orders
        self.order_items_collection = self.client.shopping_cart.order_items

    async def disconnect_db(self):
        self.client.close()