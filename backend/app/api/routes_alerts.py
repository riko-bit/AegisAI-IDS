from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict, Any

router = APIRouter()

alerts: List[Dict[str, Any]] = []

class Alert(BaseModel):
    timestamp: str
    type: str
    data: Dict[str, Any]

@router.post("/alert")
def add_alert(alert: Alert):
    alerts.append(alert.dict())

    # prevent infinite growth
    if len(alerts) > 200:
        alerts.pop(0)

    return {"status": "ok"}

@router.get("/alerts")
def get_alerts():
    return alerts[-50:]