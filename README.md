Python script for changing MAC addresses. It begins by displaying the current MAC address, then allows the user to input a new one. The updated MAC address is subsequently shown.

The script utilizes basic functions to collect user input, modify the MAC address, and retrieve the current MAC. Additionally, I've incorporated the subprocess module for executing system commands, the optparse module for handling command-line options, and the re module for regex functionality.

This script not only validates user input to prevent hijacking but also verifies that the input meets requirements. It provides error handling and a helpful message.

Upon execution, the script leverages system commands to showcase the modified MAC address. This automation simplifies the process, previously done manually, saving both time and lines of code. You can find this script on my GitHub repository.

# Synatx: sudo python3 mac_changer.py -i wlan0 -m 00:11:22:33:44:55

