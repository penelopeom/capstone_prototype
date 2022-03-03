import socket

def nslookup_func(address):
    addresses = address.split("\r\n")
    result =""

    for ip in addresses:
        try:
            result_list = socket.gethostbyaddr(ip)
            result += result_list[0] + "; "
        except:
            result += "NO RESULTS FOUND; "
    
    return result