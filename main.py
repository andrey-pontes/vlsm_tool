from vlsm_tool import VlsmAllocator, display_allocation_table

def run_allocator():

    main_network_cidr = "192.168.10.0/24"
    
    department_requirements = {
        "Administracao": 50,
        "Financeiro": 30,
        "Suporte": 14,
        "TI": 6
    }
    
    try:
        allocator = VlsmAllocator(main_network_cidr)
        final_allocations = allocator.allocate_subnets(department_requirements)
        allocation_summary = allocator.get_summary()
        
        display_allocation_table(
            final_allocations, 
            allocation_summary, 
            allocator.main_network.prefixlen
        )
        
    except Exception as e:
        print(f"\nErro: {e}")

if __name__ == "__main__":
    run_allocator()