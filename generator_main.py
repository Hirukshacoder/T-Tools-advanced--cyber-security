# modules
import subprocess
import os
import sys
from tabulate import tabulate
import pyfiglet

# banner
banner = pyfiglet.figlet_format("Random password generator")
print(banner)
print("")

# owner 
text = """
Made with 💖 by THB
"""

table = [[text]]
output = tabulate(table, tablefmt='grid')

print(output)
print("")

# os
ossys = (sys.platform)
oslist = print(sys.platform)
# sysos = input("What is your OS? : ")

os.listdir()

# intro
print("Hello welcome to random password generator 1.0 VOL")
print("")

# start

print("[1] Special password")
print("[2] Numeric password")
print("")

subprocess_commands1 = "clear"
subprocess_commands2 = "cls"


select = input("Enter your option [default - special_password] : ")
if select == "":
        subprocess.run(subprocess_commands1, shell=True)
        subprocess.run(subprocess_commands2, shell=True)
        from generator import *

elif select == "1":
         subprocess.run(subprocess_commands1 , shell=True)
         subprocess.run(subprocess_commands2, shell=True)
         from generator import *

elif select == "2":

        subprocess.run(subprocess_commands1 , shell=True)
        subprocess.run(subprocess_commands2, shell=True)
        from numeric import *

else:
    print("Nothing found")