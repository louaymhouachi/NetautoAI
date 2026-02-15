import ipaddress
import random

def generate_networks(main_network, vlans):
    networks = {}
    vlan_ids = list(range(10,200,10))
    random.shuffle(vlan_ids)
    
    main_net = ipaddress.ip_network(main_network)
    subnets = list(main_net.subnets(new_prefix=24))
    for i, vlan in enumerate(vlans):
        subnet = subnets[i]
        hosts = list(subnet.hosts())
        
        networks[vlan["name"]] = {
            "vlan_id": vlan_ids[i],
            "network": str(subnet),
            "gateway": str(hosts[0])
        }
        return networks       
    
    
