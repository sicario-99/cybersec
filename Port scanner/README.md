# Port Scanner

## Introduction
This is a simple Python port scanner script that allows you to scan a target IP address for open ports within a specified range. It is a basic tool for network security testing and exploration.

## Features
- Scans a target IP address for open ports in a defined range.
- Provides information about open ports on the target.
- Simple and easy to use.

## Disclaimer
This tool is intended for educational and testing purposes. Always ensure you have the necessary permissions to scan a target. Unauthorized scanning of networks or hosts is illegal and unethical.

## Usage
1. Make sure you have Python 3.x installed on your system.
2. Clone this repository to your local machine or download the `port_scanner.py` script.
3. Open your terminal or command prompt.
4. Navigate to the directory where the `port_scanner.py` script is located.
5. Run the script by executing the following command:

Replace `<target_ip>` with the IP address of the target you want to scan.

6. The script will start scanning the target for open ports within the default port range (50-85).

## Customization
- You can modify the port range by editing the `for` loop in the script. The default range is set from 50 to 85, but you can change it to scan a different range of ports.
- You can add error handling or additional functionality to the script to suit your specific needs.

## Example
Here's an example of running the port scanner on a local target:

```shell
python3 port_scanner.py 127.0.0.1
