import socket

def nslookup_func(address):
    result =""

    try:
        result_list = socket.gethostbyaddr(address)
        result += result_list[0]
    except:
        result += "NO RESULTS FOUND"
    
    return result