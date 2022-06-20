import json as jsonFile

def writeData (data):

    # Creates file if not exits and add data to it.
    with open('data.json', 'w') as f:
        jsonFile.dump(data, f, sort_keys=True, indent=4)

    # Use for read data from file
    with open('data.json', 'r') as f:
        config = jsonFile.load(f)
        print('Password: {}'.format(config['Password']))
