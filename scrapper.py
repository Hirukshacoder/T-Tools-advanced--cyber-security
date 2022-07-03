# modules
import requests
import itertools
import threading
import time
import sys
from tabulate import tabulate
import pyfiglet
from bs4 import BeautifulSoup



# banner
banner = pyfiglet.figlet_format("Web Scrapper X")
print(banner)
print("")

# owner 
text = """
Made with 💖 by THB
"""

table = [[text]]
output = tabulate(table, tablefmt='grid')

print(output)

# web link
link = str(input("Enter your url to scrap : "))

# get link
got_it = requests.get(link)
document = BeautifulSoup(got_it.text, "html.parser")

html = str((document.prettify()))
print("")

# loading
print("Getting ready")
print("")
done = False
#here is the animation
def animate():
      for c in itertools.cycle(['(', ')', '^', '\\']):
        if done:
            break
        sys.stdout.write("\r getting information " + c)
        sys.stdout.flush()
        time.sleep(0.1)
sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(10)
done = True
print("")
print("")
print("Got information")
print("")


# file
file = open(input("Enter the name of your html file : "), "a")
file.write(html)
file.close()

# end
print("")
print("** THANK You for using **")

