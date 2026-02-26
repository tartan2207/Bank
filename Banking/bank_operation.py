from Utils.exception import InvalidAmountError, BankError,  AccountLockedError
from Model.account import AccountStatus
from Storage.storage import StorageOperation
from Banking.transaction import Transaction
from Banking.account_operation import AccountOperation
from Utils.decorator import validate_transaction


class BankOperation:
    def __init__(self,  account_operation: AccountOperation, storage: StorageOperation)->None:
        self.__account_operation = account_operation
        self.__storage=storage
        self.__transaction =Transaction()
        self.__transaction.success_message = "успіх"
        self.__transaction.error_message = "відміна"

    @validate_transaction
    def deposit(self, amount: str):
        result_message=None
        try:
            if self.__account_operation.account.status == AccountStatus.frozen:
                raise AccountLockedError(self.__account_operation.account.account_number)
            self.__account_operation.add_money(float(amount))
        except AccountLockedError as ex:
            result_message = self.__transaction.error_message
            print(ex)
        except TypeError as ex:
            result_message = self.__transaction.error_message
            print(ex)
        except InvalidAmountError as ex:
            result_message = self.__transaction.error_message
            print(ex)
        except BankError as ex:
            result_message = self.__transaction.error_message
            print(ex)
        else:
           result_message = self.__transaction.success_message
        finally:
            arg = (self.__account_operation.account.account_number,"поповнення", self.__transaction.number, amount, result_message)
            self.__storage.save_transaction( *arg)


    @validate_transaction
    def withdraw(self,amount:str):
        result_message = None
        try:
            if self.__account_operation.account.status == AccountStatus.frozen:
                raise AccountLockedError(self.__account_operation.account.account_number)
            self.__account_operation.withdraw_money(float(amount))
        except AccountLockedError as ex:
            print(ex)
        except TypeError as ex:
            result_message = self.__transaction.error_message
            print(ex)
        except InvalidAmountError as ex:
            result_message = self.__transaction.error_message
            print(ex)
        except BankError as ex:
            result_message = self.__transaction.error_message
            print(ex)
        else:
            result_message = self.__transaction.success_message
        finally:
            arg = (self.__account_operation.account.account_number,"зняття",self.__transaction.number , amount, result_message)
            self.__storage.save_transaction( *arg)

    def inf_account(self):
        print("\nВідомості про рахунок")
        print(self.__account_operation.inf_account())
        print()

