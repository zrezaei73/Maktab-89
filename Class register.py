import re

class User:
    def __init__(self, f_name, l_name, phone, email, username, password):
        self.f_name = f_name
        self.l_name = l_name
        self.phone = phone
        self.email = email
        self.username = username
        self.__password = password
        self.user_info = {}

    def register(self):
        self.validate()
        if self.username in self.user_info:
            raise Exception('user already exist!')
        else:
            self.user_info.update({self.username: [self.__password, self.f_name, self.l_name, self.phone, self.email]})


    def validate(self):
        assert re.findall('^(\+98)?9\d{9}$', self.phone), 'invalid phone'
        assert re.findall('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', self.email), 'invalid email'
        assert re.findall('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', self.__password), 'invalid password'

        return True

    def login(self, username, password):
        if username in self.user_info:
            if self.__password == password:
                return 'successfully registered'
            else:
                 return 'wrong password'
        else:
            return 'user has not registered yet'

class Main:
    try:
        obj = User('zahra', 'rezaei', '+989125883464', 'szrezaei@yahoo.com', 'zrezaei73', 'Zrezaei73')
        obj.register()
        print(obj.user_info.keys())
        print(obj.login('zrezaei73','12345'))
        print(obj.login('sz','12345'))
    except AssertionError as msg:
        print(msg)