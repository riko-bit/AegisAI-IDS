import requests
import datetime

# Backend API endpoint where alerts will be sent
API="http://localhost:8000/alert"

def send_alert(type,data):

    # Prepare alert payload to send to backend
    payload={

        # Timestamp of when anomaly was detected
        "timestamp":str(datetime.datetime.now()),

        # Type of alert (e.g., ANOMALY)
        "type":type,

        # Data associated with the anomaly (feature vector)
        "data":str(data)

    }

    # Send alert to backend FastAPI server
    requests.post(API,json=payload)