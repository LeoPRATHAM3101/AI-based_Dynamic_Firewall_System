import json
from datetime import datetime
from utils.geo import get_ip_location

LOG_FILE = "logs.json"


def log_attack(ip, threat_score):
    # Get geo info
    geo = get_ip_location(ip)

    # Create full log entry
    log_entry = {
        "ip": ip,
        "time": str(datetime.now()),
        "threat_score": threat_score,
        "country": geo["country"],
        "region": geo["region"],
        "city": geo["city"],
        "lat": geo["lat"],
        "lon": geo["lon"],
        "isp": geo["isp"]
    }

    # Load existing logs safely
    try:
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    # Append new log
    data.append(log_entry)

    # Save back to file
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)
