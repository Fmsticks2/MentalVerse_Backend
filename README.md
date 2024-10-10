# MentalHealthDAO

#### 1.1 Clone the Git Repository
1. Decide on a project name: *“MentalHealthDAO”* (feel free to change this).
   ```bash
   git clone git@github.com:Adebowale-Morakinyo/MentalHealthDAO.git
   ```

#### 1.2 Set up Python Virtual Environment
1. Install Python virtual environment package if not already installed:
   ```bash
   sudo apt install python3-venv
   ```
2. Set up and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required packages (we'll start simple and expand as needed):
   ```bash
   pip install -r requirements.txt
   ```

   *FastAPI* will handle our APIs, *uvicorn* will serve the application, *web3* will handle blockchain interactions, and *requests* will support external API calls.

### 2. **Backend Structure**
We will create a simple FastAPI backend that handles Web3 wallet connection, decentralized identity, and token incentives.

#### 2.1 Project Structure
```bash
MentalHealthDAO/
│
├── app/
│   ├── __init__.py
│   ├── main.py  # Entry point for the API
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py  # Decentralized identity routes (DID)
│   │   └── therapy.py  # Therapy session booking routes
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py  # Logic for DID and session management
│   │   └── therapy_service.py  # Logic for therapy sessions
│   ├── models/  # Future models here
│   │   └── __init__.py
│   └── icp/
│       └── canister_interaction.py  # Interact with ICP canisters directly
├── .env  # Environment variables
├── requirements.txt  # Python dependencies
├── README.md
└── main.py  # Uvicorn entry point
```
