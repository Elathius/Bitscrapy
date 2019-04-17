
import urllib.request 
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import datetime
from time import sleep
import sys
#from forex_python.converter import CurrencyRates
#returning to ruby
import json, sys

#cei = CurrencyRates()




def peon():
    # instantiate a chrome options object so you can set the size and headless preference
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    '''


    #Setting user agent
    opts = Options()
    opts.add_argument("user-agent=whatever you want")
    '''


    chrome_driver = os.getcwd() +"\\chromedriver.exe"

    # go to Google and click the I'm Feeling Lucky button
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
 

    '''
    -----------------------------------------------------
    '''


    driver.get('https://bitoasis.net/en/')
    driver.save_screenshot('mybot.png') # save a screenshot to disk




    pgsrc = driver.page_source
    soup = BeautifulSoup(pgsrc,"html.parser")
    a = soup.findAll("span", {"class":"bitcoinBuyPrice"})
    a_a = a[0].text.strip()
    '''
    print (datetime.datetime.now())
    
    print (a_a)
    '''
    numericAED = a_a[:-4]
    return (numericAED)    


def main():
   
    myvar = peon()
    return myvar
    
json.dump(main(), sys.stdout)
