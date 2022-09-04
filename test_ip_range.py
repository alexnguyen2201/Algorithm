import ipaddress
ip_range = [str(ip) for ip in ipaddress.IPv4Network('1.52.0.0/22')]
print(ip_range[0])
print(ip_range[-1])
