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
import requests
from googlesearch import search
import whois_script
import geolocation_script
import re

# all us states 
us_states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'NewHampshire', 'NewJersey', 'NewMexico', 'NewYork', 'NorthCarolina', 'NorthDakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'RhodeIsland', 'SouthCarolina', 'SouthDakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'WestVirginia', 'Wisconsin', 'Wyoming']

def getURL(companyName, State):
    try:
        term = ' '.join([companyName, State, "contact", "company"])
        for url in search(term, num_results=1):
            return url
    except:
        return ''

def getTenDigits(numbers):
    digits = "0123456789"
    count = 0 
    for num in numbers:
        for x in num:
            if x in digits:
                count+=1
        if count == 10:
            return num
        else:
            count = 0
    return "no 10 digit nums"

def contact_func(address):

    # creating driver
    owner = whois_script.whois_func(address)
    ownerList = owner.split(" ")
    x = 0
    owner = ""
    while not("-" in ownerList[x]):
        owner += ownerList[x] + " "
        x += 1
    
    # parsing together search query
    location = geolocation_script.geolocation_func(address)
    location = location.replace(' ', '').split(',')
    state = (set(location) & set(us_states)).pop()

    profile_url = getURL(owner, state)

    # this will open the link
    src =  requests.get(profile_url).text

    # getting page source to parse
    soup = BeautifulSoup(src, 'lxml')

    # finding overview section
    # https://stackoverflow.com/a/3868861/15164646
    match_phone = re.findall(r'((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))', src)

    contact = getTenDigits(match_phone)
    return contact

