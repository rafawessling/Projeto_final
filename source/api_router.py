from fastapi import APIRouter
from rotas import endereco_rota

router = APIRouter()

router.include_router(endereco_rota.router)