#! /Users/user/.pyenv/versions/3.7.5/bin/python3

# strongPasswordDectection: checks whether
# a copied password or entered password is strong.

import re
import time
import pyperclip


def main():
    #  built a function that uses REGEX to make sure the password string it is passed
    #  is at least 8 characters long
    #  contains both upper and lower case letters
    #  has at least one digit

    def strongPasswordChecker():
        # Password REGEXs
        #  is at least 8 characters long
        CharCountRegex = re.compile(r'.{8,}')
        #  contains both upper and lower case letters
        UpperLettersRegex = re.compile(r'[A-Z]')
        #  has at least one digit
        DigitRegex = re.compile(r'[0-9]')

        print("checking length...")

        # Check input from the user:
        passwordToCheck = pyperclip.paste()
        criteria1 = CharCountRegex.search(passwordToCheck)

        criteria2 = UpperLettersRegex.search(passwordToCheck)

        criteria3 = DigitRegex.search(passwordToCheck)

        if criteria1 != None:
            print("great your password has at least eight chars")
            print("checking contents...")
            time.sleep(2)
            if criteria2 != None:
                print(
                    "great your password also contains uppercase and lowercase letters")
                print("checking for numeric values in your password...")
                time.sleep(2)
                if criteria3 != None:
                    print("your password is awesome. use it!")
                else:
                    print("your password needs to contain numbers to be strong")
            else:
                print("your password is long enough but...")
                print("it needs both uppercase and lowercase letters")
        else:
            print("you can make a better password...")
            print("make it at least eight characters for starters")

    strongPasswordChecker()


main()
