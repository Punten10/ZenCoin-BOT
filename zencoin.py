import requests
import json
import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    banner = """
     _____           ____      _       
    |__  /___ _ __  / ___|___ (_)_ __  
      / // _ \ '_ \| |   / _ \| | '_ \ 
     / /|  __/ | | | |__| (_) | | | | |
    /____\___|_| |_|\____\___/|_|_| |_|
   ┌──────────────────────────┐
   │ By ZUIRE AKA SurrealFlux │
   └──────────────────────────┘
    """
    print(Fore.LIGHTCYAN_EX + banner)

def send_tap_request(taps_and_coins, token):
    url = "https://service.zencoin.ai/zen-coin/clicker/taps"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json;charset=UTF-8",
        "lang": "en",
        "origin": "https://cdn-tg-mini.zencoin.ai",
        "referer": "https://cdn-tg-mini.zencoin.ai/",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127", "Microsoft Edge WebView2";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "token": token,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
    }
    payload = {
        "availableTaps": taps_and_coins,
        "coins": taps_and_coins,
        "isStart": False,
        "lastSyncUpdate": int(time.time())
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        resp_json = response.json().get("result", {})
        tgUserId = resp_json.get("tgUserId", "Unknown")
        firstName = resp_json.get("firstName", "Unknown")
        lastName = resp_json.get("lastName", "Unknown")
        balanceCoins = resp_json.get("balanceCoins", "Unknown")
        isBot = resp_json.get("isBot", "Unknown")

        print(Fore.LIGHTWHITE_EX + "Username : " + Fore.LIGHTGREEN_EX + f"{firstName} {lastName} | {tgUserId}")
        print(Fore.LIGHTWHITE_EX + "Balance  : " + Fore.LIGHTGREEN_EX + f"{balanceCoins}")
        print(Fore.LIGHTWHITE_EX + "Hacker   : " + Fore.LIGHTGREEN_EX + f"{isBot}")
    else:
        print(Fore.RED + f"Request gagal dengan status code {response.status_code}.")
        print("Response:", response.text)

if __name__ == "__main__":
    print_banner()
    
    taps_and_coins = int(input(Fore.YELLOW + "Your Energy Now: "))

    # Membaca token dari file token.txt
    with open('token.txt', 'r') as file:
        token = file.read().strip()

    interval = 5 

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Perintah untuk clear screen
        print_banner()  # Tampilkan banner setiap kali screen di-clear
        send_tap_request(taps_and_coins, token)
        print(Fore.LIGHTCYAN_EX + f"Menunggu {interval} detik sebelum mengirim request berikutnya...")
        time.sleep(interval)
