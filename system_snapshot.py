#/bin/bash/python3

# Title: System Snapshot
# Author: Brandon Klett
# Date Created: 03/29/2024
# Date Modified: 03/29/2024
# Description:
#   Provide local system snapshot of hardware and software information
#   and present it within CLI. Initial build is for windows.

import subprocess, platform, sys

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
    #open lists to take in gathered data
    dsk_friend_name = []
    dsk_serial_nmbr = []
    dsk_type = []
    dsk_size = []
    gb_convert = 1024**3
    
    dsk_friend_name_raw = subprocess.Popen(["powershell.exe",
                                        "Get-PhysicalDisk | Foreach-Object {write-output $_.FriendlyName}"],
                                        stdout=subprocess.PIPE, shell=True).communicate()[0].splitlines() #grab friendly disk name
    
    for name in dsk_friend_name_raw: #grabs output oject
        if name != None:
            name_decode = name.decode("utf-8")
            dsk_friend_name.append(str(name_decode)) #if the oject isnt none it will append it to the list
            
    dsk_serial_nmbr_raw = subprocess.Popen(["powershell.exe",
                                        "Get-PhysicalDisk | Select-Object -ExpandProperty SerialNumber"],
                                        stdout=subprocess.PIPE, shell=True).communicate()[0].splitlines() #grabs disk serial number
    for number in dsk_serial_nmbr_raw:
        if number != None:
            number_decode = number.decode("utf-8")
            dsk_serial_nmbr.append(str(number_decode)) #append to serial number list
    
    dsk_type_raw = subprocess.Popen(["powershell.exe",
                                        "Get-PhysicalDisk | Foreach-Object {write-output $_.MediaType}"],
                                        stdout=subprocess.PIPE, shell=True).communicate()[0].splitlines() # grabs whether its an hdd or ssd
    for type in dsk_type_raw:
        if type != None:
            type_decode = type.decode("utf-8")
            dsk_type.append(str(type_decode))
    
    dsk_size_raw = subprocess.Popen(["powershell.exe",
                                        "Get-PhysicalDisk | Foreach-Object {write-output $_.Size}"],
                                        stdout=subprocess.PIPE, shell=True).communicate()[0].splitlines() #grabs disk size
    for size in dsk_size_raw:
        if size != None:
            size_decode = size.decode("utf-8")
            gb_size = float(size_decode)/gb_convert #correct disk size to human readable format
            dsk_size.append(f"{gb_size} GB")
    
    storage_report = ""
    
    for name, nmbr, type, size in zip(dsk_friend_name, dsk_serial_nmbr, dsk_type, dsk_size):
        storage_report += f"""
                            Disk Name: {name}
                            Disk Serial Number: {nmbr}
                            Disk Type: {type}
                            Disk Size: {size}
                            """
    return storage_report
    
def main():
    print ("---------------- SCRIPT START ----------------")
    print ("Gathering OS information")
    
    osys = platform.platform() #store operating system name
    mobo_make, mobo_model, mobo_serial = mobo_info()
    storage_report = storage_info()
    

if __name__ == "__main__":
    main()