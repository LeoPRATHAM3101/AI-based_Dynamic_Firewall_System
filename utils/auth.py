import json
from werkzeug.security import generate_password_hash, check_password_hash

USERS_FILE = "users.json"


def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


def register_user(username, password):
    users = load_users()
    users[username] = generate_password_hash(password)
    save_users(users)


def validate_user(username, password):
    users = load_users()
    if username in users:
        return check_password_hash(users[username], password)
    return False

