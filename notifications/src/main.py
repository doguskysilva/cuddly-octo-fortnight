from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"service": "notifications"}

@app.get("/version")
def version():
    return {"service": "notifications", "version": "0.0.1"}
