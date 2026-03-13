from fastapi import APIRouter

router=APIRouter()

alerts=[]

@router.get("/alerts")

def get_alerts():

    return alerts


@router.post("/alert")

def add_alert(alert:dict):

    alerts.append(alert)

    return {"status":"ok"}