from fastapi import FastAPI

app = FastAPI(
    title="My Wardrobe API",
    description="API for managing personal wardrobe",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to My Wardrobe API"
    }