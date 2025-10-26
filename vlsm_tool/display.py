from typing import List, Dict
from .models import SubnetAllocation

def display_allocation_table(allocations: List[SubnetAllocation], summary: Dict, network_prefixlen: int):
    
    header = f"{'departamento':<15} | {'hosts':<5} | {'rede_ID':<15} | {'mascara':<20} | {'faixa_util':<33} | {'broadcast':<15}"
    
    print("-" * len(header))
    print(header)
    print("-" * len(header))
    
    if not allocations:
        return

    for alloc in allocations:
        print(f"{alloc.department_name:<15} | {alloc.required_hosts:<5} | {str(alloc.network_id):<15} | {alloc.subnet_mask:<20} | {alloc.usable_range:<33} | {str(alloc.broadcast_address):<15}")
    
    print("-" * len(header))
    print(f"Total de IPs da Rede Principal (/{network_prefixlen}): {summary['main_network_size']}")
    print(f"Total de IPs Alocados: {summary['allocated_ips']}")
    print(f"Total de IPs Restantes: {summary['remaining_ips']} (A partir de {summary['next_available_ip']})")