import enum

class AccountStatus(enum.IntEnum):
    frozen = 1
    actual = 2

class Account:
    def __init__(self, acc_number:str,owner:str )->None:
        self.__acc_number = acc_number
        self.__owner = owner
        self.__balance = 0
        self.__status = AccountStatus.actual

    @property
    def account_number(self) -> str:
        return self.__acc_number

    @property
    def owner(self) -> str:
        return self.__owner

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, amount: float) -> None:
        self.__balance=amount

    @property
    def status(self) -> AccountStatus:
        return self.__status

    @status.setter
    def status(self, status:AccountStatus) -> None:
        self.__status=status

    def __str__(self):
        return (f"рахунок № {self.__acc_number}, власник: {self.owner}, "
              f"статус {self.__status.name}, баланс {self.__balance}грн")

