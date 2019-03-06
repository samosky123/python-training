import cobra.mit.access
import cobra.mit.session
import cobra.mit.request
import cobra.model.fabric
import cobra.model.infra
import cobra.model.pol
import cobra.model.fv
import cobra.model.cdp
import cobra.model.fvns
import cobra.model.phys
import requests
import sys
import yaml
import getpass
from requests.packages.urllib3.exceptions import InsecureRequestWarning, InsecurePlatformWarning, SNIMissingWarning


def apic_connect(apic_uri, apic_user, apic_password):
    apic_connected = False
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
        requests.packages.urllib3.disable_warnings(SNIMissingWarning)
        ls = cobra.mit.session.LoginSession('https://' + apic_uri, apic_user, apic_password)
        md = cobra.mit.access.MoDirectory(ls)
        md.login()
        apic_connected = True
    except:
        pass

    if not apic_connected:
        return [1, 'ERROR: Failed to connect to APIC \n']
    else:
        return [0, md]


def tn(md, task):

    try:
        tn_name = task['vars']['tn_name']
        op = task['tn']
    except:
        return [1, 'ERROR: Missing variables']

    print 'Processing task: ', task['name']

    topMo = cobra.model.pol.Uni('')

    # build the request using cobra syntax
    fvTenant = cobra.model.fv.Tenant(topMo, name=tn_name)
    cobra.model.fv.RsTenantMonPol(fvTenant, tnMonEPGPolName=u'default')

    if op == 'delete':
        fvTenant.delete()
        print 'Deleting Tenant', tn_name
    elif op == 'add':
        print 'Adding Tenant', tn_name
    else:
        return [1, 'ERROR: Valid operations add or delete.']

    c = cobra.mit.request.ConfigRequest()
    c.addMo(fvTenant)
    response = md.commit(c)

    if response.status_code == 200:
        return [0, 'Result: OK']
    else:
        return [1, 'Result: ' + response]


def vrf(md, task):

    try:
        tn_name = task['vars']['tn_name']
        vrf_name = task['vars']['vrf_name']
        op = task['vrf']
    except:
        return [1, 'ERROR: Missing variables']

    print 'Processing task: ', task['name']

    polUni = cobra.model.pol.Uni('')
    fvTenant = cobra.model.fv.Tenant(polUni, tn_name)

    fvCtx = cobra.model.fv.Ctx(fvTenant, name=vrf_name)
    cobra.model.fv.RsCtxToEpRet(fvCtx, tnFvEpRetPolName=u'default')
    cobra.model.fv.RsCtxMonPol(fvCtx, tnMonEPGPolName=u'default')

    if op == 'delete':
        fvCtx.delete()
        print 'Deleting VRF', vrf_name
    elif op == 'add':
        print 'Adding VRF', vrf_name
    else:
        return [1, 'ERROR: Valid operations add or delete.']

    c = cobra.mit.request.ConfigRequest()
    c.addMo(fvCtx)
    response = md.commit(c)

    if response.status_code == 200:
        return [0, 'Result: OK']
    else:
        return [1, 'Result: ' + response]


def bd(md, task):
    try:
        tn_name = task['vars']['tn_name']
        vrf_name = task['vars']['vrf_name']
        bd_name = task['vars']['bd_name']
        op = task['bd']
    except:
        return [1, 'ERROR: Missing variables']

    print 'Processing task: ', task['name']

    polUni = cobra.model.pol.Uni('')
    fvTenant = cobra.model.fv.Tenant(polUni, tn_name)
    fvCtx = cobra.model.fv.Ctx(fvTenant, vrf_name)
    fvBD = cobra.model.fv.BD(fvTenant, bd_name)
    cobra.model.fv.RsCtx(fvBD, tnFvCtxName=fvCtx.name)

    if op == 'delete':
        fvBD.delete()
        print 'Deleting BD', bd_name
    elif op == 'add':
        print 'Adding BD', bd_name
    else:
        return [1, 'ERROR: Valid operations add or delete.']

    c = cobra.mit.request.ConfigRequest()
    c.addMo(fvBD)
    response = md.commit(c)

    if response.status_code == 200:
        return [0, 'Result: OK']
    else:
        return [1, 'Result: ' + response]


