import subprocess
import ctypes
#import requests 
import urllib
#from urllib import urlopen
from os import system, getuid, path
from time import sleep
from platform import system as systemos, architecture
from subprocess import check_output

RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2= '\033[91m', '\033[46m', '\033[36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m'
def checkjp2a():
    system('clear')
    if 256 != system('which jp2a > /dev/null'):
        print(" {0}[{2}*{0}] {2}JP2A INSTALLATION FOUND....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)
    else:
        print("{0}[{2}*{0}] {2}JP2A NOT FOUND\n {0}[{2}*{0}] {2}Installing PHP... ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        system('apt-get install jp2a > /dev/null')
        exit()

def checkwget():
    system('clear')
    if 256 != system('which wget > /dev/null'):
        print(" {0}[{2}*{0}] {2}WGET INSTALLATION FOUND....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)
    else:
        print("{0}[{2}*{0}] {2}WGET NOT FOUND\n {0}[{2}*{0}] {2}Installing PHP... ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        system('apt-get install wget > /dev/null')
        exit()

def checkPHP():
    if 256 != system('which php > /dev/null'):
        print(" {0}[{2}*{0}] {2}PHP INSTALLATION FOUND.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)
    else:
        print("{0}[{2}*{0}] {2}PHP NOT FOUND\n {0}[{2}*{0}] {2}Installing PHP... ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        system('apt-get install php > /dev/null')
        exit()

def checkNgrok():
    if path.isfile('Server/ngrok') == False:
        print(' {0}[{2}*{0}]{2} Ngrok Not Found {0}!!'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print(' {0}[{2}*{0}]{2} Downloading Ngrok...{5}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'ngrok-stable-linux-arm64.zip'
            url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
            req=system('wget {0}'.format(url))
            #with open(filename, "wb") as file_obj:
            #file_obj.write(req.content)
            system('unzip ' + filename)
            system('mv ngrok Server/ngrok')
            system('rm ' + filename)
            system('chmod +x ngrok')
            system('clear')
            print("{4} ".format(GREEN, DEFAULT, RED)) 
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
            else:
                filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        req=system('wget {0}'.format(url))
        #with open(filename, "wb") as file_obj:
            #file_obj.write(req.content)
        system('unzip ' + filename)
        system('mv ngrok Server/ngrok')
        system('rm ' + filename)
        system('clear')
        #print("{4} ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)) 
    else:
        print(" {0}[{2}*{0}] {2}NGROK INSTALLATION FOUND......".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)

def checkLocalxpose():
    if path.isfile('Server/loclx') == False:
        print(' {0}[{2}*{0}]{2} Localxpose Not Found {0}!!'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print(' {0}[{2}*{0}]{2} Downloading Localxpose...{5}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'loclx-linux-arm64.zip'
            url = 'https://lxpdownloads.sgp1.digitaloceanspaces.com/cli/'+filename
            req=system('wget {0}'.format(url))
            #with open("{0}", "wb".format(filename)) as file_obj:
            #file_obj.write(req.content)
            system('unzip {0} && rm {0}'.format(filename))
            sleep(2)
            system('mv loclx-linux-* loclx && mv loclx Server/')
            system('chmod +x loclx')
            #print("{4} ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'loclx-linux-amd64.zip'.format(ostype)
            else:
                filename = 'loclx-linux-386.zip'.format(ostype)
        url = 'https://lxpdownloads.sgp1.digitaloceanspaces.com/cli/'+filename
        req=system('wget {0}'.format(url))
        #with open("{0}", "wb".format(filename)) as file_obj:
            #file_obj.write(req.content)
        system('unzip {0} && rm {0}'.format(filename))
        system('mv loclx-linux-* loclx && mv loclx Server/')
        print("{1} ".format(GREEN, DEFAULT, RED)) 
    else:
        print(" {0}[{2}*{0}] {2}LOCALXPOSE INSTALLATION FOUND.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)



