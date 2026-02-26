class User:
    def __init__(self, login, password)->None:
        self.__login=login
        self.__password=password
        self.__is_authenticated =False

    @property
    def login(self) -> str:
        return self.__login

    @property
    def password(self) -> str:
        return self.__password

    @property
    def is_authenticated(self) -> bool:
        return self.__is_authenticated

    def log_in(self):
        self.__is_authenticated=True

    def log_out(self):
        self.__is_authenticated = False