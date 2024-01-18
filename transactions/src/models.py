from typing import Literal
from pydantic import BaseModel, ConfigDict
from uuid import UUID

Origin = Literal['app', 'web', 'internal']
Status = Literal['in_progress', 'approved', 'discarded']

class TransactionBase(BaseModel):
    customer_id: UUID
    amount: int
    origin: str = Origin

class Transaction(TransactionBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    status: str = Status
