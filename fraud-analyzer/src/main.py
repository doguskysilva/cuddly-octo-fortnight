from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"service": "fraud-analizer"}

@app.get("/version")
def version():
    return {"service": "fraud-analizer", "version": "0.0.1"}
