def checkLength():
    global length
    # Checks length of password.
    try :
        length = int(input('Enter your password length (1-20): '))
        if 1 <= int(length) <= 20:
            length = int(length)
            return length
        else:
            print("Password length not correct. Pick a number between 1 and 20.")
            exit()
    except ValueError:
        print("Password length not correct. Pick a number between 1 and 20.")
        exit()
