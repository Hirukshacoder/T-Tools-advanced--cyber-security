import ssl
import smtplib
from email.message import EmailMessage
from tabulate import tabulate
from termcolor import colored
import pyfiglet

# banner
banner = pyfiglet.figlet_format("Email Attacker")
text = colored(banner, "blue")
print(text)
text = colored("Made by Treveen", "green")
print(text)

# owner 
text = """
Made with 💖 by THB
"""

table = [[text]]
output = tabulate(table, tablefmt='grid')

print(output)

# Email details
sender_email = input("Enter your Email Address: ")
sender_email_password = input("Enter your password: ")
receiver_email = input("Enter the email of the receiver: ")
subject = input("Enter your subject: ")
attach = input("Do you want to attach a file [y/n]:")
body = input("Enter the body of the email: ")
name = input("What is your Name? ")
print("")


# Email variables
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

if attach == "y":
    enter_path = input("Enter the path to your file: ")

    with open(enter_path, "rb") as f:
        file_data = f.read()
        print("file data in binary", file_data)

        file_name = f.name
        print("file name is",file_name)


        message.add_attachment(file_data,maintype="html",subtype="txt",filename=file_name)


if attach == "n":
    pass



# sending email
context = ssl.create_default_context()
print("Sending Email to: ",receiver_email)
print("Give me a second",name)
print("")

# sent Email
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender_email, sender_email_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("ALL RIGHTS RESERVED BY TREVEEN")
print("")
print("Succesfully sent email to",receiver_email)
print("")
print("Thank you for using Email Attacker")
