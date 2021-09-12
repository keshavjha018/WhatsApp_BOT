#Takes - Contact Name(Must be saved in phone's contact list), Message, Time  as input
# and sends message to the given contact at given time
# Accuracy Level ~ Seconds. (Also depends on your network speed)

from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
from selenium.webdriver.common.keys import Keys
import time
from threading import Timer
from datetime import datetime

driver.get("https://web.whatsapp.com/")
print("Scan the QR code to Log in...")

nameofcontact = input('Give name of contact: ')
msg = input("Type the message you want to send: ")
print("Enter Time of sending Message (Hrs, Min & Sec...)")
hrs = int(input("Hrs: "))
mins = int(input("Min: "))
secs = int(input("Sec: "))


x=datetime.today()
y=x.replace(day=x.day+1, hour=hrs, minute=mins, second=secs, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def send_msg():
    global nameofcontact, msg
    css_path = 'span[title="' + nameofcontact + '"]'
    nameofcontact = driver.find_element_by_css_selector(css_path)
    nameofcontact.click()

    chatbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    chatbox.send_keys(msg)
    chatbox.send_keys(Keys.RETURN)

t = Timer(secs, send_msg)
t.start()
