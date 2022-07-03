# Modules
import subprocess
from tabulate import tabulate
import pyfiglet
from termcolor import colored

# banner
banner = pyfiglet.figlet_format("T - Tools")
text = colored(banner, "blue")
print(text)

# owner
text = """
Owner :- @Treveen
Only for educational purposes
"""

table = [[text]]
output = tabulate(table, tablefmt='grid')

print(output)

print("")

# select
text1 = colored("[1] - Email Attacker", "green")
text2 = colored("[2] - Random password generator", "green")
text3 = colored("[3] - Web Scrapper X", "green")
text4 = colored("[4] - phone number locator", "green")
print(text1)
print(text2)
print(text3)
print(text4)

print("")

select = input(colored("Enter an option from the above list: ", "green"))



if select == '1':
    print("")
    print("OK")
    print("")
    # commands
    subprocess.run("cls", shell=True)
    subprocess.run("clear", shell=True)
    from email_attacker import *

elif select == '2':
    print("")
    print("OK")
    print("")
    subprocess.run("cls", shell=True)
    subprocess.run("clear", shell=True)
    from generator_main import *

elif select == '3':
    print("")
    print("OK")
    print("")
    subprocess.run("cls", shell=True)
    subprocess.run("clear", shell=True)
    from scrapper import *

elif select == '4':
    print("")
    print("OK")
    print("")
    subprocess.run("cls", shell=True)
    subprocess.run("clear", shell=True)
    from phonenumberlocator import *

else:
    print("Nothing found like :-", select)