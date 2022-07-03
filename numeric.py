# modules
import random

# style
print("Hello welcome to random numeric password generator 1.0 VOL")
print("")

# name
name = str(input("Enter your name : "))

# start
numbers = "0987654321"

passwords = int(input("How many passwords do you want? : "))
pwdArray = [0]*passwords
password_length = int(input("How many numbers do you want in your password? : "))
add_name = str(input("Do you want to add your name? (not recommended) [y/n] : "))
special_remarks = str(input("Any special remarks? : "))


# start generator
if add_name == 'y':
    for i in range(0, passwords):
        password = ""
        for a in range(0, password_length):
            password_characters = random.choice(numbers)
            password        = password + password_characters
            passwords_built = name + special_remarks + password
        pwdArray[i]=passwords_built

    print("Your password is: ",(pwdArray))

elif add_name == 'n':
    for i in range(0, passwords):
        password = ""
        for a in range(0, password_length):
            password_characters = random.choice(numbers)
            password        = password + password_characters
            passwords_built = special_remarks + password
        pwdArray[i]=passwords_built
    
    print("Your password is: ",(pwdArray))

# save password
save = input("Do you want to save your password? [y/n] : ")

if save == "y":
    file = open(input("What is the name of your file? make sure to enter the file type : "),"a")
    content=str(pwdArray)
    file.write(content)
    file.close()

elif save == "n":
    print("OK Goodbye!")

else:
    print("Nothing found")