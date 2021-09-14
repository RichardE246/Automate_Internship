#Libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date

import pyautogui

import time
import os

# Initialization


dur = 10 #stay 10 minuites total

def min(a):
    b = a * 60
    return b

#Directory Creation

print("Creating directory")

parent_dir = r"C:\Users\brich\OneDrive\Desktop\GAOtek_Screenshots"

date = str(date.today())

child_dir = date

scr_path = os.path.join(parent_dir, date)

os.mkdir(scr_path)

print("Directory created")



#Activating Browser


url1 = [ 'https://gaotek.com/conference/', 'https://gaotek.com/category/drones/', 'https://gaotek.com/teksearch/#gsc.tab=0', 'https://gaotek.com/technology-videos/']
url2 = ['TekSummits','Drones','']
url3 = ['https://gaotek.com/blog/', 'https://gaotek.com/conference/become-a-sponsor/', 'https://gaotek.com/conference/faq/', 'https://gaotek.com/conference/summit-attendee/']
url4 = ['Advertising', 'Retail', 'Manufacturing', 'Oil & Gas', 'Security']


for i in range(len(url1)):

    shot = i + 1

    browser = webdriver.Firefox(executable_path = 'C:\geckodriver.exe')

    a = ActionChains(browser)

    browser.maximize_window()

    browser.get(url1[i])

    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    time.sleep(1)

    browser.execute_script("window.scrollTo(0,0)")

    time.sleep(1)

    screenshot = pyautogui.screenshot()

    time.sleep(1)

    screenshot.save(r'{}\screenshot{}.png'.format(scr_path, shot))

    browser.close()










