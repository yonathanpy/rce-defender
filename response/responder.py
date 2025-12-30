import datetime
from config import LOG_FILE

def alert(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"[{timestamp}] {message}"
    print(log)

    try:
        with open(LOG_FILE, "a") as f:
            f.write(log + "\n")
    except:
        print("Log write failed")
