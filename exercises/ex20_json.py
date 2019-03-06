import json

# Example of JSON output for interface/VRF mapping
# Result is returned in two tables, related by Index (first in one, matches first in second, etc)

output_json = '''
{
  "TABLE_vrf": [
    {
      "ROW_vrf": {
        "vrf-name-out": "default"
      }
    },
    {
      "ROW_vrf": {
        "vrf-name-out": "default"
      }
    },
    {
      "ROW_vrf": {
        "vrf-name-out": "management"
      }
    },
    {
      "ROW_vrf": {
        "vrf-name-out": "evobot"
      }
    }
  ],
  "TABLE_intf": [
    {
      "ROW_intf": {
        "intf-name": "Lo0",
        "prefix": "172.16.17.1",
        "ip-disabled": "FALSE",
        "iod": 38,
        "proto-state": "up",
        "link-state": "up",
        "admin-state": "up"
      }
    },
    {
      "ROW_intf": {
        "intf-name": "Eth2/3",
        "prefix": "172.16.16.1",
        "ip-disabled": "FALSE",
        "iod": 41,
        "proto-state": "up",
        "link-state": "up",
        "admin-state": "up"
      }
    },
    {
      "ROW_intf": {
        "intf-name": "mgmt0",
        "prefix": "192.168.56.56",
        "ip-disabled": "FALSE",
        "iod": 4,
        "proto-state": "up",
        "link-state": "up",
        "admin-state": "up"
      }
    },
    {
      "ROW_intf": {
        "intf-name": "Vlan100",
        "prefix": "192.168.22.251",
        "ip-disabled": "FALSE",
        "iod": 2,
        "proto-state": "up",
        "link-state": "up",
        "admin-state": "up"
      }
    }
  ]
}
'''

intf_dict = json.loads(output_json)

# Print dictionary, loaded from JSON output
print 'Loaded Dictionary:', intf_dict

i = 0
for intf in intf_dict['TABLE_intf']:

    print 'Interface: ', intf['ROW_intf']['intf-name'], ',', 'VRF: ',\
        intf_dict['TABLE_vrf'][i]['ROW_vrf']['vrf-name-out']
    i += 1

# Exercise:
# 1. Process output as above
# 2. Merge data from two tables and output as JSON

