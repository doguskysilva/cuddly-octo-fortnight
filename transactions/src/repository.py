from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.wire import TransactionIn
from src import schemas
from src.models import Transaction


def store_transaction(transaction: TransactionIn, db: Session) -> Transaction:
    db_transaction = schemas.Transaction(**transaction.model_dump())

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    
    return Transaction.model_validate(db_transaction)

def transaction_by_id(id: int, db: Session) -> Optional[Transaction]:
    transaction = db.get(schemas.Transaction, id)

    if transaction is None:
        return None
    
    return Transaction.model_validate(transaction)
