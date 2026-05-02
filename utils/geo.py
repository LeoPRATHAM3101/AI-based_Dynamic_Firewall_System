import requests

def get_ip_location(ip):
    try:
        # Free public API (no key required)
        url = f"http://ip-api.com/json/{ip}"

        response = requests.get(url, timeout=5)
        data = response.json()

        if data["status"] == "success":
            return {
                "ip": ip,
                "country": data.get("country", "Unknown"),
                "region": data.get("regionName", "Unknown"),
                "city": data.get("city", "Unknown"),
                "lat": data.get("lat", 0),
                "lon": data.get("lon", 0),
                "isp": data.get("isp", "Unknown")
            }
        else:
            return fallback(ip)

    except Exception as e:
        print(f"Geo error: {e}")
        return fallback(ip)


# Fallback if API fails (VERY IMPORTANT)
def fallback(ip):
    return {
        "ip": ip,
        "country": "Unknown",
        "region": "Unknown",
        "city": "Unknown",
        "lat": 20.5937,   # Default: India center
        "lon": 78.9629,
        "isp": "Unknown"
    }
