#!/user/bin/env python

import subprocess                                                                                        #allows to run system commands
import optparse                                                                                          #helps in parsing command-line options.

def get_arguments():                                                                                     #function to get arguments from user   
    parser = optparse.OptionParser()                                                                     #parser is a variable/object, optparse is name of module and OptionParser is a class
    parser.add_option("-i", "--interface", dest="int", help="Interface to change MAC address")          
    parser.add_option("-m", "--mac", dest="new", help="Enter new MAC address")                          
    (arguments, options) =  parser.parse_args()  
    if not arguments.int:
        parser.error("[-] Please enter an interface,use --help for more info")
    elif not arguments.new:
        parser.error("[-] Please enter a new mac address, use --help for more info")                      #method that allows the object to understand what user has entered and handle it, return values and arguments user has entered to variables 
    return options

def mac_changer(interface, new_mac):                                                                     #function to change mac address 
    print("[+] Changing a mac address  for " +interface+ " to " +new_mac )
    subprocess.call(["ifconfig", interface ,"down"])                                                     #providing a list so that user does'nt hijacks the code and it knows input is a part of one line of code
    subprocess.call(["ifconfig", interface ,"hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface ,"up"])

options = get_arguments()
mac_changer(arguments.int,arguments.new)                                                                 #directly passing input from parser to function as parameters

