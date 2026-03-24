from fastapi import FastAPI

app = FastAPI()

# Ana endpoint
@app.get("/")
def home():
    return {"message": "API çalışıyor 🚀"}

# Parametreli endpoint
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": "Erdem"}

# Query param
@app.get("/search")
def search(q: str):
    return {"query": q}