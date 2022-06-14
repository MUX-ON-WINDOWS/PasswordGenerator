# Password generator
# Language Pyhton
import random
import json
import const

def generate():
    # Defaults
    dataCheckDefault = input("Default settings? (y/n): ")
    if dataCheckDefault.lower() == 'yes' or dataCheckDefault.lower() == 'y':
        Use_for = const.lower_case + const.upper_case + const.numbers + const.special_characters
    elif dataCheckDefault.lower() == 'no' or dataCheckDefault.lower() == 'n':
        print(const.options)
        askData = input("What lower case characters do you want? (1-4): ")

        if askData == '1':
            Use_for = const.lower_case + const.upper_case
        elif askData == '2':
            Use_for = const.upper_case + const.numbers
        elif askData == '3':
            Use_for = const.numbers + const.special_characters
        elif askData == '4':
            Use_for = const.special_characters + const.lower_case

    # Checks length of password.

    length = int(input('Enter your password length (1-20): '))
    if 1 <= length <= 20:
        length = int(length)
    else:
        print("Password length not correct. Pick a number between 1 and 20.")
        exit()
    # Generate password.
    password = "".join(random.sample(Use_for, length))

    # Creates json file data setup
    data = {
    "Password" : password,
    }
    # Creates file if not exits and add data to it.
    with open('data.json', 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)

    # Use for read data from file
    with open('data.json', 'r') as f:
        config = json.load(f)
        print('Password: {}'.format(config['Password']))
