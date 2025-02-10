import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class read_config:
    @staticmethod
    def get_login_page_url():
        login_page_url = config.get("login page data", "login_page_url")
        return login_page_url

    @staticmethod
    def get_username():
        username = config.get("login page data", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("login page data", "password")
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get("login page data", "invalid_username")
        return invalid_username