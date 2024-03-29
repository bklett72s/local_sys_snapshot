#/bin/bash/python3

# Title: System Snapshot
# Author: Brandon Klett
# Date Created: 03/29/2024
# Date Modified: 03/29/2024
# Description:
#   Provide local system snapshot of hardware and software information
#   and present it within CLI. Initial build is for windows

import os, subprocess, platform, sys

#grabs basic manufacturer, model, and serial number information as registered on the board
def mobo_info():
    try:
        mobo_make = ""
        mobo_model = ""
        mobo_serial= ""
        try:
            mobo_make = subprocess.Popen(["powershell.exe",
                                        "get-wmiobject win32_baseboard | select-object -expandproperty Manufacturer"],
                                        stdout=sys.stdout, shell=True).communicate()[0] #grab manufacturer from wmiobject
        except:
            mobo_make = "ERROR: mobo make N/A"
            
        try:
            mobo_model = subprocess.Popen(["powershell.exe",
                                        "get-wmiobject win32_baseboard | select-object -expandproperty Product"],
                                        stdout=sys.stdout, shell=True).communicate()[0] #grab model from wmiobject
        except:
            mobo_model = "ERROR: mobo make N/A"
        
        try:
            mobo_serial = subprocess.Popen(["powershell.exe",
                                        "get-wmiobject win32_baseboard | select-object -expandproperty SerialNumber"],
                                        stdout=sys.stdout, shell=True).communicate()[0] #grab serial number from wmiobject
        except:
            mobo_serial = "ERROR: mobo seriel N/A"
            
        return mobo_make, mobo_model, mobo_serial
    except: 
        return "ERROR: Mobo gather failed"

#gather information on storgae devices within local hardware
def storage_info():
    print ("derp")
    

def main():
    print ("---------------- SCRIPT START ----------------")
    print ("Gathering OS information")
    
    osys = platform.platform() #store operating system name
    mobo_make, mobo_model, mobo_serial = mobo_info()
    

if __name__ == "__main__":
    main()