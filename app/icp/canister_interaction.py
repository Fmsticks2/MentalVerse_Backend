import requests

CANISTER_ID = "amwkh-wyaaa-aaaaj-azuaa-cai"  # Ensure this is correct
# https://a4gq6-oaaaa-aaaab-qaa4q-cai.raw.icp0.io/?id=amwkh-wyaaa-aaaaj-azuaa-cai


def call_icp_canister(method_name: str, payload: dict):
    canister_url = f"https://a4gq6-oaaaa-aaaab-qaa4q-cai.raw.icp0.io/?id={CANISTER_ID}"
    try:
        response = requests.post(canister_url, json={"method": method_name, "args": payload})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error calling canister: {e}")
        return {"error": str(e)}


# Get user's token balance
def get_user_balance(user: str):
    return call_icp_canister("get_balance", {"user": user})


# Create tokens for a user
def create_user_tokens(user: str, amount: int):
    return call_icp_canister("create_token", {"user": user, "amount": amount})
