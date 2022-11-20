from pydantic import BaseModel


class Transaction(BaseModel):
    id: int
    amount: float
    vendor: str
    category_name: str
    user_id: int
