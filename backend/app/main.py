from fastapi import FastAPI
from backend.app.api.routes_alerts import router

app=FastAPI()

app.include_router(router)