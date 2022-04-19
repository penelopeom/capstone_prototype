import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'bs4'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'googlesearch-python'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'lxml'])

# from pip._internal import main

# main(['install','bs4'])
# main(['install','requests'])
# main(['install','googlesearch-python'])

from bs4 import BeautifulSoup
import time
import requests
from googlesearch import search
import time
import whois_script
import geolocation_script

# all us states 
us_states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Washington DC', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

def getURL(companyName, State):
    try:
        term = ' '.join([companyName, State, "LinkedIn"])
        for url in search(term, num_results=1):
            return url
    except:
        return ''

def contact_func(address):

    # creating driver
    owner = whois_script.whois_func(address)
    owner = owner[:(owner.index("-"))]
    
    # parsing together search query
    location = geolocation_script.geolocation_func(address)
    location = location.replace(',', '').split(' ')
    state = (set(location) & set(us_states)).pop()

    profile_url = getURL(owner, state)
    

    # this will open the link
    src =  requests.get(profile_url).content

    

    # getting page source to parse
    soup = BeautifulSoup(src, 'lxml')

    # finding overview section
    overview = soup.find('span', {'  dir': 'ltr','class': 'link-without-visited-state'}).getText(strip=True)

    web_loc = overview.findAll('a')
    website = web_loc.get_text()

    src = requests.get(website).content
    contact = soup.findAll(text='contact')
    print(contact)
        
contact_func('12.106.168.50')

