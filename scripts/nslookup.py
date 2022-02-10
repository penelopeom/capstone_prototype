import socket

def nslookup_func(address):
    try:
        result_list = socket.gethostbyaddr(address)
        result = result_list[0]
    except:
        result = "Not Valid"
    return result