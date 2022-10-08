#import email
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from source.api_router import router
import uvicorn

app = FastAPI(title= "Shopping Cart - Cleaning")

app.include_router(router)

# if __name__ == '__main__':
#     uvicorn.run("main:app", host='127.0.0.1', port=8005, log_level="info", reload=True)
#     print("running")