from Utils.exception import InvalidAmountError, UserNotPermission
def validate_transaction(func):
    def wripper(*args, **kwargs):

        if type(args[1]) is not str:
            raise TypeError("Помилковий тип аргументу")
        if not str(args[1]).isdigit() or float(args[1]) <= 0:
            raise InvalidAmountError(str(args))
        return func(*args, **kwargs)
    return wripper

def auth_user(func):
    def wrapper(*args, **kwargs):
        user,login,password= args
        if user.login==login and user.password==password:
            return func(*args, **kwargs)
        else:
            raise UserNotPermission(login)
    return wrapper

