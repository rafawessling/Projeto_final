from fastapi import FastAPI
from pydantic import BaseModel
from api_router import router
from server.database import DataBase
import uvicorn
from dotenv import load_dotenv
from pathlib import Path

app = FastAPI()

app.include_router(router)
load_dotenv(Path('main.py').resolve().parents[1].joinpath('.env'))
db = DataBase()

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8005, log_level="info", reload=True)
    print("running")