from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
from googlesearch import search
import time
import whois_script
import geolocation_script

# all us states 
us_states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Washington DC', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

def contact_func(address):
    # Creating an instance
    owner = whois_script.whois_func(address)
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

    # Logging into LinkedIn
    # driver.get("https://linkedin.com/uas/login")
    # time.sleep(5)

    # username = driver.find_element_by_id("username")
    # username.send_keys("boibevin@gmail.com") # Enter Your Email Address

    # pword = driver.find_element_by_id("password")
    # pword.send_keys("bevinboibevin")	 # Enter Your Password

    # driver.find_element_by_xpath("//button[@type='submit']").click()

    location = geolocation_script.geolocation_func(address)
    location.split(' ')

    state = set(location) & set(us_states)

    profile_url = getURL(owner, state)

    driver.get(profile_url)	 # this will open the link

def getURL(companyName, State):
    try:
        term = ' '.join([companyName, State, "LinkedIn"])
        for url in search(term, num_results=1):
            return url
    except:
        return ''
        
