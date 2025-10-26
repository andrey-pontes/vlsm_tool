import ipaddress
from dataclasses import dataclass

@dataclass
class SubnetAllocation:
    
    department_name: str
    required_hosts: int
    network: ipaddress.IPv4Network
    
    @property
    def usable_range(self) -> str:

        if self.network.num_addresses <= 2:
            return "Nenhum"
        return f"{self.network.network_address + 1} - {self.network.broadcast_address - 1}"

    @property
    def subnet_mask(self) -> str:
        return f"/{self.network.prefixlen} ({self.network.netmask})"

    @property
    def broadcast_address(self) -> ipaddress.IPv4Address:
        return self.network.broadcast_address

    @property
    def network_id(self) -> ipaddress.IPv4Address:
        return self.network.network_address