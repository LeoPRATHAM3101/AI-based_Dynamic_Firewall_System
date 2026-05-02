import json
from datetime import datetime

LOG_FILE = "logs.json"


def log_attack(ip, threat_score):
    log = {
        "ip": ip,
        "time": str(datetime.now()),
        "threat_score": threat_score
    }

    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(log)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)
