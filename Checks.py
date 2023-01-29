import subprocess
import ctypes
import requests 
import urllib
#from urllib import urlopen
from os import system, getuid, path
from time import sleep
from platform import system as systemos, architecture
from subprocess import check_output
import sys, os, time, random, threading
RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2= '\033[91m', '\033[46m', '\033[36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m'
def net():
    system('clear')
    print("{0}[{2}#{0}] {2}Checking for internet connection{2}....".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW ))
    sleep(3)
    m = system('wget -q --spider http://google.com')
    if m == 0:
        print("\n{0}[{2}#{0}] {3}INTERNET {0}- {3}[{2}CONNECTED{3}]".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW ))
        sleep(3)
    else:
        print("\n{0}[{2}#{0}] {3}INTERNET {0}- {3}[{2}NOT-CONNECTED{3}]".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW ))
        print("{0}[{2}#{0}] {2}Turn on your internet connection\n\n".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW ))
        exit()
        
def verCheck():
    #system('clear')
    print("\n{0}[{2}#{0}] {2}Checking For Updates{2}...".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW ))
    response = requests.get('https://raw.githubusercontent.com/hasanfirnas/symbiote/master/version.txt')
    print(response.text.strip())
    with open("version.txt", "r") as f:
        local_version = f.read().strip()
    if local_version[0] == response:
        print("{0}[{2}#{0}] {2}[Up-To-Date]- {0}v {6}{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, response))
        system('git fetch --quiet; git reset --hard origin/master --quiet; git pull --quiet')
        sleep(1)
    else:
        print("\n{0}[{2}#{0}] {2}Their Is A Newer Version Available.".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
        print("{0}[{2}#{0}] {0}[{2}Current{0}]{2}- {0}v {6}\n{0}[{2}#{0}] {0}[{2}Available{0}]{2}- {0}v.{7}".format(RED, WHITE, CYAN, GREEN, DEFAULT, YELLOW, local_version[0], response[0])) 
        print("{0}[{2}#{0}] {2}Updating To The Latest Version {0}[{2}v {6}{0}] \n{0}[{2}#{0}] {2}Please Wait....{7}\n".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, response[0] ,GREEN2))
        system('git fetch --quiet; git reset --hard origin/master --quiet; git pull --quiet')
        print("\n\n\n\t\t{2}[{0}#{2}] {0}Restart program \n {2}Enter this command to run {0}-> {3}python3 symbiote.py".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
        exit()

def checkjp2a():
    system('clear')
    if 256 != system('which jp2a > /dev/null'):
        print(" {0}[{2}*{0}] {2}JP2A INSTALLATION FOUND....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)
    else:
        print("{0}[{2}*{0}] {2}JP2A NOT FOUND\n {0}[{2}*{0}] {2}Installing PHP... ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        system('apt-get install jp2a -y > /dev/null')
        exit()

def checkwget():
    system('clear')
    if 256 != system('which wget > /dev/null'):
        print(" {0}[{2}*{0}] {2}WGET INSTALLATION FOUND....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)
    else:
        print("{0}[{2}*{0}] {2}WGET NOT FOUND\n {0}[{2}*{0}] {2}Installing PHP... ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        system('apt-get install wget -y > /dev/null')
        exit()

def checkPHP():
    if 256 != system('which php > /dev/null'):
        print(" {0}[{2}*{0}] {2}PHP INSTALLATION FOUND.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)
    else:
        print("{0}[{2}*{0}] {2}PHP NOT FOUND\n {0}[{2}*{0}] {2}Installing PHP... ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        system('apt-get install php -y > /dev/null')
        exit()

def checkNgrok():
    if path.isfile('Server/ngrok') == False:
        print(' {0}[{2}*{0}]{2} Ngrok Not Found {0}!!'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print(' {0}[{2}*{0}]{2} Downloading Ngrok...{5}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'ngrok-stable-linux-arm.zip'
            url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
            req=system('wget {0}'.format(url))
            #with open(filename, "wb") as file_obj:
            #file_obj.write(req.content)
            system('unzip ' + filename)
            system('mv ngrok Server/ngrok')
            system('rm ' + filename)
            system('chmod +x ngrok')
            system('clear')
            print("\n\n\n\t\t{2}[{0}#{2}] {0}Restart program \n {2}Enter this command to run symbiote {0}-> {3}python3 symbiote.py".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
            exit()  
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
        print("{4} ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)) 
        #exit() 
        sleep(2)
    else:
        print(" {0}[{2}*{0}] {2}NGROK INSTALLATION FOUND......".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)

def checkLocalxpose():
    if path.isfile('Server/loclx') == False:
        print(' {0}[{2}*{0}]{2} Localxpose Not Found {0}!!'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print(' {0}[{2}*{0}]{2} Downloading Localxpose...{5}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        if 'Android' in str(check_output(('uname', '-a'))) or 'arm' in str(check_output(('uname', '-a'))):
            filename = 'loclx-linux-arm.zip'
            url = 'https://lxpdownloads.sgp1.digitaloceanspaces.com/cli/'+filename
            req=system('wget {0}'.format(url))
            #with open("{0}", "wb".format(filename)) as file_obj:
            #file_obj.write(req.content)
            system('unzip {0} && rm {0}'.format(filename))
            system('mv loclx-linux-* loclx && chmod +x loclx && mv loclx Server/')
            system('clear')
            print("\n\n\n\t\t{2}[{0}#{2}] {0}Restart program \n {2}Enter this command to run symbiote{0}-> {3}python3 symbiote.py".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
            exit()
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'loclx-linux-amd64.zip'.format(ostype)
            else:
                filename = 'loclx-linux-386.zip'.format(ostype)
        url = 'https://lxpdownloads.sgp1.digitaloceanspaces.com/cli/'+filename
        req=system('wget {0}'.format(url))
        system('unzip {0} && rm {0}'.format(filename))
        system('mv loclx Server/')
        print("{1} ".format(GREEN, DEFAULT, RED)) 
        #exit()
        sleep(2)
    else:
        print(" {0}[{2}*{0}] {2}LOCALXPOSE INSTALLATION FOUND.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(1)

def loadingHack():
    chaine ="/////////////////////"+"[*]"+" Starting symbiote......"+"/////////////////////".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)
    charspec = "$*X^%\#~?;"
    i=0
    while i<4:
        chainehack = ""
        i +=1
        for c in chaine:
            chainehack += c
            r = random.choice(charspec)+random.choice(charspec)+random.choice(charspec)
            if len(chainehack+r) <= len(chaine):
                pass
            else:
                r = ""
            sys.stdout.write('\r'+chainehack+r)
            time.sleep(0.06)

def loadingTextPrint():
    string ="                    "+"[*]"+" Starting symbiote......"
    a= 0
    while a <3:    
        space = " " * 100
        sys.stdout.write("\r"+space)
        x = 1
        a += 1
        while x <= len(string):
            times = "0.1"
            times += str(random.choice(range(1, 3)))
            sys.stdout.write("\r "+string[:x]+">")
            time.sleep(float(times))
            x += 1
