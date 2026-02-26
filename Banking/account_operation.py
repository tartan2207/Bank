from Utils.exception import  InsufficientFundsError
from Model.account import Account


class AccountOperation:
    def __init__(self, account:Account)->None:
        self.__account=account

    @property
    def account(self) -> Account:
        return self.__account

    def add_money(self, amount: float):
            self.__account.balance += amount

    def withdraw_money(self, amount:float):
            if self.__account.balance < amount:
                raise InsufficientFundsError(self.__account.account_number)
            self.__account.balance -= amount

    def inf_account(self)->str:
        return self.__account.__str__()
