from generate import generatePassword
from assets.banner import banner

try :
    banner()
    generatePassword()
except EOFError:
    print('Hello user it is EOF exception, please enter something and run me again')
    exit()
except KeyboardInterrupt:
    print("\n[!] You pressed Ctrl+C")
    print("[!] Exiting...")
    exit()
