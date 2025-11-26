# main.py (raíz)
from auth_service import app

@app.get("/health")
def health():
    return {"status": "ok", "service": "ms_categories"}