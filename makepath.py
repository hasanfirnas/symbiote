
import subprocess
import ctypes
#import requests 
import urllib
#from urllib import urlopen
from os import system, getuid, path, popen
from time import sleep
from platform import system as systemos, architecture
from subprocess import check_output

RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2= '\033[91m', '\033[46m', '\033[36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m'
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
    system('rm -rf Server/www_f/ip.txt && touch Server/www_f/ip.txt')
    system('rm -rf Server/www_b/ip.txt && touch Server/www_b/ip.txt')
    system('rm -rf Server/www_f/Log.log && touch Server/www_f/Log.log')
    system('rm -rf Server/www_b/Log.log && touch Server/www_b/Log.log') 
    system('rm -rf Server/www_f/path.txt && touch Server/www_f/path.txt')
    system('rm -rf Server/www_b/path.txt && touch Server/www_b/path.txt')
    system('rm -rf link.url && touch link.url')
