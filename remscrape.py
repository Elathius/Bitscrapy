
import urllib.request 
from bs4 import BeautifulSoup 
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import os
import datetime
#returning to ruby
import json, sys
#func to extract int from str
def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))
def peasant():

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")

    chrome_driver = os.getcwd() +"\\chromedriver.exe"

    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
        

    driver.get('https://remitano.com/in')



    pgsrc = driver.page_source

    soup = BeautifulSoup(pgsrc,"html.parser")


    gold = pgsrc.find("{\"currency\":\"INR\",\"btc_bid\":")
    #print(gold)
    silver = pgsrc.find("btc_ask", gold)
    #print(silver)
    
    
    
    
    whatineed = pgsrc[silver+9:silver+25]
    #print(whatineed)
    whatineed = whatineed.partition('.')
    whatineed = whatineed[0]
    #whatineed = get_num(whatineed)
    return whatineed


def main():
   
    myvar = peasant()
    return myvar
    
json.dump(main(), sys.stdout)