import pyshark
from realtime.feature_extractor import extract
from realtime.inference import detect
from realtime.alert_manager import send_alert

def start_capture():
    capture = pyshark.LiveCapture(interface="Wi-Fi")

    for packet in capture.sniff_continuously():

        # ✅ skip packets without IP layer
        try:
            ip = packet.ip.src
        except AttributeError:
            continue

        features = extract(packet)

        if features:
            result = detect(features, ip)

            print("RESULT:", result)

            send_alert(result)

start_capture() 