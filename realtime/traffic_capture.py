import pyshark
from realtime.feature_extractor import extract
from realtime.inference import detect
from realtime.alert_manager import send_alert

def start_capture():

    # Capture live packets from network interface
    capture=pyshark.LiveCapture(interface="Wi-Fi")

    # Continuously monitor network traffic
    for packet in capture.sniff_continuously():

        # Convert packet into feature vector
        features=extract(packet)

        if features:

            # Run anomaly detection
            result=detect(features)

            print("Packet processed: ",result)

            # If anomaly detected → send alert
            if result=="ANOMALY":

                send_alert("ANOMALY",features)

# Start packet capture process
start_capture()