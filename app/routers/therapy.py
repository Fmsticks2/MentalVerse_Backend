from fastapi import APIRouter
from app.services.therapy_service import book_therapy_session
from app.icp.canister_interaction import create_user_tokens

router = APIRouter()


@router.post("/therapy/book")
async def book_therapy_route(user_did: str, therapist_id: str, session_type: str):
    # Book a therapy session
    result = book_therapy_session(user_did, therapist_id, session_type)

    # After booking, reward the user with tokens (for demo, we'll give 10 tokens)
    create_user_tokens(user_did, 10)

    return {"status": result["status"], "reward": "10 tokens awarded"}
