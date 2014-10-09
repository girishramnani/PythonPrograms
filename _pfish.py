import logging
import argparse
import os
import sys



def readCommandline():
    parser = argparse.ArgumentParser("this is the girish python file system hashing Gp-fish\n")
    parser.add_argument('-v',help="shows the the arguments in the command line\n\n",action="store_true");
    parser.add_argument('--version',action="version",version="GP-fish ver 1.0");
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-md5',help="Uses the MD5 algorithm",action="store_true")
    group.add_argument('-SHA1',help="uses the SHA1 algorithm", action="store_true")
    group.add_argument('-SHA2',help="uses the SHA2 algorithm", action="store_true")


    global obj
    obj=parser.parse_args(['-md5','-v'])
print(obj)


    
readCommandline()

