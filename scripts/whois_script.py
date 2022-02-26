import os
from pip._internal import main
main(['install', 'ipwhois'])
from ipwhois import IPWhois

def whois_func(address):
    # if single IP, there will only be one element of the array after split
    # if multiple IPs, it will convert them into an array
    addresses = address.split("\r\n")
    result = ""

    for IPaddress in addresses:
        search = IPWhois(IPaddress)
        res = search.lookup_whois()
        if (res != ""):
            address = res["nets"][0]['address']
            city = res["nets"][0]['city']
            country = res["nets"][0]['country']
            username = res["nets"][0]['name']
            
            fullAddr = address + ", " + city + ", " + country
            result += username + ", " + fullAddr + ". ";
        else:
            result += "NO RESULTS FOUND"

    return result