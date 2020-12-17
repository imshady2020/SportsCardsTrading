# python package
import csv
import time
import random
import sys
import os

# selenium package
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException


# identifiants
email_address = "frederictwc@live.com"
password = "SBaVAmdB!L7iRvh"

# fonction pause
def pause():
    time_break = random.randint(3,5)
    # print "Pause de " + str(time_break) + " seconde(s)."
    return time.sleep(time_break)

# options
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(desired_capabilities=capa, chrome_options=options)
wait = WebDriverWait(driver, 30)
pause()
print ("Driver 1 open")

# url de depart
url = "https://app.cardladder.com/card/QEpWBk1v1yVF1J185Uoa/sales"

# aller sur linkedin
driver.get(url) #1 : page principale
try:
    wait.until(EC.presence_of_element_located(
                    (By.ID, "email"))
                )
except (TimeoutException):
    sys.exit("Error message - loading page")
pause()
print ("Connected to cardladder")

# s'identifier
driver.find_element_by_id("email").send_keys(email_address)
pause()
driver.find_element_by_id("password").send_keys(password)
pause()
#driver.find_element_by_id("login-submit").click()
button = driver.find_element_by_xpath('//button[@class="btn block"]').click()
pause()
#wait.until(EC.element_to_be_clickable(
#    (By.ID, "nav-typeahead-wormhole"))
#)
pause()
print ("logged in")

#Loop for website

link = open("cards_link_working.py").readlines()

with open("blank.csv", "w") as file:
    for x in link:
        driver.get(x)
        #Click load more sales button
        while True:
            #button_1 = driver.find_element_by_class_name('load-more btn secondary').click
            #button_1 = driver.find_element_by_xpath('//button[@class="load-more.btn.secondary"]').click()
            pause()
        time.sleep(5)
        get_div = driver.find_element_by_class_name('table-container').text
        print(get_div)
        #!!!!!NEED TO REPLACE X WITH THE CARD NAME!!!!!
        file.write(" %s \n %s\n " %(x, get_div)) #Reference: https://www.kite.com/python/answers/how-to-write-a-variable-to-a-file-in-python#:~:text=Use%20string%20formatting%20to%20write,Use%20file.
file.close()
    



"""
for element in get_div:
    print (element.text)
    print (element.tag_name)
    print (element.parent)
    print (element.location)
    print (element.size)
"""


