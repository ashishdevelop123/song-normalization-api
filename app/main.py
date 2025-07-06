from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Song API")

app.include_router(router)
