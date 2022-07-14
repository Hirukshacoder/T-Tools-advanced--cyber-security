from termcolor import colored 
import pyfiglet
import random 
import requests
import socket


banner1 = pyfiglet.figlet_format("Ip - Tracer", font = "alligator")
banner2 = pyfiglet.figlet_format("Ip - Tracer", font = "standard")
banner3 = pyfiglet.figlet_format("Ip - Tracer", font = "letters")
banner4 = pyfiglet.figlet_format("Ip - Tracer", font = "alphabet")
banner5 = pyfiglet.figlet_format("Ip - Tracer", font = "5lineoblique")
banner6 = pyfiglet.figlet_format("Ip - Tracer", font = "slant")
text1 = colored(banner1, "blue")
text2 = colored(banner3, "red")


banner = (text1, text2, banner4, banner5, banner6)


random_banner = random.choice(banner)
print(random_banner)


ip = str(input("Enter the public ip to trace: "))

hostname = socket.gethostname()

ipaddress = socket.gethostbyname(hostname)

print("your ipv4 - ",ipaddress)
response = requests.post("http://ip-api.com/batch", json=[
  {"query": ip},

]).json()

for ip_info in response:
    for k,v in ip_info.items():
        print(k,v)
    print("\n")

