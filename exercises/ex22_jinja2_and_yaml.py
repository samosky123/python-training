import yaml
import jinja2


jinja2_template = """
snmp-server community {{snmp.community}}
{% for host in snmp.hosts -%}
! snmp server {{host.name}}
snmp-server host {{host.ip}} version {{host.version}} {{host.community}}
{% endfor %}
"""

settings = """
snmp:
     community: public
     hosts:
           - name: ServerA
             ip: 1.1.1.1
             community: public
             version: 2c
           - name: ServerB
             ip: 2.2.2.2
             community: public
             version: 1
"""

template = jinja2.Template(jinja2_template)

settings_dict = yaml.load(settings, Loader=yaml.FullLoader)
print('Loaded YAML:', settings_dict)

output = template.render(settings_dict)

print('Rendered Config:\n', output)

# Exercise:
# Create new Jinja2 template to configure Interface description and IP address with mask or prefix
# Load parameters from YAML file into Jinja2 to generate desired configuration
