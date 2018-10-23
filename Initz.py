#!/usr/bin/env python2.7
#|=============|
#| ./InYourHeart   |   
#|./InMyHeart       |
#|./Falka                 |
#|./Mr G4T.             |
#|=============|
#NoRecodeMyTools Bitch
#2Easy4Hack Team
# Terminal color definitions

#class fg :
#BLACK   = '\033[30m'
#RED     = '\033[31m'
#GREEN   = '\033[32m'
# YELLOW  = '\033[33m'
#BLUE    = '\033[34m'
#MAGENTA = '\033[35m'
#CYAN    = '\033[36m'
#WHITE   = '\033[37m'
#RESET   = '\033[39m'

#Class Bg :
#BLACK   = '\033[40m'
#RED     = '\033[41m'
#GREEN   = '\033[42m'
#YELLOW  = '\033[43m'
#BLUE    = '\033[44m'
#MAGENTA = '\033[45m'
#CYAN    = '\033[46m'
#WHITE   = '\033[47m'
#RESET   = '\033[49m'

#class style :
#BRIGHT    = '\033[1m'
#DIM       = '\033[2m'
#NORMAL    = '\033[22m'
#RESET_ALL = '\033[0m'
##################

import sys
import argparse
import os
import time
import httplib
import subprocess
import re
import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
import Queue
import threading
#############
import base64
from getpass import getpass
from commands import *
from sys import argv
from platform import system
from urlparse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep
##############


os.system('clear')

def menu():
    print ("""
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |    ####  ####   ##   ####   ######  #####    |
    |      ##     ## ##  ##     ##           ##              ##       |
    |     ##     ##  ## ##     ##           ##              ##        |
    | ####  ##   ####   ####        ##             #####  |
    +-+-+-+-+-+-+-+By : InYourHeart Ft ITzCsTFuCk-+-+""")
    
    os.system('clear')
    os.system('clear')
    os.system('clear')
    
###################
   
def logo():
	print """
	+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |    ####  ####   ##   ####   ######  #####    |
    |      ##     ## ##  ##     ##           ##              ##       |
    |     ##     ##  ## ##     ##           ##              ##        |
    | ####  ##   ####   ####        ##             #####  |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    (NB : Gunakan Dengan Bijak).
    """
    
######################
    
initzlogo  =  """\033[46m
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |    ####  ####   ##   ####   ######  #####    |
    |      ##     ## ##  ##     ##           ##              ##       |
    |     ##     ##  ## ##     ##           ##              ##        |
    | ####  ##   ####   ####        ##             #####  |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     \033[91m"""
def menu():
	def menu():
    print (initzlogo + """\033[46m
 [!] Thanks For All Member 2Easy4Hack
\033[0m
   {1}--Defacement Website
   {2}--Private Defacement Website
   {99}-Exit
 """)
 choice = raw_input("'\033[41m'root@2E4H~# ")
 os.system('clear')
  elif choice == "1":
 	webhack()
 elif choice == "2":
 	privwebhack()
 elif choice == "99":
    clearScr(), sys.exit() 
 elif choice == "":
 	menu()
 else:
 	menu()
 
 def webhack():
 	print(initzlogo)
     print(" {1}--File Upload Finder ")
     print(" {2}--Shell Dir Finder ")
     print(" {3}--Wordpress Exploit ")
     print(" {99}--Menu ")
     deface = raw_input("root@InMyHeart")
     if deface == "1":
     	clearScr()
         sqlscan()
     if deface == "2":
     	clearScr()
         shelltarget()
     if deface == "3":
     	clearScr()
         wpscanner()
     elif deface == "99":
     	menu()
     elif deface == "":
     	menu()
     else:
     	menu()

##############
#FileUploadFinder#
##############


class bcolors:
    HEADER = ''
    OKBLUE = ''
    OKGREEN = ''
    WARNING = ''
    FAIL = ''
    ENDC = ''
    CYAN = ''


class colors():
    PURPLE = ''
    CYAN = ''
    DARKCYAN = ''
    BLUE = ''
    GREEN = ''
    YELLOW = ''
    RED = ''
    BOLD = ''
    ENDC = ''


def grabsqli(ip):
    try:
        print bcolors.OKBLUE + "Check_Uplaod... "
        print '\n'

        page = 1
        while page <= 21:
            bing = "http://www.bing.com/search?q=ip%3A" + \
                ip + "+upload&count=50&first=" + str(page)
            openbing = urllib2.urlopen(bing)
            readbing = openbing.read()
            findwebs = re.findall('<h2><a href="(.*?)"', readbing)
            sites = findwebs
            for i in sites:
                try:
                    response = urllib2.urlopen(i).read()
                    checksqli(i)
                except urllib2.HTTPError, e:
                    str(sites).strip(i)

            page = page + 10
    except:
        pass


def checksqli(sqli):
    responsetwo = urllib2.urlopen(sqli).read()
    find = re.findall('type="file"', responsetwo)
    if find:
        print(" Found ==> " + sqli)


def sqlscan():
    ip = raw_input('Masukan IP -> ')
    grabsqli(ip)
    
################
#KeyBoard Interrupt#
###############

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(" Finishing up...\r"),
        time.sleep(0.25)