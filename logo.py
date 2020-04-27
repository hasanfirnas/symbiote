#!/usr/bin/python3
# This Python file uses the following encoding: utf-8
import random 
import subprocess
import ctypes
import sys
import os
#import requests 
import urllib
#from urllib import urlopen
from os import system, getuid, path
from time import sleep
from platform import system as systemos, architecture
from subprocess import check_output
#from gif_for_cli.execute import execute

def banner():
    '''
    a=1
    a=random.choice([1, 4, 2, 5, 3])
    if a == 1:
        system('jp2a --size=80x50 https://logodix.com/logo/50111.jpg')
    elif a == 2:
        system('jp2a --size=80x50 https://logodix.com/logo/50111.jpg')
    elif a == 3:
        system('jp2a --size=80x50 https://i.pinimg.com/originals/83/16/c4/8316c474f79fcb441903d27b010c55cd.jpg')
    elif a == 4:
        system('jp2a --size=80x50 https://sf.co.ua/14/07/wallpaper-1871574.jpg')
    elif 2 == 5:
        system('jp2a --size=80x50 https://lh4.googleusercontent.com/proxy/LNebVAWORnLveXy9wqVAhDwK2Fg8BH06qF7rze1D8fQ6iF5fUNelwFTD0cAityBeW7S1vFPzkKaX1ZTyVa86r51GxGUG0yckCHvu4NL-M6mGCz_lK-drUSMlHtwM5Q1wCoucU4eSnHtNVWyoMXYHFA')
    #system('jp2a https://cmkt-image-prd.freetls.fastly.net/0.1.0/ps/6815549/600/400/m1/fpnw/wm1/skull-icon-wih-headphones-colorful-neon-re-.jpg?1565732224&s=58967501b5853c6435611a04d239cf6c')
    #system('jp2a https://ae01.alicdn.com/kf/HTB1eJAzRVXXXXbaapXXq6xXFXXXH.jpg_q50.jpg')
    #system('jp2a https://i.ytimg.com/vi/a1z8f7YBhgI/hqdefault.jpg')
    #system('jp2a https://explosivefunctionalfitness.com/wp-content/uploads/2017/08/2996-anonymous-tie-suit.jpg')
    #system('jp2a https://3.bp.blogspot.com/-WGTFiSgNOQU/UpqQCIA9Z6I/AAAAAAAAAJ8/epWIqZ_VKIU/s1600/da.jpeg')
    #system('jp2a https://cdn4.vectorstock.com/i/1000x1000/35/18/yellow-radiation-sign-on-black-background-flat-vector-19873518.jpg')
'''
    RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2, BRED= '\033[91m', '\033[46m', '\033[36m', '\033[1;91m', '\033[0m' , '\033[1;32m' , '\033[1;93m', '\033[1;92m',"\033[5;35m"
    BLINK ,Magenta ="\033[5m","\033[1;34m"
    y='\033[1;33m'
    system('clear')
    print('''
                                                                
                                {5}...                             
                           {5}.ckXWMMMMWKx:                        {6}|    
                         {5};0MMMWKOOOKWMMMWk'                     {6}|     
                       {5}'KMMWd'       .oNMMMk.                   {6}|     
                      {5}lMM0d.  {4}.:cllc,.  {5}cKWMN.                  {6}|     
                     {5}oMWc  {4}'kWMMMMMMMMKl. {5}.XMW.                 {6}|    
                    {5};MW, {4}.OMMMMMMMMMMMMMWd. {5}KMN                 {6}|              {3}░░░░░░░ ░░    ░░ ░░░    ░░░ ░░░░░░  ░░  ░░░░░░  ░░░░░░░░ ░░░░░░░{4}  
                    {5}XM: {4};NMMMMMMMMMMMMMMMMN;{5}.XMx                {6}|              {3}░░       ░░  ░░  ░░░░  ░░░░ ░░   ░░ ░░ ░░    ░░    ░░    ░░{4}
                   {5};Mx {4}lMMMMMMMMMMMMMMMMMMMM:{5}.WM.               {6}|              {3}▒▒▒▒▒▒▒   ▒▒▒▒   ▒▒ ▒▒▒▒ ▒▒ ▒▒▒▒▒▒  ▒▒ ▒▒    ▒▒    ▒▒    ▒▒▒▒▒{4} 
                   {5}kN {4}:MMMMMMMMMMMMMMMMMMMMMW'{5}lMo               {6}|              {3}     ▓▓    ▓▓    ▓▓  ▓▓  ▓▓ ▓▓   ▓▓ ▓▓ ▓▓    ▓▓    ▓▓    ▓▓{4} 
                  {5}.Wc{4} KMMMMMMMMMMMMMMMMMMMMMM0 {5}KN {4}              {6}|{4}              {3}███████    ██    ██      ██ ██████  ██  ██████     ██    ███████{4}
                  KMNMMMMMMMMMMMMMMMMMMMMMMMMMNNMK              {6}|{4}                                                                 {7}================{4}
                 .MMMMMMMMMMMWWWWWWWWWWMMMMMMMMMMM.             {6}|{4}                                                                   {5}BY: {0}404-ghost{4}     
                 :MMMMMWOWMMMWWMMMMMMWWMMMW0NMMMMM:             {6}|{4}                                                                 {7}================{4} 
                 cMMMMK{5}{1}.":{4}cXMWWWWMWMMWWMK{5}{1}:".{4}xMMMMMl             {6}|{4}                         {7}GITHUB LINK{6}{0} :  {4}{5}https://github.com/404-ghost{4} 
                 cMMMMMW{5}{1}"   "{4}OWWMWWWWWX{5}{1}"  "{4}XMMMMMMc             {6}|{4}                      {7}INSTAGRAM ID{6}{0} : {4}{5}https://www.instagram.com/_yoo_yoo._{4}
                 ;MMMMMMx{5}{1}"    "{4}kWWWO{5}{1}"    "{4}MMMMMWMM,             {6}|{4}           
                 .MNMMMMMKd{5}{1}".."{4}0WWXl{5}{1},..,"{4}lOWMMMWM.              {6}|{4}           
                  XlNMMMMMMMMWWWWxKWMWWMMMMMMMMWdK              {6}|{4}           
                  ..:koXMMMMMWWMOdkoMWWMMMMMWxN:..              {6}|{4}           
                       KMMMWddWW0XWxWWWXooWMW x                 {6}|{4}     
                       xMMNl{0}",{4}WWWWWWWWW{0},"{4}lWWW: {5}'\'{4}               {6}|{4}     
                        lXMM{0};;{4}WWWWWWWWM{0};;{4}WMMk{5}.|.{4}                {6}|{4}     
                       {3}oWMMM{4}KkWWWWWWWWWW{3}MMMMMM.{5}'\'{4}               {6}|{4}     
                      {3}cMMMMMMM{4}WMMMWMMWM{3}MMMMMMWO  {5}.\.{4}            {6}|{4}     
                     {3}:MMMMMMMM{4}MMMMMMMM{3}MMMMMMWMM:  {5}'\'{4}            {6}|{4}     
                      {3}MMMMMMMMX{4}MMMMMM{3}NKMMMMMMM:   {5}.|.{4}           {6}|{4}     
                       {3}KMMMMMMwc{4}WMMM{3}kkMMMMMMM;    {5}.|.{4}           {6}|{4}     
                       {3}cMMMMMMd{4}  ...  {3}WMMMMMo    {5}'|'{4}            {6}|{4}     
                        {3}XMMMMMk{4}      {3}.KMMMMW.   {5}./.{4}             {6}|{4}     
                        {3};MMMK;{4}         {3}'kMMl    {5}.|.{4}             {6}|{4}     
                         {3}kX:{4}             {3}lx:     {5}.|.{4}            {6}|{4}     
                          {3}"{4}               {3}"{4}      {5}'/'{4}            {6}|     
                                                {5}./.             {6}|     
                                                {5}.|.             {6}|     
                                               {5}'/'              {6}|     
                                               {5}'|'              {6}|     
                                               {5}.|'              {6}|     


    '''.format(RED, BRED, CYAN, GREEN, DEFAULT ,YELLOW,Magenta,y))

