import psutil
import time
from config import SUSPICIOUS_PROCESSES
from response.responder import alert

def monitor_processes():
    alert("Process monitor started")

    while True:
        try:
            for proc in psutil.process_iter(['pid', 'name']):
                name = proc.info.get("name")
                if not name:
                    continue

                for bad in SUSPICIOUS_PROCESSES:
                    if bad in name.lower():
                        alert(f"Suspicious process: {name} (PID {proc.info['pid']})")

            time.sleep(5)

        except Exception as e:
            alert(f"Process monitor error: {e}")
