
#!/usr/bin/env python

import subprocess                                                                                        #allows to run system commands
import optparse                                                                                          #helps in parsing command-line options.
import re

def get_arguments():                                                                                     #function to get arguments from user   
    parser = optparse.OptionParser()                                                                     #parser is a variable/object, optparse is name of module and OptionParser is a class
    parser.add_option("-i", "--interface", dest="int", help="Interface to change MAC address")          
    parser.add_option("-m", "--mac", dest="new", help="Enter new MAC address")                          
    (arguments, options) =  parser.parse_args()  
    if not arguments.int:
        parser.error("[-] Please enter an interface,use --help for more info")
    elif not arguments.new:
        parser.error("[-] Please enter a new mac address, use --help for more info")                      #method that allows the object to understand what user has entered and handle it, return values and arguments user has entered to variables 
    return arguments

def mac_changer(interface, new_mac):                                                                      #function to change mac address 
    print("[+] Changing a mac address  for " +interface+ " to " +new_mac )
    subprocess.call(["ifconfig", interface ,"down"])                                                      #providing a list so that user does'nt hijacks the code and it knows input is a part of one line of code
    subprocess.call(["ifconfig", interface ,"hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface ,"up"])

def get_current_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    ifconfig_str = ifconfig.decode('utf-8') 
    result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_str)
    if result:
        return result.group(0)
    else:
        print("[-] Could not read mac address.")


arguments = get_arguments()                                                                               #get arguments from user using get_arguments function and store to variable arguments 

current_mac = get_current_mac(arguments.int)                                                              #using system commands gets the current mac address and stores it 
print("Current MAC = " + str(current_mac))                                                                #prints the current mac using regex principal

mac_changer(arguments.int,arguments.new)                                                                  #changes the mac address taking input from user 

current_mac = get_current_mac(arguments.int)                                                              #checks that new mac is equal to what user entered
if current_mac == arguments.new: 
    print("[+] Mac address was successfully changed" +current_mac)
else:
    print("[-] Mac address was not changed")
