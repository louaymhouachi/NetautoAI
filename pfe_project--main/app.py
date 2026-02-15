import json 
import os
import subprocess
from core.network_generator import generate_networks 
from core.config_builder import build_configs
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "architecture.json")

#============lire l'architecture =============
with open(file_path) as f:
    data = json.load(f)
#=============gnerer les réseaux =================
networks = generate_networks(
    data["main_network"],
    data["vlans"]
) 
#=========generer configs===============
build_configs(data["devices"],networks) 
print("configurations générées avec succès.") 
print("==========contenu des configs générées==========")
for device in data["devices"]:
    cfg_file = f"generated_configs/{device['name']}.cfg"
    print(f"\n---{device['name']}---")
    with open(cfg_file, "r") as f:
        print(f.read())

#=============lancer Ansible pour le deploiement=============
deploy = input("voulez_vous déployer la configuration ? (y/n):")

if deploy.lower() == "y":
    subprocess.run(["ansible-playbook", "-i", "ansible/inventory.yml", "ansible/playbook.yml"])
     
    
