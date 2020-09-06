import random
import string

class GenerateUserInfo:

    def __init__(self):
        pass

    @staticmethod
    def create_username(prefixvalue):
        print("creating username")
        num = ''.join((random.choice(string.digits) for i in range(4)))
        username = prefixvalue + num
        print(username)
        return username

    @staticmethod
    def create_password():
        print("creating password")
        letter_and_digit = string.ascii_letters + string.digits
        password = ''.join(random.choice(letter_and_digit) for i in range(8))
        print(password)
        return password

    @staticmethod
    def create_phonenumber():
        print("creating email")
        num = ''.join(random.choice(string.digits) for i in range(9))
        phonenumber = "+358"+num
        print(phonenumber)
        return phonenumber

if __name__ == "__main__":
    gen = GenerateUserInfo()
    gen.create_username('user')
    gen.create_password()
    gen.create_phonenumber()