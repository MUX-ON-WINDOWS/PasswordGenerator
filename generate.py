# Password generator Python
import random as Generate
import json as jsonFile
import assets.const as const
from assets.custom import writeData

def generatePassword():
    # Use default question.
    dataCheckDefault = input("Default settings? (y/n): ")
    if dataCheckDefault.lower() == 'yes' or dataCheckDefault.lower() == 'y':
        Use_for = const.lower_case + const.upper_case + const.numbers + const.special_characters
    elif dataCheckDefault.lower() == 'no' or dataCheckDefault.lower() == 'n':
        # Displays possible options for custom password generation.
        print(const.options)

        # Asks user to input the options they want to use.
        askData = input("What lower case characters do you want? (1-4): ")
        if 1 <= int(askData) <= 4:
            if askData == '1':
                Use_for = const.lower_case + const.upper_case
            elif askData == '2':
                Use_for = const.upper_case + const.numbers
            elif askData == '3':
                Use_for = const.numbers + const.special_characters
            elif askData == '4':
                Use_for = const.special_characters + const.lower_case
        else:
            print("Password length not correct. Pick a number between 1 and 4.")
            exit()

    # Checks length of password.

    length = int(input('Enter your password length (1-20): '))
    if 1 <= int(length) <= 20:
        length = int(length)
    else:
        print("Password length not correct. Pick a number between 1 and 20.")
        exit()
    # Generate password.
    password = "".join(Generate.sample(Use_for, length))

    # Creates json file data setup
    data = {
    "Password" : password,
    }

    writeData(data)
