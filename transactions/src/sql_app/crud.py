from sqlalchemy.orm import Session

from .. import wire
from .. import models
from . import schemas

def create_transaction(db: Session, transaction: wire.TransactionIn):
    db_transaction = schemas.Transaction(
        customer_id = transaction.customer_id,
        amount = transaction.amount,
        origin = transaction.origin
    )

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction