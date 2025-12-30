from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from config import WATCH_DIRECTORIES
from response.responder import alert

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        alert(f"File created: {event.src_path}")

    def on_modified(self, event):
        alert(f"File modified: {event.src_path}")

def monitor_files():
    alert("File monitor started")

    observer = Observer()
    handler = Handler()

    for path in WATCH_DIRECTORIES:
        observer.schedule(handler, path, recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
