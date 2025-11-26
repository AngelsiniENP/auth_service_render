# main.py ← EN LA RAÍZ DEL REPO
from auth_service.app import app   # Cambia "auth_service" por el nombre real de tu carpeta interna

# Health check para Render
@app.get("/health")
def health():
    return {"status": "ok", "service": "auth"}