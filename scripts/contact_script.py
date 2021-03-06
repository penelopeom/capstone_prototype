from bs4 import BeautifulSoup
import requests
from googlesearch import search
import whois_script
import geolocation_script
import re

# all us states 
us_states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'NewHampshire', 'NewJersey', 'NewMexico', 'NewYork', 'NorthCarolina', 'NorthDakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'RhodeIsland', 'SouthCarolina', 'SouthDakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'WestVirginia', 'Wisconsin', 'Wyoming']
us_states_with_spaces = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

def getURL(companyName, State):
    #try:
        term = ' '.join([companyName, State, "contact", "company"])
        print(term)
        urls=[]
        for url in search(term, num_results=5):
            print(url)
            urls.append(url)
        

        return(urls[0])

def getTenDigits(numbers):
    count = 0 
    digits = "1234567890"
    for num in numbers:
        for x in num:
            if x in digits:
                count+=1
        if count == 10:
            return num
        else:
            count = 0
    return "Unable to determine number."

def contact_func_solo(address):

    # creating driver
    owner = whois_script.whois_func(address)

    # parsing together search query
    location = geolocation_script.geolocation_func(address)
    location = location.replace(' ', '').split(',')
    state = (set(location) & set(us_states)).pop()
    state = us_states_with_spaces[us_states.index(state)]

    profile_url = getURL(owner, state)

    # this will open the link
    src =  requests.get(profile_url).text

    # getting page source to parse
    soup = BeautifulSoup(src, 'lxml')

    # finding overview section
    # https://stackoverflow.com/a/3868861/15164646
    match_phone = re.findall(r'((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))', src)

    contact = getTenDigits(match_phone)
    return contact + " - " + profile_url

def contact_func_all(address, whois, geolocation):

    # creating driver
    owner = whois

    # parsing together search query
    location = geolocation
    location = location.replace(' ', '').split(',')
    state = (set(location) & set(us_states)).pop()
    state = us_states_with_spaces[us_states.index(state)]

    profile_url = getURL(owner, state)

    # this will open the link
    src =  requests.get(profile_url).text

    # getting page source to parse
    soup = BeautifulSoup(src, 'lxml')

    # finding overview section
    # https://stackoverflow.com/a/3868861/15164646
    match_phone = re.findall(r'((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))', src)

    contact = getTenDigits(match_phone)
    return contact + " - " + profile_url
