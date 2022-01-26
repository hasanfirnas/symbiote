import requests
from playsound import playsound
from bs4 import BeautifulSoup
import time

RED, WHITE, CYAN, GREEN, DEFAULT , YELLOW, YELLOW2, GREEN2= '\033[1;91m', '\033[46m', '\033[1;36m', '\033[1;32m', '\033[0m' , '\033[1;33m' , '\033[1;93m', '\033[1;92m'

def stock1():
    cookies = {
        'A18ID': '1643181545454.896140',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.moneycontrol.com/stocks/cptmarket/compsearchnew.php?search_data=&cid=&mbsearch_str=&topsearch_type=1&search_str=bel',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'DNT': '1',
        'Sec-GPC': '1',
        'Cache-Control': 'max-age=0',
        'TE': 'trailers',
    }

    response = requests.get('https://www.moneycontrol.com/india/stockpricequote/computers-hardware/redingtonindia/RI37', headers=headers, cookies=cookies)
    soup = BeautifulSoup(str(response.text), 'html.parser')
    all_p=soup.find_all('div', attrs={'class' : 'inprice1 nsecp'})
    if float(all_p[0].text) >= float(180.00):
        print(("{3}+{4}"*25).format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print("Current price: "+str(all_p[0].text))
        print(("{3}+{4}"*25).format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        system("mpv song.wav")
    else:
        print(("{0}-{0}"*25).format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
        print("Current price: "+str(all_p[0].text))
        print(("{0}-{0}"*25).format(RED, WHITE, CYAN, GREEN, DEFAULT ,YELLOW))
count=0
while True:
    stock1()
    count+=1
    time.sleep(20)
    os.system("clear")
    print("\t\tCount :" +str(count))
