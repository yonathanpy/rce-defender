import psutil
import time
from config import SUSPICIOUS_PORTS
from response.responder import alert

def monitor_network():
    alert("Network monitor started")

    while True:
        try:
            for conn in psutil.net_connections(kind='inet'):
                if conn.raddr and conn.raddr.port in SUSPICIOUS_PORTS:
                    alert(f"Suspicious connection to port {conn.raddr.port}")

            time.sleep(5)

        except Exception as e:
            alert(f"Network monitor error: {e}")
