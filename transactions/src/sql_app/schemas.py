from sqlalchemy import Column, Integer, String, Uuid, Numeric

from .database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Uuid, index=True)
    amount = Column(Numeric)
    origin = Column(String)
    status = Column(String, default="in_progress")
