from fastapi import Depends, FastAPI, status

from .wire import TransactionIn, TransactionOut
from .sql_app import crud, schemas, database

app = FastAPI()

schemas.Base.metadata.create_all(bind=database.engine)


@app.get("/")
def read_root():
    return {"service": "transactions"}

@app.get("/version")
def version():
    return {"service" : "transactions", "version": "0.0.1"}

@app.post("/transactions", status_code=status.HTTP_201_CREATED, response_model=TransactionOut)
async def create_transaction(transaction: TransactionIn, db: crud.Session = Depends(database.get_database)):
    return crud.create_transaction(db, transaction)
