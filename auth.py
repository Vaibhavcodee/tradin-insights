from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

# Create a reusable HTTPBasic instance
security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    """Basic username/password authentication."""
    if not (secrets.compare_digest(credentials.username, "user") and secrets.compare_digest(credentials.password, "pass")):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return credentials.username
