import os
from pip._internal import main
main(['install', 'ipwhois'])
from ipwhois import IPWhois

def whois_func(address):
    IPaddress = address.strip()
    search = IPWhois(IPaddress)
    res = search.lookup_whois()
    if (res != ""):
        address = res["nets"][0]['address']
        city = res["nets"][0]['city']
        country = res["nets"][0]['country']
        username = res["nets"][0]['name']
        
        fullAddr = address + ", " + city + ", " + country
        return username + ", " + fullAddr

    return "NO RESULTS FOUND"