from pydantic import BaseModel
from uuid import UUID

from . import models

class TransactionIn(BaseModel):
    customer_id: UUID
    amount: int
    origin: str

class TransactionOut(models.Transaction):
    pass