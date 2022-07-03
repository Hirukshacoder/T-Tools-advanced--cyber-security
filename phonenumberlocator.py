# modules
import phonenumbers
from tabulate import tabulate

print("       .__                            _______               ___. ")                
print(" _____ |  |__   ____   ____   ____    \      \  __ __  _____\_ |__   ___________ ")
print("\____ \|  |  \ /  _ \ /    \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ ")
print("|  |_> >   Y  (  <_> )   |  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ ")
print("|   __/|___|  /\____/|___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   ")
print("|__|        \/            \/     \/          \/            \/    \/     \/       ")

print("")

# owner 
text = """
Made with 💖 by THB
"""

table = [[text]]
output = tabulate(table, tablefmt='grid')

print(output)

from phonenumber import number
from phonenumbers import geocoder
channel_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(channel_number, "en"))
print("")
from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))
print("")
print("Goodbye!")