import os
from pip._internal import main
import socket
from datetime import datetime as dt
import time

def whois_func(address):
    addresses = address.split("\r\n")
    result =""

    for ip in addresses:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("whois.arin.net", 43))
        s.send(('n ' + ip + '\r\n').encode())

        response = b""

        # setting time limit in seconds
        startTime = time.mktime(dt.now().timetuple())
        timeLimit = 3
        while True:
            elapsedTime = time.mktime(dt.now().timetuple()) - startTime
            data = s.recv(4096)
            response += data
            if (not data) or (elapsedTime >= timeLimit):
                break

        if (response.decode() != ""):
            result += response.decode() + ";"
        else:
            result += "NO RESULT FOUND; "
    
    
    sheesh = """#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2022, American Registry for Internet Numbers, Ltd.
#"""

    while(result.find(sheesh) != -1):
        result = result.replace(sheesh, "")

    replace = result[result.find("AT&T"):]
    replace = replace[:replace.find("\n")]

    while(result.find("AT&T") != -1):
        result = result.replace(replace, "")
        replace = result[result.find("AT&T"):]
        replace = replace[:replace.find("\n")]

    while(result.find("\n\n") != -1):
        result = result.replace("\n\n", "\n")

    
    s.close()
    return result.strip()