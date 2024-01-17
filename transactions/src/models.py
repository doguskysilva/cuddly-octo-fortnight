from typing import Literal
from pydantic import BaseModel
from uuid import UUID

Origin = Literal['app', 'web', 'internal']
Status = Literal['in_progress', 'approved', 'discarded']

class TransactionBase(BaseModel):
    customer_id: UUID
    amount: int
    origin: str = Origin

class Transaction(TransactionBase):
    id: int
    status: str = Status

    class ConfigDict:
        from_attributes = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True 
