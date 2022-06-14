from gen import generate
from banner import banner

banner()

Check = input("Generate password? (y/n): ")
if Check.lower() == 'yes' or Check.lower() == 'y':
    generate()
else:
    print ("Generatring cancled.")
    exit()
