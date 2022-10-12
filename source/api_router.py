from fastapi import APIRouter
from routes import cart_route, product_route, order_route,address_route, user_route

router = APIRouter()

router.include_router(address_route.router)
router.include_router(user_route.router)
router.include_router(product_route.router)
router.include_router(cart_route.router)
