import requests
import datetime

API = "http://127.0.0.1:8000/alert"

def send_alert(result):
    payload = {
        "timestamp": str(datetime.datetime.now()),
        "type": result["risk_level"],
        "data": result
    }

    # 🔥 send everything for local testing
    requests.post(API, json=payload)