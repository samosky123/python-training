import requests
import json
import sys
from pprint import pprint as pp

apic_user = 'admin'
apic_password = 'ciscopsdt'
headers = {'content-type': "application/json", 'cache-control': "no-cache"}
apic_address = 'https://sandboxapicdc.cisco.com'

login_uri = '{0}/api/aaaLogin.json'.format(apic_address)
payload = {'aaaUser': {'attributes': {'name': apic_user, 'pwd': apic_password}}}
#session = requests.Session()
response = requests.post(login_uri, data=json.dumps(payload), headers=headers, verify=False)

print('Login response code:', response.status_code)

cookie = {'APIC-cookie': response.cookies['APIC-cookie']}

#tn = 'pystud1'
#tenant_uri = '{0}/api/node/mo/uni.json'.format(apic_address, tn)
#descr = 'Python Training at very reasonable price'
#payload = {"fvTenant": {"attributes": {"dn":"uni/tn-"+tn, "name": tn, "descr": descr }, "children":[]}}
#
#response = requests.post(tenant_uri, data=json.dumps(payload), headers=headers, cookies=cookie, verify=False)
#print('Create Tenant response code:', response.status_code)
#print('Create Tenant response text:', response.text)


tenant_uri = '{0}/api/class/fvTenant.json'.format(apic_address)
response = requests.get(tenant_uri, headers=headers, cookies=cookie, verify=False)
#pp(response.json())


for tenant in response.json()['imdata']:
    name = tenant['fvTenant']['attributes']['name']
    print('Tenant name:', name)


