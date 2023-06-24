import configparser

config= configparser.RawConfigParser()
config.read("D:\Sagar Study\pythonProject\OrangeHRM\Configurations\config.ini")

class Readconfig:
    @staticmethod
    def getUrl():
        url= config.get('login data','url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('login data', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('login data', 'password')
        return password
