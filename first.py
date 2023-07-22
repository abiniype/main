

import time
import webbrowser
import schedule
import sys
sys.path.append("/home/ubuntu/.local/lib/python3.5/site-packages")


def open_gmail():
    Url = 'https:mail.google.com'
    webbrowser.open(Url)


schedule.every().day.at("10:00").do(open_gmail)

while True:
    schedule.run_pending()
    time.sleep(1)
