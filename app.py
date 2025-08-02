from fastapi import FastAPI
import os

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Welcome to DAVIDJOS API"}
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
  uvicorn app:app --host 0.0.0.0 --port $PORT
from fastapi import FastAPI
import os
app = FastAPI()
@app.get("/health")
def health_check():
    return {"status": "ok"}
# Optional: Root endpoint
@app.get("/")
def home():
    return {"message": "DAVIDJOS API is live!"}
