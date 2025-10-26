import ipaddress
from typing import List, Dict, Optional, Tuple
from .models import SubnetAllocation

class VlsmAllocator:
    
    def __init__(self, main_network_str: str):
        try:
            self.main_network = ipaddress.ip_network(main_network_str)
            self.next_available_address = self.main_network.network_address
            self.allocations: List[SubnetAllocation] = []
            self.total_allocated_ips = 0

        except ValueError:
            raise
            
    def _calculate_prefix_length(self, required_hosts: int) -> int:
        
        required_addresses = required_hosts + 2
        host_bits = (required_addresses - 1).bit_length()
        
        return 32 - host_bits

    def _allocate(self, department_name: str, required_hosts: int) -> Optional[SubnetAllocation]:
        
        prefix_length = self._calculate_prefix_length(required_hosts)
        
        try:
            new_subnet = ipaddress.ip_network(f"{self.next_available_address}/{prefix_length}")
        except ValueError:
            return None

        if not self.main_network.supernet_of(new_subnet):
            return None

        allocation = SubnetAllocation(
            department_name=department_name,
            required_hosts=required_hosts,
            network=new_subnet
        )
        self.allocations.append(allocation)
        
        self.next_available_address = new_subnet.broadcast_address + 1
        self.total_allocated_ips += new_subnet.num_addresses
        
        return allocation

    def allocate_subnets(self, requirements: Dict[str, int]) -> List[SubnetAllocation]:

        sorted_requirements: List[Tuple[str, int]] = sorted(
            requirements.items(), 
            key=lambda item: item[1], 
            reverse=True
        )
        
        for name, hosts in sorted_requirements:
            if not self._allocate(name, hosts):
                break
                        
        return self.allocations

    def get_summary(self) -> Dict:
        
        remaining_ips = self.main_network.num_addresses - self.total_allocated_ips
        
        return {
            "main_network_size": self.main_network.num_addresses,
            "allocated_ips": self.total_allocated_ips,
            "remaining_ips": remaining_ips,
            "next_available_ip": self.next_available_address
        }