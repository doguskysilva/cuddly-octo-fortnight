from typing import Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict

Origin = Literal["app", "web", "internal"]
Status = Literal["in_progress", "approved", "discarded"]


class TransactionBase(BaseModel):
    customer_id: UUID
    amount: int
    origin: str = Origin


class Transaction(TransactionBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    status: str = Status
