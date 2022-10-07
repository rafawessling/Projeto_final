from fastapi import APIRouter
from routes import address_route

router = APIRouter()

router.include_router(address_route.router)