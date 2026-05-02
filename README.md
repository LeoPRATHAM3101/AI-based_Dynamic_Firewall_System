Here’s a **clean, professional, placement-ready `README.md`** for your project 👇

---

# 🚀 AI-Powered Dynamic Firewall System

An intelligent, real-time firewall system that uses **Machine Learning + Packet Sniffing** to detect and block malicious traffic automatically.
This project combines **Cybersecurity + AI + Web Dashboard** into a powerful, portfolio-ready system.

---

## 🔥 Features

### 🧠 AI-Based Threat Detection

* Uses a trained ML model (`RandomForestClassifier`)
* Classifies traffic as **Normal / Malicious**
* Real-time decision making

### 📡 Packet Sniffing

* Captures live network traffic using Python
* Extracts key packet features (IP, protocol, size)

### 🚫 Automatic IP Blocking

* Blocks malicious IPs using macOS PF firewall
* Prevents repeated attacks dynamically

### 📊 Advanced Dashboard

* Beautiful UI with:

  * 📈 Charts (Chart.js)
  * 🌍 Attack Map (Leaflet.js)
  * 📊 Threat statistics
* Real-time updates

### 🔐 Authentication System

* Secure login system
* Password hashing (no plain text)
* Session-based authentication

### 📁 Logging System (Secure)

* JSON-based logs (no unsafe `eval`)
* Stores:

  * IP address
  * Timestamp
  * Threat score
  * Location (optional)

### 🎯 Threat Scoring

* Each IP assigned a severity level:

  * 🟢 Low
  * 🟡 Medium
  * 🔴 High

---

## 🧱 Project Structure

```
dynamic-firewall/
│
├── app.py                 # Main Flask app
├── firewall.py            # IP blocking logic
├── packet_sniffer.py      # Network packet capture
├── train_model.py         # ML model training
├── model.pkl              # Trained model
│
├── users.json             # User credentials (hashed)
├── logs.json              # Structured logs
├── logs.txt               # Raw logs
│
├── utils/
│   ├── auth.py            # Authentication logic
│   ├── logger.py          # Logging system
│   └── geo.py             # IP geolocation
│
├── templates/
│   ├── index.html         # Login page
│   ├── dashboard.html     # Main dashboard UI
│
├── static/
│   ├── css/
│   ├── js/
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/dynamic-firewall.git
cd dynamic-firewall
```

---

### 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Train the ML model

```bash
python3 train_model.py
```

---

### 5️⃣ Create Admin User

```bash
python3 -c "from utils.auth import register_user; register_user('admin','admin123')"
```

---

### 6️⃣ Run the Application

```bash
python3 app.py
```

---

### 🌐 Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔑 Default Login

| Username | Password |
| -------- | -------- |
| admin    | admin123 |

---

## 📊 Dashboard Preview

* 📈 Live traffic charts
* 🌍 Attack origin map
* 📊 IP-wise stats
* 🚨 Threat alerts

---

## 🧪 Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn
* **Frontend:** HTML, CSS, JS
* **Charts:** Chart.js
* **Map:** Leaflet.js
* **Packet Sniffing:** Scapy
* **Firewall:** macOS PF

---

## 🔐 Security Highlights

* Password hashing (secure storage)
* JSON logging (no unsafe parsing)
* Session authentication
* Duplicate IP blocking prevention

---

## 🚀 Future Enhancements

### 🟡 High Value

* JWT Authentication
* Real-time WebSockets
* CSV/JSON log export
* Alert system (sound + popup)

### 🟢 Next Level

* Deep Learning model
* Cloud deployment (AWS / Render)
* Admin control panel
* Auto attack simulation
* Threat intelligence API integration

---

## ☁️ Deployment

You can deploy this project on:

* Render
* AWS EC2
* Railway

---

## 📌 Use Cases

* Cybersecurity learning
* Network monitoring systems
* Intrusion Detection System (IDS)
* Portfolio / Resume project

---
## 👨‍💻 Author
**Pratham Joshi**
BCA Student |
Cybersecurity Enthusiast
---
