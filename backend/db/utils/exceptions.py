class UserIdNotExist(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = "ERROR: user id does not exist."


class CategoryIdNotExist(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = "ERROR: category id does not exist."


class TransactionIdNotExist(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.message = "ERROR: transaction id does not exist."
