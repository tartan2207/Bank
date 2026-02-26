import sys

from Banking.account_operation import AccountOperation
from Banking.bank_operation import BankOperation
from Model.account import Account
from Storage.storage import StorageOperation
from Authentication.user import User
from Authentication.auth import  UserAuthentication


def AuthUser(user:User):
    print("Аутентифікація пользователя")
    login = input("Введіть логин: ")
    password = input("Введіть пароль: ")
    UserAuthentication.user_login(user, login, password)

def start_banking():
    account = Account("12356", "Sam")
    account_operation = AccountOperation(account)
    storage = StorageOperation(account)
    bank_operation = BankOperation(account_operation, storage)

    while True:
        print("Menu:\n1. Баланс\n2. Поповнити\n3. Зняти\n4. Історія\n5. Вихід")
        menu_item = input("Виберіть пункт меню: ")
        match menu_item:
            case "1":
                bank_operation.inf_account()
            case "2":
                amount = input("Введіть суму для поповнення рахунку: ")
                bank_operation.deposit(amount)
                bank_operation.inf_account()
            case "3":
                amount = input("Введіть суму для зняття коштів: ")
                bank_operation.withdraw(amount)
                bank_operation.inf_account()
            case "4":
                storage.account_history(account)
            case "5":
                sys.exit(0)
            case _:
                print("Невірний пункт меню. Спробуйте ще раз")

if __name__ == '__main__':
    user = User("login", "password")
    AuthUser(user)
    if user.is_authenticated:
        start_banking()










