from abc import ABC, abstractmethod
from typing import List, Dict
from ..models import *


class Dal(ABC):

    @abstractmethod
    def add_transaction(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    def delete_transaction(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    def get_all_transactions_by_user_id(self, user_id: int) -> List[Transaction]:
        pass

    @abstractmethod
    def get_user_balance(self, user_id: int) -> float:
        pass

    @abstractmethod
    def get_all_expenses_by_category(self) -> Dict[str, float]:
        pass
