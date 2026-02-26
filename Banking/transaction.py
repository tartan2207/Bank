
def transaction_number():
    count = 1
    while True:
        yield count
        count += 1

class Transaction:
    def __init__(self)->None:
        self.__number = None
        self.__success_message = ""
        self.__error_message = ""


    @property
    def number(self) -> int:
        return next(transaction_number())

    @property
    def success_message(self) -> str:
        return self.__success_message

    @success_message.setter
    def success_message(self, message: str) -> None:
        self.__success_message = message

    @property
    def error_message(self) -> str:
        return self.__error_message

    @error_message.setter
    def error_message(self, message: str) -> None:
        self.__error_message = message