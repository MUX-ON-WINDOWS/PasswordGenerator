# Password generator Python
import random as Generate
from assets.options import options
from assets.checklength import checkLength
from assets.writedata import writeData

def generatePassword():
    # Use default question.
    use_for = options()
    # Checks length of password.
    length = checkLength()
    # Generate password.
    password = "".join(Generate.sample(use_for, length))

    # Creates json file data setup
    data = {
    "Password" : password,
    }
    writeData(data)
