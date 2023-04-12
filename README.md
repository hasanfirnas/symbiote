



<p align="center">
  #TO BE USED FOR EDUCATIONAL PURPOSES ONLY#
</p>

# **AVAILABLE TUNNELLING OPTIONS**
1) NGROK [ACCOUNT NEEDED] (https://ngrok.com)
2) Localhost.run (http://localhost.run)
3) LOCALXPOSE [ACCOUNT NEEDED] (https://localxpose.io)
# Installing (Kali Linux/Termux):
## step 1 (install this before you start):
```
sudo apt update && upgrade
sudo apt install python -y
sudo apt install wget -y
sudo apt install php -y
sudo apt install openssh -y
sudo apt install jq -y
sudo ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa <<<y >/dev/null 2>&1
```
## step 2:
```
git clone https://github.com/hasanfirnas/symbiote
cd symbiote
python3 symbiote.py
```
## step 3:
### After you got your cam file:
```
cd symbiote
cd CapturedData 
ls
termux-open <file_name>
```
# PREREQUISITES:
* Python 3
* PHP
* wget

# SCREENSHOT (Kali-linux):
![Shot](https://imgur.com/kBiCDpP.png)
