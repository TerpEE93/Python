"""
getCredentials.py
    Reusable code to get host, username, and password info
    and then connect to a Junos device.
"""

from getpass import getpass
from IPy import IP
from jnpr.junos import Device
from jnpr.junos import exception as EzErrors

def openWithCreds():
    """
    Function that prompts user for host, username, and password info
    and then connects to a Junos device.

    Call as dev1 = openWithCreds().
    Returns an object of class Device.
    """
    hostCreds = {'host': None, 'user': None, 'password': None}

    hostCreds['host'] = getHost()
    hostCreds['user'] = getUser()
    hostCreds['password'] = getpass()

    dev = Device(host = hostCreds['host'],
                 user = hostCreds['user'],
                 password = hostCreds['password'])

    print("Opening connection to " + dev.hostname + " as " + dev.user +"...")
 
    try:
       dev.open()
    except EzErrors.ConnectAuthError:
        print ("Authorization error.  Check username and password")
    except EzErrors.ConnectRefusedError:
        print ("Connection refused.")
    except EzErrors.ConnectTimeoutError:
        print ("Connection timeout.")
    except:
        print ("Something went wrong...")
    else:
       return dev

    return None

"""
Support functions below
"""

def getHost():
    """
    Prompt user for host IP address, validate format, and return
    if the address is properly formatted.  Prompt the user to
    try again if not properly formatted.
    """
    host = None

    while host == None:
        ipHost = raw_input("IP address of host to connect: ")

        try:
            IP(ipHost)
        except:
            print("Invalid IP address.")
        else:
            host = ipHost

    return host

def getUser():
    return raw_input("Username: ")
