from flask import Flask, render_template, request, redirect, session, jsonify
import json
from utils.auth import validate_user, register_user
from utils.simulator import simulate_attack

app = Flask(__name__)
app.secret_key = "supersecretkey"


# 🔐 LOGIN
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        if validate_user(user, pwd):
            session["user"] = user
            return redirect("/dashboard")

    return render_template("login.html")


# 🧠 DASHBOARD
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    return render_template("dashboard.html")


# 📊 FETCH LOGS
@app.route("/logs")
def get_logs():
    try:
        with open("logs.json") as f:
            data = json.load(f)
    except:
        data = []

    return jsonify(data)


# 🤖 SIMULATE ATTACK
@app.route("/simulate")
def simulate():
    data = simulate_attack()
    return jsonify(data)


# 📁 EXPORT LOGS
@app.route("/export")
def export_logs():
    return open("logs.json").read()


# 🚪 LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
