import xmltodict

xml_output = '''<?xml version="1.0" encoding="ISO-8859-1"?>
<nf:rpc-reply xmlns:nf="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="http://www.cisco.com/nxos:1.0:cdpd">
 <nf:data>
  <show>
   <cdp>
    <neighbors>
     <__XML__OPT_Cmd_show_cdp_neighbors_interface>
      <__XML__OPT_Cmd_show_cdp_neighbors___readonly__>
       <__readonly__>
        <TABLE_cdp_neighbor_brief_info>
         <ROW_cdp_neighbor_brief_info>
          <ifindex>436301824</ifindex>
          <device_id>ukdc2-c02(JAF1739AHHH)</device_id>
          <intf_id>Ethernet1/24</intf_id>
          <ttl>153</ttl>
          <capability>router</capability>
          <capability>switch</capability>
          <capability>IGMP_cnd_filtering</capability>
          <capability>Supports-STP-Dispute</capability>
          <platform_id>N7K-C7010</platform_id>
          <port_id>Ethernet7/9</port_id>
         </ROW_cdp_neighbor_brief_info>
         <ROW_cdp_neighbor_brief_info>
          <ifindex>436305920</ifindex>
          <device_id>ukdc2-c01(JAF1739APPP)</device_id>
          <intf_id>Ethernet1/25</intf_id>
          <ttl>173</ttl>
          <capability>router</capability>
          <capability>switch</capability>
          <capability>IGMP_cnd_filtering</capability>
          <capability>Supports-STP-Dispute</capability>
          <platform_id>N7K-C7010</platform_id>
          <port_id>Ethernet7/9</port_id>
         </ROW_cdp_neighbor_brief_info>
         <ROW_cdp_neighbor_brief_info>
          <ifindex>436318208</ifindex>
          <device_id>ukdc2-a02(SII172908G1)</device_id>
          <intf_id>Ethernet1/28</intf_id>
          <ttl>151</ttl>
          <capability>switch</capability>
          <capability>IGMP_cnd_filtering</capability>
          <capability>Supports-STP-Dispute</capability>
          <platform_id>N5K-C5548UP</platform_id>
          <port_id>Ethernet1/28</port_id>
         </ROW_cdp_neighbor_brief_info>
         <ROW_cdp_neighbor_brief_info>
          <ifindex>436322304</ifindex>
          <device_id>ukdc2-a02(SII172908G1)</device_id>
          <intf_id>Ethernet1/29</intf_id>
          <ttl>151</ttl>
          <capability>switch</capability>
          <capability>IGMP_cnd_filtering</capability>
          <capability>Supports-STP-Dispute</capability>
          <platform_id>N5K-C5548UP</platform_id>
          <port_id>Ethernet1/29</port_id>
         </ROW_cdp_neighbor_brief_info>
        </TABLE_cdp_neighbor_brief_info>
       </__readonly__>
      </__XML__OPT_Cmd_show_cdp_neighbors___readonly__>
     </__XML__OPT_Cmd_show_cdp_neighbors_interface>
    </neighbors>
   </cdp>
  </show>
 </nf:data>
</nf:rpc-reply>
'''


def cdp_xml_parser():
    xml_dict = xmltodict.parse(xml_output)

    cdp_nbr_list = xml_dict['nf:rpc-reply']['nf:data']['show']['cdp']['neighbors']\
        ['__XML__OPT_Cmd_show_cdp_neighbors_interface']['__XML__OPT_Cmd_show_cdp_neighbors___readonly__']\
        ['__readonly__']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info']

    # Print local interface, device_id, remote_interface

    template = '{0:15} | {1:15} | {2:15}'
    print template.format('Local Port', 'Neighbor', 'Remote Port')
    print ('----------------+-----------------+---------------')
    for cdp_nbr in cdp_nbr_list:
        print template.format(cdp_nbr['intf_id'], cdp_nbr['device_id'].split('(')[0], cdp_nbr['port_id'])


if __name__ == '__main__':
    cdp_xml_parser()
