from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"service": "transactions"}

@app.get("/version")
def version():
    return {"service" : "transactions", "version": "0.0.1"}
