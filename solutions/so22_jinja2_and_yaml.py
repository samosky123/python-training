#!/usr/bin/env python
import yaml
import jinja2

j2_template = """
{% for interface in switch_config.interfaces -%}
interface {{interface.name}}
  description {{interface.description}}
  ip address {{interface.ip}}/{{interface.prefix}}
{% endfor %}
"""

settings = """
switch_config:
     interfaces:
           - name: et10
             description: infrastructure link
             ip: 192.168.100.250
             prefix: 24
           - name: et11
             description: infrastructure link
             ip: 192.168.101.250
             prefix: 24
"""

template = jinja2.Template(j2_template)

print yaml.load(settings)

output = template.render(yaml.load(settings))

print output
