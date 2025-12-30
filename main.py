import threading
from monitors.process_monitor import monitor_processes
from monitors.network_monitor import monitor_network
from monitors.file_monitor import monitor_files

print("Starting RCE Defender...")

threading.Thread(target=monitor_processes, daemon=True).start()
threading.Thread(target=monitor_network, daemon=True).start()
threading.Thread(target=monitor_files, daemon=True).start()

while True:
    pass
