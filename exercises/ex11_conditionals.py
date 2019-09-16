# Ex.11
#

vlans = [90, 100, 101, 102, 103]

for vlan in vlans:
    if vlan > 100:
        print("VLAN", vlan, "is greater than 100")
    elif vlan < 100:
        print("VLAN", vlan, "is less than 100")
    else:
        print("VLAN", vlan, "is 100")
#
for vlan in vlans:
    if vlan > 100 and vlan % 2 == 0:
        print("VLAN", vlan, "is greater than 100 and even")
#
for vlan in vlans:
   if vlan % 2:
       print("VLAN", vlan, "is odd")
#
for vlan in vlans:
   if not vlan % 2:
       print("VLAN", vlan, "is even")
#
idx = 0
while idx < 3:
    print("index:", idx, "vlan:", vlans[idx])
    idx += 1

#
