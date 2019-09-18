import yaml
import jinja2

output_file = 'config_file.txt'

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

settings_dict = yaml.load(settings, Loader=yaml.FullLoader)

print('Loaded YAML Settings:\n', settings_dict)

output = template.render(settings_dict)

print('Rendered Config:\n', output)

print('Saving Config in file {0}.'.format(output_file))

with open(output_file, 'w') as ofile:

    ofile.write(output)

# Exercise:
# Create new Jinja2 template to configure Interface description and IP address with mask or prefix
# Load parameters from YAML file into Jinja2 to generate desired configuration
