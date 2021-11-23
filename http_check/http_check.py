import psutil
import socket
import urllib.request
from urllib.error import HTTPError, URLError

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)


def checkNginxRunning():
    '''
    Function check, if nginx present in processes on OS
    :return: True if nginx process exist and False if not
    '''
    for proc in psutil.process_iter():
        try:
            if "nginx" in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def checkNginxGet(adress):
    '''
    Function check, if nginx present in processes on OS
    :param adress: ip-adress for requst URL
    :return: True if OK or False if Error
    '''
    try:
        http_get = urllib.request.urlopen(f"http://{adress}/")
    except (HTTPError, URLError):
        return False
    return True


if checkNginxRunning():
    if checkNginxGet(local_ip):
        print(f'OK: Process Nginx is running and listen on {local_ip}:80')
    elif checkNginxGet("localhost"):
        print('Warning: Process Nginx is running, but listen loopback interface (127.0.0.1)')
else:
    print("Error: Nginx is not running on this host")