def ap(md, task):

    try:
        tn_name = task['vars']['tn_name']
        ap_name = task['vars']['ap_name']
        op = task['ap']
    except:
        return [1, 'ERROR: Missing variables']

    print 'Processing task: ', task['name']

    polUni = cobra.model.pol.Uni('')
    fvTenant = cobra.model.fv.Tenant(polUni, tn_name)
    fvAp = cobra.model.fv.Ap(fvTenant, name=ap_name)

    if op == 'delete':
        fvAp.delete()
        print 'Deleting AP Profile', ap_name
    elif op == 'add':
        print 'Adding AP Profile', ap_name
    else:
        return [1, 'ERROR: Valid operations add or delete.']
    c = cobra.mit.request.ConfigRequest()
    c.addMo(fvAp)
    response = md.commit(c)

    if response.status_code == 200:
        return [0, 'Result: OK']
    else:
        return [1, 'Result: ' + response]


def epg(md, task):

    try:
        tn_name = task['vars']['tn_name']
        ap_name = task['vars']['ap_name']
        epg_name = task['vars']['epg_name']
        bd_name = task['vars']['bd_name']
        pd_name = task['vars']['pd_name']
        op = task['epg']
    except Exception as error:
        print str(error)
        return [1, 'ERROR: Missing variables']

    print 'Processing task: ', task['name']

    polUni = cobra.model.pol.Uni('')
    fvTenant = cobra.model.fv.Tenant(polUni, tn_name)
    fvBD = cobra.model.fv.BD(fvTenant, bd_name)
    fvAp = cobra.model.fv.Ap(fvTenant, ap_name)
    fvAEPg = cobra.model.fv.AEPg(fvAp, epg_name)

    cobra.model.fv.RsBd(fvAEPg, tnFvBDName=fvBD.name)
    cobra.model.fv.RsDomAtt(fvAEPg,  tDn='uni/phys-{}'.format(pd_name))

    if op == 'delete':
        fvAEPg.delete()
        print 'Deleting EPG', epg_name
    elif op == 'add':
        print 'Adding EPG', epg_name
    else:
        return [1, 'ERROR: Valid operations add or delete.']

    c = cobra.mit.request.ConfigRequest()
    c.addMo(fvAEPg)
    response = md.commit(c)

    if response.status_code == 200:
        return [1, 'Status: OK']
    else:
        return [1, 'Result: ' + response]


def main():
    try:
        yaml_file = open('aci_with_epg.yaml', 'r')

    except Exception as error:
        print 'ERROR: ' + str(error)
        sys.exit(1)

    try:
        config = yaml.load(yaml_file)
    except Exception as error:
        print 'ERROR: ' + str(error)
        sys.exit(1)

    yaml_file.close()

    if 'apic' in config:
        apic_uri = config['apic']
    else:
        print 'ERROR: APIC address is missing in config file.'
        sys.exit(1)

    if 'tasks' in config:

        apic_user = raw_input('Enter APIC username: ')
        apic_password = getpass.getpass('Enter password: ')
        resp = apic_connect(apic_uri, apic_user, apic_password)
        if resp[0] == 0:
            md = resp[1]

            for task in config['tasks']:

                if 'tn' in task:
                    result = tn(md, task)
                    print result[1]
                elif 'ap' in task:
                    result = ap(md, task)
                    print result[1]
                elif 'vrf' in task:
                    result = vrf(md, task)
                    print result[1]
                elif 'bd' in task:
                    result = bd(md, task)
                    print result[1]
                elif 'epg' in task:
                    result = epg(md, task)
                    print result[1]

            md.logout()

        else:
            print 'ERROR: Failed to connect to APIC', apic_uri
    else:
        print 'ERROR: No tasks in a config file.'
        sys.exit(1)

if __name__ == '__main__':
    main()
