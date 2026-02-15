import os
from jinja2 import Environment, FileSystemLoader

def build_configs(devices,networks):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base_dir,"..", "templates")
    
    env = Environment(loader=FileSystemLoader(template_dir))
    os.makedirs("generated_configs", exist_ok=True) 
    
    for device in devices:
        if device["type"] == "core":
            template = env.get_template("core.j2")
        else:
            template = env.get_template("access.j2") 
        config = template.render(
            device_name= device["name"],
            networks=networks
        )       
        with open(f"generated_configs/{device['name']}.cfg", "w") as f:
            f.write(config)