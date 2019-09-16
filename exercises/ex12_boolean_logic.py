# Ex.12
# Some more booleans

vlans = ['', 90, 100, 101, 102, 103]
big_vlan = False
for vlan in vlans:
  if vlan:
    if vlan > 100:
        big_vlan = True
    if big_vlan:
        print("VLAN", vlan, "and we have seen a vlan > 100")
    else:
        print("VLAN", vlan, "and not yet seen a vlan > 100")
#

