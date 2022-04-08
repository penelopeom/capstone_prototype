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

    # creating driver
    owner = whois_script.whois_func(address)
    driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

    
    # parsing together search query
    location = geolocation_script.geolocation_func(address)
    location.split(' ')
    state = set(location) & set(us_states)
    profile_url = getURL(owner, state)

    # this will open the link
    driver.get(profile_url)

    # scrolling to the bottom
    start = time.time()
    initial_scroll = 0
    final_scroll = 1000
    pause_time = 3
    scroll_time = 20

    while True:
        driver.execute_script(f"window.scrollTo({initial_scroll}, {final_scroll}")
        initial_scroll = final_scroll
        finalScroll += 1000

        # stop so data can load
        time.sleep(pause_time)
        end = time.time()

        # scroll for scroll time
        if round(end - start) > scroll_time:
            break

    # getting page source to parse
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')

    # finding overview section
    overview = soup.find('div', {'id': 'ember53','class': 'ember-view'})

    web_loc = overview.findAll('a')
    website = web_loc.get_text()

    driver.get(website)

    while True:
        driver.execute_script(f"window.scrollTo({initial_scroll}, {final_scroll}")
        initial_scroll = final_scroll
        finalScroll += 1000

        # stop so data can load
        time.sleep(pause_time)
        end = time.time()

        # scroll for scroll time
        if round(end - start) > scroll_time:
            break

    src = driver.page_source
    contact = soup.find('a')



    def getURL(companyName, State):
        try:
            term = ' '.join([companyName, State, "LinkedIn"])
            for url in search(term, num_results=1):
                return url
        except:
            return ''
        
