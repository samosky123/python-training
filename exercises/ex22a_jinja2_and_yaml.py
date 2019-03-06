import yaml
import jinja2


jinja2_template = """
{% for interface in interfaces -%}
interface {{interface['name'] }}
 no switchport
 ip ospf point-to-point
 description {{ interface['description'] }}
 ip address {{ interface['ip'] }} {{ interface['mask'] }}
 no shutdown
 exit
!
{% endfor %}
"""

settings = """
---
interfaces:
  - name: Ethernet2/1
    ip: 1.1.1.1
    mask: 255.255.255.0
    description: L3 Interface
  - name: Ethernet2/2
    ip: 2.2.2.2
    mask: 255.255.255.0
    description: L3 Interface 
"""

template = jinja2.Template(jinja2_template)

print yaml.load(settings)

output = template.render(yaml.load(settings))

print output

out_file = open('config_file.txt', 'w')

out_file.write(output)

out_file.close()

# Exercise:
# Create new Jinja2 template to configure Interface description and IP address with mask or prefix
# Load parameters from YAML file into Jinja2 to generate desired configuration
