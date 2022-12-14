#!/usr/bin/env python
'''
Autogenerated code using arya
Original Object Document Input: 
{"fvAEPg":{"attributes":{"dn":"uni/tn-Scorp/ap-Web/epg-VL1003","name":"VL1003","rn":"epg-VL1003","status":"created"},"children":[{"fvRsBd":{"attributes":{"tnFvBDName":"Frankfurt_VRF","status":"created,modified"},"children":[]}}]}}

'''
raise RuntimeError('Please review the auto generated code before ' +
                    'executing the output. Some placeholders will ' +
                    'need to be changed')

# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.pol
from cobra.internal.codec.xmlcodec import toXMLStr

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession('https://10.106.1.51', 'admin', 'C1sc0123')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
polUni = cobra.model.pol.Uni('')
fvTenant = cobra.model.fv.Tenant(polUni, 'Scorp')
fvAp = cobra.model.fv.Ap(fvTenant, 'Web')

# build the request using cobra syntax
fvAEPg = cobra.model.fv.AEPg(fvAp, name=u'VL1004')
fvRsBd = cobra.model.fv.RsBd(fvAEPg, tnFvBDName=u'Frankfurt_VRF')


# commit the generated code to APIC
#print toXMLStr(fvAp)
print fvAP
c = cobra.mit.request.ConfigRequest()
c.addMo(fvAp)
md.commit(c)

