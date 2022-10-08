from fastapi import APIRouter
from source.routes import product_route

router = APIRouter()

# router.include_router(address_route.router)
router.include_router(product_route.router)

