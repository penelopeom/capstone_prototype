from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from googlesearch import search
import time
import whois_script

def contact_func(address):
    # Creating an instance
    ownwer = whois_script.whois_func(address)
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

    # Logging into LinkedIn
    # driver.get("https://linkedin.com/uas/login")
    # time.sleep(5)

    # username = driver.find_element_by_id("username")
    # username.send_keys("boibevin@gmail.com") # Enter Your Email Address

    # pword = driver.find_element_by_id("password")
    # pword.send_keys("bevinboibevin")	 # Enter Your Password

    # driver.find_element_by_xpath("//button[@type='submit']").click()

    # Opening Kunal's Profile
    # paste the URL of Kunal's profile here
    profile_url = getURL(owner)

    driver.get(profile_url)	 # this will open the link

def getURL(companyName, State):
    try:
        term = ' '.join([companyName, State, "LinkedIn"])
        for url in search(term, num_results=1):
            return url
    except:
        return ''
        
