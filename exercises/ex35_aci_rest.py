import requests
import json
import pprint

APIC_ADDRESS = 'sandboxapicdc.cisco.com'

def aci_get_epg(s, headers, cookie):
    uri = 'https://{0}/api/class/fvAEPg.json?'.format(APIC_ADDRESS)
    response = s.get(uri, headers=headers, cookies=cookie, verify=False).json() 
    pprint.pprint(response)
    return

def aci_add_tenant(tn, descr, s, headers, cookie):

    uri = 'https://{0}/api/node/mo/uni/tn-{1}.json'.format(APIC_ADDRESS, tn)

    payload = {"fvTenant":
                   {"attributes":
                         {"name": tn, "descr": descr },
                    "children":[]
                   }
              }

    response = s.post(uri, data=json.dumps(payload), headers=headers, cookies=cookie, verify=False)
    print response
    return

def main():

    apic_user = 'admin'
    apic_password = 'ciscopsdt'
    
    headers = {'content-type': "application/json", 'cache-control': "no-cache"}
    
    uri = "https://{0}/api/aaaLogin.json".format(APIC_ADDRESS)
    
    payload = {'aaaUser': {'attributes': {'name': apic_user, 'pwd': apic_password}}}
    
    session = requests.Session()
    
    response = session.post(uri, data=json.dumps(payload), headers=headers, verify=False)
    
    cookie = {'APIC-cookie': response.cookies['APIC-cookie']}
   
    #aci_get_epg(session, headers, cookie)
    aci_add_tenant('Evolvere1', 'Evolvere1 Test Tenant', session, headers, cookie)
 
    session.close()


if __name__ == '__main__':
    main()
