def generate_next_ip(subnet):
    subnet_split = subnet.split('.')
    if len(subnet_split) != 4:
        return ["Invalid IP address format"]

    try:
        subnet_split[2] = str(int(subnet_split[2]) + 1)
        next_ip = '.'.join(subnet_split)

        return next_ip

    except ValueError:
        return ["Invalid IP address format"]

vlan_total = {}  # Create an empty dictionary for storing the VLAN and its corresponding IPs

start_vlan = int(input("Enter the starting VLAN number: "))
end_vlan = int(input("Enter the ending VLAN number: "))
subnet = input(f"Enter the initial subnet (e.g., '10.1.1.0'): ")

while start_vlan <= end_vlan:
    vlan = str(start_vlan)
    next_ip = subnet
    result = generate_next_ip(next_ip)

    if "Invalid IP address format" in result:
        print("Invalid IP address format")
        break
    else:
        vlan_total[vlan] = next_ip
        start_vlan += 1
        subnet = result  # Update the subnet for the next VLAN

print("VLAN Total Dictionary:")
print(vlan_total)
