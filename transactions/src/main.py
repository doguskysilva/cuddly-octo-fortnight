from fastapi import Depends, FastAPI, status

from . import models
from . import wire
from .sql_app import crud, schemas, database

app = FastAPI()

schemas.Base.metadata.create_all(bind=database.engine)

def get_database():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"service": "transactions"}

@app.get("/version")
def version():
    return {"service" : "transactions", "version": "0.0.1"}

@app.post("/transactions", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_transaction(transaction: wire.TransactionIn, db: crud.Session = Depends(get_database)):
    new_transaction = crud.create_transaction(db, transaction)
    return new_transaction
