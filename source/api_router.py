from fastapi import APIRouter
from routes import address_route, user_route

router = APIRouter()

router.include_router(address_route.router)
router.include_router(user_route.router)