def android_banner():
    RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2, BRED= '\033[91m', '\033[46m', '\033[36m', '\033[1;91m', '\033[0m' , '\033[1;32m' , '\033[1;93m', '\033[1;92m',"\033[5;35m"
    BLINK ,Magenta ="\033[5m","\033[1;34m"
    y='\033[1;33m'
    system('clear')
    print('''
                                                              
                              {5}...      
                         {5}.ckXWMMMMWKx:  
                       {5};0MMMWKOOOKWMMMWk'
                     {5}'KMMWd'       .oNMMMk.  
                    {5}lMM0d.  {4}.:cllc,.  {5}cKWMN.  
                   {5}oMWc  {4}'kWMMMMMMMMKl. {5}.XMW.  
                  {5};MW, {4}.OMMMMMMMMMMMMMWd. {5}KMN   
                  {5}XM: {4};NMMMMMMMMMMMMMMMMN;{5}.XMx 
                 {5};Mx {4}lMMMMMMMMMMMMMMMMMMMM:{5}.WM.
                 {5}kN {4}:MMMMMMMMMMMMMMMMMMMMMW'{5}lMo  
                 {5}kN {4}:MMMMMMMMMMMMMMMMMMMMMW'{5}lMo  
                {5}.Wc{4} KMMMMMMMMMMMMMMMMMMMMMM0 {5}KN {4}
                KMNMMMMMMMMMMMMMMMMMMMMMMMMMNNMK
               .MMMMMMMMMMMWWWWWWWWWWMMMMMMMMMMM.
               :MMMMMWOWMMMWWMMMMMMWWMMMW0NMMMMM:
               cMMMMK{5}{1}.":{4}cXMWWWWMWMMWWMK{5}{1}:".{4}xMMMMMl
               cMMMMMW{5}{1}"   "{4}OWWMWWWWWX{5}{1}"  "{4}XMMMMMMc 
               ;MMMMMMx{5}{1}"    "{4}kWWWO{5}{1}"    "{4}MMMMMWMM,
               .MNMMMMMKd{5}{1}".."{4}0WWXl{5}{1},..,"{4}lOWMMMWM.
                XlNMMMMMMMMWWWWxKWMWWMMMMMMMMWdK 
                ..:koXMMMMMWWMOdkoMWWMMMMMWxN:.. 
                     KMMMWddWW0XWxWWWXooWMW x  
                     xMMNl{0}",{4}WWWWWWWWW{0},"{4}lWWW: {5}'\'{4} 
                      lXMM{0};;{4}WWWWWWWWM{0};;{4}WMMk{5}.|.{4} 
                     {3}oWMMM{4}KkWWWWWWWWWW{3}MMMMMM.{5}'\'{4}
                    {3}cMMMMMMM{4}WMMMWMMWM{3}MMMMMMWO  {5}.\.{4}
                   {3}:MMMMMMMM{4}MMMMMMMM{3}MMMMMMWMM:  {5}'\'{4}
                    {3}MMMMMMMMX{4}MMMMMM{3}NKMMMMMMM:   {5}.|.{4}
                     {3}KMMMMMMwc{4}WMMM{3}kkMMMMMMM;    {5}.|.{4}
                     {3}cMMMMMMd{4}  ...  {3}WMMMMMo    {5}'|'{4}
                      {3}XMMMMMk{4}      {3}.KMMMMW.   {5}./.{4}
                      {3};MMMK;{4}         {3}'kMMl    {5}.|.{4} 
                       {3}kX:{4}             {3}lx:     {5}.|.{4} 
                        {3}"{4}               {3}"{4}      {5}'/'{4}  
                                              {5}./.  
                                              {5}.|.
                                             {5}'/' 
                                             {5}'|' 
                                             {5}.|' {4}

   {3}░░░░░░░ ░░    ░░ ░░░    ░░░ ░░░░░░  ░░  ░░░░░░  ░░░░░░░░ ░░░░░░░{4}
   {3}░░       ░░  ░░  ░░░░  ░░░░ ░░   ░░ ░░ ░░    ░░    ░░    ░░{4}
   {3}▒▒▒▒▒▒▒   ▒▒▒▒   ▒▒ ▒▒▒▒ ▒▒ ▒▒▒▒▒▒  ▒▒ ▒▒    ▒▒    ▒▒    ▒▒▒▒▒{4}
   {3}     ▓▓    ▓▓    ▓▓  ▓▓  ▓▓ ▓▓   ▓▓ ▓▓ ▓▓    ▓▓    ▓▓    ▓▓{4}
   {3}███████    ██    ██      ██ ██████  ██  ██████     ██    ███████{4}
                                                    {7}================{4}
                                                      {5}BY: {0}404-ghost{4}
                                                    {7}================{4}
              {7}GITHUB LINK{6}{0} :  {4}{5}https://github.com/404-ghost{4}
           {7}INSTAGRAM ID{6}{0} : {4}{5}https://www.instagram.com/_yoo_yoo._{4}
'''.format(RED, BRED, CYAN, GREEN, DEFAULT ,YELLOW,Magenta,y))
def sbanner():
    RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2= '\033[1;31m', '\033[46m', '\033[1;36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m'
    lred,blink,lyellow="\033[91m",'\033[5m',"\033[93m"

    print('''
    {10}(   ( (  (  (   ( . (    (( (   (  ((   (   ( (  (   (  (( (  ({4}  
    {9})\ )\))\ )\:)\ ()) .)\   ))\)\ )\ ( )\  )\ )\))\ )\: )\ ))\)\ )\{4}
   {0}((_)(_)(_)(_)(_)_)()((_)(((_)(_)(_))((_)((_)(_)(_)(_)((_)(_)(_)(_){4}
   {8}░░░░░░░ ░░    ░░ ░░░    ░░░ ░░░░░░  ░░  ░░░░░░  ░░░░░░░░ ░░░░░░░{4}
   {8}░░       ░░  ░░  ░░░░  ░░░░ ░░   ░░ ░░ ░░    ░░    ░░    ░░{4}
   {8}▒▒▒▒▒▒▒   ▒▒▒▒   ▒▒ ▒▒▒▒ ▒▒ ▒▒▒▒▒▒  ▒▒ ▒▒    ▒▒    ▒▒    ▒▒▒▒▒{4}
   {8}     ▓▓    ▓▓    ▓▓  ▓▓  ▓▓ ▓▓   ▓▓ ▓▓ ▓▓    ▓▓    ▓▓    ▓▓{4}
   {8}███████    ██    ██      ██ ██████  ██  ██████     ██    ███████{4}
                                               {7}================{4}
                                                {5}BY: {0}404-ghost{4} 
                                               {7}================{4}        
           {7}GITHUB LINK{6}{0} : {4}{5}https://github.com/404-ghost{4}               
       {7}INSTAGRAM ID{6}{0} : {4}{5}https://www.instagram.com/_yoo_yoo._{4}
'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,blink,GREEN2,YELLOW2,lred,lyellow))
def end():
    RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2= '\033[1;91m', '\033[46m', '\033[1;36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m'
    blink='\033[5m'
    
    print('''{2}
                                                                                           
                                                                                              {5}|{4} 
                                                                                              {5}|{4}
                                                                                              {5}|{4}
                                                                                              {5}|{4}
                                                                                              {5}|{4}
                                                                                              {5}|{4}
                                       {2}'cdxOOkdl,{4}                                             {5}|{4}                .                          {0}<Symbiote> {5}BY: {0}404-ghost
                                    {2}.lKMMMMMMMMMMXd.{4}                                          {5}|{4}                .                       
                                   {2}lNMMMMMMMMMMNXXNNo{4}                                         {5}|{4}                .      {0}[[{6}{2}*{4}{0}]] {7}IF YOU LIKE THIS TOOL, THEN PLEASE HELP TO BECOME BETTER.       
                                 {2}'0MMMMMMMNkl,..   .'.{4}                                        {5}|{4}                .      {0}[[{6}{2}*{4}{0}]] {7}PLEASE LET ME KNOW , IF ANY PROBLEM IN THIS. 
                                {2}oWMMMMMMO;{4}                                                    {5}|{4}                .      {0}[[{6}{2}*{4}{0}]] {7}MAKE PULL REQUEST, LET US KNOW YOU SUPPORT US. 
                              {2}.OMMMMMMK;{4}                                                      {5}|{4}                .      {0}[[{6}{2}*{4}{0}]] {7}IF YOU HAVE ANY IDEA, THEN JUST LET ME KNOW .   
                             {2}.0MMMMMWd{4}                                                        {5}|{4}                .      {0}[[{6}{2}*{4}{0}]] {7}PLEASE DON'T HARM ANYONE , IT'S ONLY FOR EDUCATIONAL PURPOSE.
                            {2}.KMMMMMX; .';:cc:;,..{4}                                             {5}|{4}                .      {0}[[{6}{2}*{4}{0}]] {7}WE WILL NOT BE RESPONSIBLE FOR ANY MISUSE OF THIS TOOL.  
                           {2}.XMMMMMWkOXWMMMMMMMMMWXOo;.{4}                                        {5}|{4}                .      {0}[[{6}{2}*{4}{0}]] {7}THANKS FOR USE THIS TOOL. {0}"HAPPY HACKING ... GOOD BYE" {4}
                          {2}'NMMMMMMMMMMMMMMMMMMMMMMMMMW0o'{4}                                     {5}|{4}                .       
                         {2}'NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;{4}                                   {5}|{4}                .                   {7}GITHUB LINK{6}{0} :  {4}{5}https://github.com/404-ghost{4}
                        {2},NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO,{4}                                 {5}|{4}                .                  
                       {2}lWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO'{4}                               {5}|{4}                .                {7}INSTAGRAM ID{6}{0} : {4}{5}https://www.instagram.com/_yoo_yoo._
                     {2},0MMMMMMMMMMMMMMMWXOkxMMkllllodxOMMMMMMMMWd.{4}                             {5}|{4}
            {2}.dc;'';lOWMMMMMMMMMMMMMMMc.   {6}{0}.WM,{4}      {2};KMMMMMMMMMMK'{4}                            {5}|{4}        
             {2}cWMMMMMMMMMMMMMMMMM0c,{6}{0}WMo    oMW.{4}     {2}dWMMMMMMN0OOOKK,{4}                           {5}|{4}
              {2}:NMMMMMMMMMMMMMMMx   {6}{0}xMWo..oWMd{4}    {2}.0MMMMMWk,{4}                                   {5}|{4}           
               {2}.xWMMMMMMMMMMMMMO   {6}{0}.XMMWMMMX.{4}    {2}OMMMMMN;{4}                                     {5}|{4}           
                 {2}.cxKNNNKkldMMMW'   {6}{0}.0MMMM0.{4}    {2}dMMMMMK.{4}                                      {5}|{4}           
                            {2}xMMMK.    {6}{0}'cc'{4}     {2}dMMMMM0.{4}                                       {5}|{4}           
                             {2}dMMMK.           {2}xMMMMM0.{4}                                        {5}|{4}  
                              {2};KMMWd.        {2}kMMMMM0.{4}                                         {5}|{4}  
                                {2}'ldkd,     {2}.0MMMMM0.{4}                                          {5}|{4}  
                                          {2}cNMMMMM0{4}                                            {5}|{4}
                              {2} .       .cKMMMMMMO.{4}                                            {5}|{4}
                              {2} l0dlccoOWMMMMMMMx{4}                                              {5}|{4}
                               {2}cNMMMMMMMMMMMX:{4}                                                {5}|{4}
                                 {2}.l0WMMMMMWO:{4}                                                 {5}|{4}
                                    {2}.,:c;'.{4}                                                   {5}|{4}
                                                                                              {5}|{4}
                                                                                              {5}|{4}
                                                                                              {5}|{4}                  
'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,blink,GREEN2))

def android_end():
    RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2= '\033[1;91m', '\033[46m', '\033[1;36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m'
    blink='\033[5m'
    print('''
                                 {2}'cdxOOkdl,{4}
                              {2}.lKMMMMMMMMMMXd.{4}
                             {2}lNMMMMMMMMMMNXXNNo{4}
                           {2}'0MMMMMMMNkl,..   .'.{4}
                          {2}oWMMMMMMO;{4}
                        {2}.OMMMMMMK;{4}                                
                       {2}.0MMMMMWd{4}
                      {2}.KMMMMMX; .';:cc:;,..{4}
                     {2}.XMMMMMWkOXWMMMMMMMMMWXOo;.{4}
                    {2}'NMMMMMMMMMMMMMMMMMMMMMMMMMW0o'{4}
                   {2}'NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;{4}
                  {2},NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO,{4}
                 {2}lWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO'{4}
               {2},0MMMMMMMMMMMMMMMWXOkxMMkllllodxOMMMMMMMMWd.{4}
      {2}.dc;'';lOWMMMMMMMMMMMMMMMc.   {6}{0}.WM,{4}      {2};KMMMMMMMMMMK'{4}
       {2}cWMMMMMMMMMMMMMMMMM0c,{6}{0}WMo    oMW.{4}     {2}dWMMMMMMN0OOOKK,{4}
        {2}:NMMMMMMMMMMMMMMMx   {6}{0}xMWo..oWMd{4}    {2}.0MMMMMWk,{4}
         {2}.xWMMMMMMMMMMMMMO   {6}{0}.XMMWMMMX.{4}    {2}OMMMMMN;{4}
           {2}.cxKNNNKkldMMMW'   {6}{0}.0MMMM0.{4}    {2}dMMMMMK.{4}
                      {2}xMMMK.    {6}{0}'cc'{4}     {2}dMMMMM0.{4}
                       {2}dMMMK.           {2}xMMMMM0.{4}
                        {2};KMMWd.        {2}kMMMMM0.{4}
                          {2}'ldkd,     {2}.0MMMMM0.{4}
                                    {2}cNMMMMM0{4}
                        {2} .       .cKMMMMMMO.{4}
                        {2} l0dlccoOWMMMMMMMx{4}
                         {2}cNMMMMMMMMMMMX:{4}
                           {2}.l0WMMMMMWO:{4}
                              {2}.,:c;'.{4}

                        {0}<Symbiote> {5}BY: {0}404-ghost
    {0}[[{6}{2}*{4}{0}]] {7}IF YOU LIKE THIS TOOL, THEN PLEASE HELP TO BECOME BETTER.
    {0}[[{6}{2}*{4}{0}]] {7}PLEASE LET ME KNOW , IF ANY PROBLEM IN THIS.
    {0}[[{6}{2}*{4}{0}]] {7}MAKE PULL REQUEST, LET US KNOW YOU SUPPORT US.
    {0}[[{6}{2}*{4}{0}]] {7}IF YOU HAVE ANY IDEA, THEN JUST LET ME KNOW .
    {0}[[{6}{2}*{4}{0}]] {7}PLEASE DON'T HARM ANYONE, IT'S ONLY FOR EDUCATIONAL PURPOSE.
    {0}[[{6}{2}*{4}{0}]] {7}WE WILL NOT BE RESPONSIBLE FOR ANY MISUSE OF THIS TOOL.
    {0}[[{6}{2}*{4}{0}]] {7}THANKS FOR USE THIS TOOL. {0}"HAPPY HACKING ... GOOD BYE" {4}

                 {7}GITHUB LINK{6}{0} :  {4}{5}https://github.com/404-ghost{4}

              {7}INSTAGRAM ID{6}{0} : {4}{5}https://www.instagram.com/_yoo_yoo._ 
'''.format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW,blink,GREEN2))

