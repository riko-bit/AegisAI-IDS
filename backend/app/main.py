from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.routes_alerts import router

app = FastAPI()

# 🔥 FIX: Enable CORS (required for dashboard)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend (localhost:5500)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)