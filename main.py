import ipaddress

def list_ips_in_cidr(cidr: str):
    network = ipaddress.ip_network(cidr)
    ip_list = [str(ip) for ip in network]
    return ip_list

def list_reserved_ips_in_aws_subnet(cidr: str):
    network = ipaddress.ip_network(cidr)
    ip_list = [str(ip) for ip in network]
    reserved_ip_list = set()
    reserved_ip_list.add(ip_list[0])
    reserved_ip_list.add(ip_list[1])
    reserved_ip_list.add(ip_list[2])
    reserved_ip_list.add(ip_list[3])
    reserved_ip_list.add(ip_list[-1])

    return reserved_ip_list

def main():
    every_ip = list_ips_in_cidr("192.168.1.0/24")
    reserved_ip_list = list_reserved_ips_in_aws_subnet("192.168.1.0/24")
    print(reserved_ip_list)
    if "192.168.1.0" in reserved_ip_list:
        print("True")
    else:
        print("False")

main()
