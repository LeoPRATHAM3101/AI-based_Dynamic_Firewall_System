from scapy.all import sniff, IP
import joblib
import numpy as np
import pandas as pd
from firewall import block_ip

# Load trained ML model
model = joblib.load('model.pkl')


# -------------------------------
# Feature Extraction
# -------------------------------
def extract_features(packet):
    try:
        packet_size = len(packet)

        # Basic protocol encoding
        protocol = 0
        if packet.haslayer(IP):
            proto = packet[IP].proto
            if proto == 6:   # TCP
                protocol = 1
            elif proto == 17:  # UDP
                protocol = 2
            elif proto == 1:   # ICMP
                protocol = 3

        flag = 0  # placeholder (can improve later)

        features = [packet_size, protocol, flag]

        # Convert to numpy array
        features = np.array(features, dtype=float)

        # Avoid NaN issues
        if np.isnan(features).any():
            return None

        return features

    except Exception as e:
        print(f"⚠️ Feature error: {e}")
        return None


# -------------------------------
# Packet Processing
# -------------------------------
def process_packet(packet):
    try:
        if not packet.haslayer(IP):
            return

        src_ip = packet[IP].src

        # Ignore invalid IP
        if src_ip == "0.0.0.0":
            return

        print(f"📦 Packet from {src_ip}")

        features = extract_features(packet)

        if features is None:
            return

        # Convert to DataFrame (fix sklearn warning)
        df = pd.DataFrame([features], columns=['packet_size', 'protocol', 'flag'])

        prediction = model.predict(df)[0]

        if prediction == 1:
            print(f"🚨 Attack detected from {src_ip}")
            block_ip(src_ip)
        else:
            print(f"✅ Normal traffic from {src_ip}")

    except Exception as e:
        print(f"❌ Error processing packet: {e}")


# -------------------------------
# Start Sniffing
# -------------------------------
print("🚀 Starting packet sniffing...")

# Only capture IP traffic (important)
sniff(filter="ip", prn=process_packet, store=0)

