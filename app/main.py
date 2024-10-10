from fastapi import FastAPI
from app.routers import auth, therapy

app = FastAPI()

# Include the authentication (DID and session management) routes
app.include_router(auth.router, prefix="/auth")

# Include the therapy session booking routes
app.include_router(therapy.router, prefix="/therapy")


@app.get("/")
def read_root():
    return {"message": "Welcome to Mental Health DAO Platform"}
