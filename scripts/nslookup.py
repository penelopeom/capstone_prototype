import os

f = open("users.txt", "w")
f2 = open("IPaddresses.txt", "w")
f3 = open("njAddresses.txt", "w")
f4 = open("njOrganizations.txt", "w")
f5 = open("overview.txt", "w")

with open("fetch-unique.txt", "r") as a_file:
  for line in a_file:
    IPaddress = line.strip()
    search = "whois -h whois.arin.net " + IPaddress + " "
    username = os.popen(search + "| grep -i 'CustName:'").read()
    if (username != ""):
        print(IPaddress)
        print(username)
        overviewStr = IPaddress + "\n"
        username = str(username)
        username = username[15:]
        username = username.strip()
        
        overviewStr += "Owned by: " + username + "\n"
        
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
        overviewStr += fullAddr + "\n"
        if (state == "NJ"):
            f3.write(IPaddress + "\n")
        
        if ("NJ" in username):
            f4.write(IPaddress + "\n")
            overviewStr += "NJ organization \n"
            
        
        f.write(username + "\n")
        f2.write(str(IPaddress) + "\n")
        f5.write(overviewStr + "----------------------------------- \n")

f.close()
f2.close()
f3.close()
f4.close()
f5.close()
    