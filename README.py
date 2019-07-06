################################################################################
############################### TWO DEPENDENCIES ###############################
############################### 1. PyQt5         ###############################
############################### 2. pygame        ###############################
################################################################################
import os
def check_for_pip3():
    # now check whether you have
    # pip3 or not
    os.system("whereis pip3 > log")
    
    # now check the log file
    file = open("./log", "r")
    paths = file.read().strip().split(" ")
    
    # the standard 'whereis' command outputs
    # three things.
    #    1. The name of binary file we are looking for
    #    2. The binary executable file
    #    3. The manual page
         
    if len(paths) < 2 : 
        # in this case
        # you do not have pip3 installed in your system
        # or may be, you have pip3 installed
        # but the path is not set
        # lets, install pip3
        os.system("sudo apt-get install python3-pip") # for apt-get 
        # or try 'yum/dnf', 'pacman'
        # based on your distribution
try:
    import pygame
except ImportError:
    # pygame is not installed
    # so ...
    check_for_pip3()
     # now install pygame
    print("#####################################")
    print("######### Installing pygame #########")
    print("#####################################")
    os.system("pip3 install pygame")
    
try:
    import PyQt5
except ImportError:
     check_for_pip3()
     # now install pyqt5
     print("#####################################")
     print("######### Installing PyQt5 ##########")
     print("#####################################")
     os.system("pip3 install pyqt5")
     check_for_pip3()
     # now install pyqt5
     os.system("pip3 install pyqt5")
