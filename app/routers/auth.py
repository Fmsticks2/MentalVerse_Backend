from fastapi import APIRouter, HTTPException
from app.services.auth_service import generate_did, create_session, get_session, create_user, authenticate_user
from app.icp.canister_interaction import get_user_balance, create_user_tokens

router = APIRouter()


# Registration endpoint
@router.post("/auth/register")
async def register_user(first_name: str, last_name: str, username: str, email: str, password: str):
    try:
        # Create user in temporary storage (JSON file)
        create_user({
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password
        })

        # Give user some initial tokens
        create_user_tokens(email, 100)

        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Login endpoint
@router.post("/auth/login")
async def login_user(email: str, password: str):
    user = authenticate_user(email, password)

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"message": "Login successful", "user": user}


# DID generation endpoint
@router.get("/wallet/did")
async def generate_did_route():
    did = generate_did()
    return {"status": "DID generated", "did": did}


# Session creation endpoint
@router.post("/session/create")
async def create_session_route(user_did: str, session_data: str):
    create_session(user_did, session_data)
    return {"status": "Session created"}


# Session retrieval endpoint
@router.get("/session/{user_did}")
async def get_session_route(user_did: str):
    session_data = get_session(user_did)
    return {"session_data": session_data}


# Token balance endpoint (ICP Canister interaction)
@router.get("/balance/{user_did}")
async def get_user_balance_route(user_did: str):
    balance = get_user_balance(user_did)
    return {"balance": balance}
