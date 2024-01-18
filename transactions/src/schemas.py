from sqlalchemy import Column, Integer, Numeric, String, Uuid
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Uuid, index=True)
    amount = Column(Numeric)
    origin = Column(String)
    status = Column(String, default="in_progress")
