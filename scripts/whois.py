import os

def whois(address):
    IPaddress = address.strip()
    search = "whois -h whois.arin.net " + IPaddress + " "
    username = os.popen(search + "| grep -i 'CustName:'").read()
    if (username != ""):
        print(IPaddress)
        print(username)
        username = str(username)
        username = username[15:]
        username = username.strip()
        
        response = str(os.popen(search).read())
        index = response.index("CustName:")
        customerInfo = response[index:index+300]
        
        addressIndex = customerInfo.index("Address:")
        cityIndex = customerInfo.index("City:")
        stateIndex = customerInfo.index("StateProv:")
        zipIndex = customerInfo.index("PostalCode:")
        countryIndex = customerInfo.index("Country:")
        
        address = (customerInfo[addressIndex:cityIndex])[16:]
        addressList = address.split("Address:")
        address = addressList[0].strip()
        city = (customerInfo[cityIndex:stateIndex])[16:]
        state = (customerInfo[stateIndex:zipIndex])[16:]
        postalCode = (customerInfo[zipIndex:countryIndex])[16:]
        country = (customerInfo[countryIndex:countryIndex+18])[-2:]
        
        address = address.strip()
        city = city.strip()
        state = state.strip()
        postalCode = postalCode.strip()
        country = country.strip()
        
        fullAddr = address + ", " + city + ", " + state + " " + postalCode + " " + country
        return username + ": " + fullAddr

    return "NO RESULTS FOUND"