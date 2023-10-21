# MAC Address Changer

## Disclaimer
This tool is intended for educational and testing purposes. Changing MAC addresses without proper authorization may violate the terms of service of network providers or local laws. Ensure you have the necessary permissions to change a MAC address.

## Introduction
This is a simple Python script that allows you to change the MAC (Media Access Control) address of a network interface on a Unix-based system. A different MAC address can help enhance your privacy and security while connecting to networks.

## Features
- Changes the MAC address of a specified network interface.
- Validates user inputs for both the interface and the new MAC address.
- Checks and displays the current MAC address before and after the change.

## Usage
1. Make sure you have Python installed on your Unix-based system.
2. Clone this repository to your local machine or download the `mac_changer.py` script.
3. Open your terminal or command prompt.
4. Navigate to the directory where the `mac_changer.py` script is located.
5. Run the script by executing the following command:

## Example
Here's an example of running the MAC address changer script:

python mac_changer.py -i eth0 -m 00:11:22:33:44:55


```shell
python mac_changer.py -i <interface> -m <new_mac>

Replace <interface> with the name of your network interface (e.g., eth0, wlan0).
Replace <new_mac> with the new MAC address you want to set for the interface.
The script will change the MAC address of the specified interface and display the current MAC address before and after the change.
''''

