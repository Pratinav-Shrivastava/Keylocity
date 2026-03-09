from fastapi import FastAPI

app = FastAPI(title = "Keylocity API")

@app.get("/")
def root():
    return {"message" : "Welcome to Keylocity API"}