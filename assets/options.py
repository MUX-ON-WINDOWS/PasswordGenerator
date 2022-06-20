import assets.const as const

def options():
    global use_for
    dataCheckDefault = input("Default settings? (y/n): ")
    if dataCheckDefault.lower() == 'yes' or dataCheckDefault.lower() == 'y':
        use_for = const.lower_case + const.upper_case + const.numbers + const.special_characters
        return use_for
    elif dataCheckDefault.lower() == 'no' or dataCheckDefault.lower() == 'n':
        # Displays possible options for custom password generation.
        print(const.options)

        # Asks user to input the options they want to use.
        askData = input("What lower case characters do you want? (1-4): ")
        if 1 <= int(askData) <= 4:
            if askData == '1':
                use_for = const.lower_case + const.upper_case
                return use_for
            elif askData == '2':
                use_for = const.upper_case + const.numbers
                return use_for
            elif askData == '3':
                use_for = const.numbers + const.special_characters
                return use_for
            elif askData == '4':
                use_for = const.special_characters + const.lower_case
                return use_for
        else:
            print("Password length not correct. Pick a number between 1 and 4.")
            exit()
    else :
        print("Invalid input. Exiting.")
        exit()
