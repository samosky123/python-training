import yaml
import jinja2
import sys
from pprint import pprint

with open("vars/arista.yaml") as fyaml:
    yaml_vars_string = fyaml.read()

yaml_vars = yaml.load(yaml_vars_string, Loader=yaml.FullLoader)

with open("templates/arista.j2") as fj2:
    j2_template_string = fj2.read()

j2_template = jinja2.Template(j2_template_string)

config = j2_template.render(yaml_vars)

with open("configs/arista-conf", "w") as fconf:
    fconf.writelines(config)

print("Configuration rendered")
