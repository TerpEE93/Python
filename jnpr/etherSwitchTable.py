"""
etherSwitchTable.py
    Demo script to grab and print the Ethernet Switching Table
    from a Junos platform.  Emulates the functionality of
    "show ethernet switching-table" from Junos
"""

from jnpr.junos.factory import loadyaml
from os.path import splitext
_YAML_ = splitext(__file__)[0] + '.yml'
globals().update(loadyaml(_YAML_))

from pprint import pprint
from jnpr.junos import Device
from getCredentials import openWithCreds

dev1 = None

while dev1 == None:
    dev1 = openWithCreds()

print("Grabbing MAC address table...")
ethTbl = EtherSwitchTable(dev1)
ethTbl.get()

print("Closing connection to " + dev1.hostname + ".")
dev1.close()

print("\n\nMAC \tType \tVLAN \tAge \tInterface")

for entry in ethTbl:
    print(str(entry.address) + "\t" +
          str(entry.type) + "\t" +
          str(entry.vlan) + "\t" +
          str(entry.age) + "\t" +
          str(entry.interface))

print("\n\nThere you go!\n")
