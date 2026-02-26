from Utils.decorator import auth_user


class UserAuthentication:

    @staticmethod
    @auth_user
    def user_login(*arg):
        user = arg[0]
        user.log_in()

    @staticmethod
    @auth_user
    def user_logout(*arg):
        user = arg[0]
        user.log_out()