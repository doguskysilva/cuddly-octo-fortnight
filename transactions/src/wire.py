from .models import Status, TransactionBase

class TransactionIn(TransactionBase):
    pass

class TransactionOut(TransactionBase):
    id: int
    status: str = Status 