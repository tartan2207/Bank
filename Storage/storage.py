import os

from Storage.file_operation import FileOperation
from Model.account import Account
from pathlib import Path

class StorageOperation:
    def __init__(self, account:Account )->None:
        self.__path_dir= "../FileStorage"
        self.__account=account
        Path(self.__path_dir).mkdir(parents=True, exist_ok=True)
        self.__file_path= ""

    def __create_file_path(self):
        if not os.path.exists(self.__file_path):
            return os.path.join(self.__path_dir, f"{self.__account.account_number}.json")

    def save_transaction(self,*arg):
        self.__file_path=self.__create_file_path()
        FileOperation.save_log(self.__file_path, *arg)

    def account_history(self, account:Account):
        self.__file_path = self.__create_file_path()
        print(f"Транзакції рахунку {account.account_number}")
        FileOperation.read_log(self.__file_path)