from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to DevDocs Semantic Search"
    }

@app.get("/health")
def health():
    return {
        "status": "UP",
        "message":"Hello my self Up bala"
    }