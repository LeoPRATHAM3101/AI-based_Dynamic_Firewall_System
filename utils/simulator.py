import random
from utils.logger import log_attack

def simulate_attack():
    fake_ip = f"192.168.1.{random.randint(1,255)}"
    threat_score = random.randint(50, 100)

    log_attack(fake_ip, threat_score)

    return {
        "ip": fake_ip,
        "threat": threat_score
    }
