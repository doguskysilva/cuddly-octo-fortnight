from pydantic import BaseModel

class TransactionBase(BaseModel):
    customer_id: str
    amount: int
    origin: str
    status: str

class Transaction(TransactionBase):
    id: int
