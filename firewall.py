import os
from datetime import datetime

RULES_FILE = "/tmp/firewall_rules.conf"
LOG_FILE = "logs.txt"

BLOCKED_IPS = set()  # Prevent duplicate blocking


# -------------------------------
# Validation Functions
# -------------------------------
def is_valid_ip(ip):
    if ip is None or ip == "0.0.0.0":
        return False
    return True


def is_safe_ip(ip):
    """
    Prevent blocking:
    - Localhost
    - Private networks
    """
    return (
        ip.startswith("127.") or
        ip.startswith("192.168.") or
        ip.startswith("10.") or
        ip.startswith("172.")  # covers 172.16.x.x - 172.31.x.x
    )


# -------------------------------
# Core Firewall Logic
# -------------------------------
def block_ip(ip):
    try:
        # ❌ Skip invalid or safe IPs
        if not is_valid_ip(ip) or is_safe_ip(ip):
            return

        # ❌ Skip already blocked IPs (memory)
        if ip in BLOCKED_IPS:
            return

        # ❌ Skip if already in file (persistent check)
        if os.path.exists(RULES_FILE):
            with open(RULES_FILE, "r") as f:
                if ip in f.read():
                    return

        print(f"🚫 Blocking IP: {ip}")

        BLOCKED_IPS.add(ip)

        rule = f"block drop from {ip} to any\n"

        # Ensure rules file exists
        if not os.path.exists(RULES_FILE):
            with open(RULES_FILE, "w") as f:
                f.write("")

        # Append new rule
        with open(RULES_FILE, "a") as f:
            f.write(rule)

        # Reload PF firewall (macOS)
        os.system(f"sudo pfctl -f {RULES_FILE}")
        os.system("sudo pfctl -e")

        # Ensure log file exists
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w") as f:
                f.write("")

        # ✅ Log with timestamp
        with open(LOG_FILE, "a") as log:
            log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - 🚫 Blocked IP: {ip}\n")

        print(f"✅ IP {ip} blocked successfully")

    except Exception as e:
        print(f"❌ Error blocking IP: {e}")


# -------------------------------
# Debug / Utility
# -------------------------------
def show_blocked_ips():
    print("🔒 Blocked IPs (memory):")
    for ip in BLOCKED_IPS:
        print(ip)


def clear_firewall():
    """
    Reset firewall rules (for testing)
    """
    try:
        os.system("sudo pfctl -F all")
        os.system("sudo pfctl -d")

        if os.path.exists(RULES_FILE):
            os.remove(RULES_FILE)

        BLOCKED_IPS.clear()

        print("🧹 Firewall reset complete")

    except Exception as e:
        print(f"❌ Error clearing firewall: {e}")
