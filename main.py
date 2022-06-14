from generate import generatePassword
from banner import banner

banner()

Check = input("Generate password? (y/n): ")
if Check.lower() == 'yes' or Check.lower() == 'y':
    generatePassword()
else:
    print ("Generatring cancled.")
    exit()
