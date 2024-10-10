import uuid
import json

USER_DATA_FILE = "user_data.json"


# DID generation
def generate_did():
    did = f"did:ic:{uuid.uuid4()}"
    return did


# Session handling
user_sessions = {}


def create_session(user_did: str, session_data: str):
    user_sessions[user_did] = session_data
    return True


def get_session(user_did: str):
    return user_sessions.get(user_did, "No active session")


# User management (temporary storage in JSON file)
def load_users():
    try:
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(users, f)


def create_user(user_data):
    users = load_users()
    if any(user['email'] == user_data['email'] for user in users):
        raise ValueError("User already exists")

    users.append(user_data)
    save_users(users)


def authenticate_user(email, password):
    users = load_users()
    for user in users:
        if (user["email"] == email or user["username"] == email) and user["password"] == password:
            return user
    return None
