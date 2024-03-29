#/bin/bash/python3

# Title: System Snapshot
# Author: Brandon Klett
# Date Created: 03/29/2024
# Date Modified: 03/29/2024
# Description:
#   Provide local system snapshot of hardware and software information
#   and present it within CLI. Initial build is for windows

import os, subprocess, platform

def main():
    print ("---------------- SCRIPT START ----------------")
    print ("Gathering OS information")
    
    osys = platform.platform() #store operating system name
    

if __name__ == "__main__":
    main()