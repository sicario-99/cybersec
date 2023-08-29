""" 
    Mac address is used to identify devices between the networks, it is unique and doesnt change 
    
    ifconfig
    sudo eth0/wlan0 down
    sudo eth0/wlan0 hw ether 00:11:22:33:44:55
    sudo eth0/wlan0 up
    ifconfig -> to check

    Subprocess-> Module
        1. This module contains a number of function
        2. This allows to execute system commands
        3. Depends on OS not on script.
    
    Syntax->    
        import subprocess
        subprocess.call("COMMAND", Shell=True)    
"""


#!/user/bin/env python

import subprocess
import optparse                                         #helps with 

def mac_changer(int, new):
    print("[+] Changing a mac address  for " +int+ " to " +new )

    subprocess.call(["ifconfig", int ,"down"])                          #providing a list so that user does'nt hijacks the code and it knows input is a part of one line of code
    subprocess.call(["ifconfig", int ,"hw", "ether", new])
    subprocess.call(["ifconfig", int ,"up"])

parser = optparse.OptionParser()                            #parser is a variable, optparse is name of module and OptionParser is a class

parser.add_option("-i", "--interface", dest="int", help="Interface to change MAC address")          #
parser.add_option("-m", "--mac", dest="new", help="Enter new MAC address")          #

(arguments, options)=parser.parse_args()             #method that allows the object to understand what user has entered and handle it, return values and arguments user has entered to variables 

mac_changer(arguments.int,arguments.new)            #directly passing input from parser to function as parameters












