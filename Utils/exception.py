class BankError(Exception):
    pass

class InsufficientFundsError(BankError):
    def __init__(self, number,  message="Hедостатньо коштів"):
        self.message = message
        self.number = number
        super().__init__(self.message)

    def __str__(self):
        return f'На рахунку № {self.number}: {self.message}'

class InvalidAmountError(BankError):
    def __init__(self, value, message="Сума менша за нуль або не число"):
        self.message = message
        self.value = value
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.value}'

class AccountLockedError(BankError):
    def __init__(self, number, message="Рахунок заморожений"):
        self.message = message
        self.number = number
        super().__init__(self.message)

    def __str__(self):
        return f'Статус рахунку № {self.number}: {self.message}'

class UserNotPermission(Exception):
    def __init__(self, login, message="Користувач не аутентифікований."):
        self.message = message
        self.login = login
        super().__init__(self.message)

    def __str__(self):
        return f'Статус користувача {self.login}: {self.message}'
    pass

class FileNotFound(Exception):
    pass

class NotFilePermission(Exception):
    pass