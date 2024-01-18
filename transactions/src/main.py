from logging import Logger
from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

from src import dependencies, wire, services

app = FastAPI()

#schemas.Base.metadata.create_all(bind=database.engine)

@app.get("/")
def read_root():
    return {"service": "transactions"}

@app.get("/version")
def version():
    return {"service" : "transactions", "version": "0.0.1"}

@app.post("/transactions", status_code=status.HTTP_201_CREATED, response_model=wire.TransactionOut)
async def create_transaction(
    transaction: wire.TransactionIn, 
    db: Session = Depends(dependencies.get_database),
    logger: Logger = Depends(dependencies.get_logger)
):
    return services.create_transaction(transaction, db, logger)
