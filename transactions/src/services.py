from logging import Logger
from src.wire import TransactionIn
from src import repository
from sqlalchemy.orm import Session

def create_transaction(
        transaction: TransactionIn,
        db: Session,
        logger: Logger
):
    # do anything with this transaction, like some validation
    logger.info("Saving transaction in database", transaction)
    return repository.store_transaction(transaction, db)
