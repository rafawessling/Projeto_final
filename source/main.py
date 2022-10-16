import sys
import pydantic
import uvicorn

# Adicionado o diretório source em PYTHONPATH
sys.path.append("source")

from bson import ObjectId
from fastapi import FastAPI
from api_router import router
from dotenv import load_dotenv
from pathlib import Path


app = FastAPI(title= "Shopping Cart - Cleaning")

pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str

app.include_router(router)
load_dotenv(Path('main.py').resolve().parents[1].joinpath('.env'))

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8005, log_level="info", reload=True)
    print("running")