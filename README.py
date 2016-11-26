try:
    import pygame
except ImportError:
    # pygame is not installed
    # so ...
    import os
    
    # now check whether you have
    # pip3 or not
    os.system("whereis pip3 > log")
    
    # now check the log file
    file = open("./log", "r")
    paths = file.read().strip().split(" ")
    
    # the standard whereis command outputs
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
        os.system("sudo apt-get install pip3") # for apt-get 
        # or try 'yum/dnf', 'pacman'
        # based on your distribution
    
     # now install pygame
     os.system("pip3 install pygame")
