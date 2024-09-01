nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
mac = "AAAA:BBBB:CCCC"
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ip = "192.168.3.1"


def task4_1(nat: str) -> str :
    return nat.replace('Fast','Gigabit')
def task4_2(mac: str) -> str :
    return mac.replace(':','.')
def task4_3(config: str) -> list :
    return config.split()[-1].split(',')
def task4_4(vlans: list) -> list :
    return list(sorted(set(vlans)))
def task4_5(command1:str, command2:str) -> list:
    command1 = set(command1.split()[-1].split(','))
    command2 = set(command2.split()[-1].split(','))
    return sorted(list(command1.intersection(command2)))
def task4_6(ospf_route:str) -> str:
    prefix = ospf_route[ospf_route.find('10.'):ospf_route.find('/24')+3]
    ospf_route = ospf_route.replace(prefix,'')
    admetric = ospf_route[ospf_route.find('['):ospf_route.find(']')+1]
    ospf_route = ospf_route.replace(admetric,'')
    admetric = admetric.strip('[]')
    nexthop = ospf_route[ospf_route.find('10.'):ospf_route.find('.3')+2]
    ospf_route = ospf_route.replace(nexthop,'')
    lastupdate = ospf_route[ospf_route.find('3'):ospf_route.find('h')+1]
    outbound = ospf_route[ospf_route.find('Fast')::]

    return (
        f"{"Prefix":22}{prefix}\n"
        f"{"AD/Metric":22}{admetric}\n"
        f"{"Next-Hop":22}{nexthop}\n"
        f"{"Last update":22}{lastupdate}\n"
        f"{"Outbound Interface":22}{outbound}\n"
    )
def task4_7(mac: str) -> str :
    return "{:b}".format(int(mac.replace(':',''),16))
def task4_8(ip: str) -> str :
    ip = ip.split('.')
    return "{:10}{:10}{:10}{:10}\n".format( ip ) + f"{int(ip[0]):010b}{int(ip[1]):010b}{int(ip[2]):010b}{int(ip[3]):010b}" 


def test_():
    assert task4_1(nat) == "ip nat inside source list ACL interface GigabitEthernet0/1 overload"
    assert task4_2(mac) == "AAAA.BBBB.CCCC"
    assert task4_3(config) == ["1", "3", "10", "20", "30", "100"]
    assert task4_4(vlans) == [1, 2, 3, 4, 10, 20, 30, 100]
    assert task4_5(command1, command2) == ['1', '3', '8']
    assert task4_6(ospf_route) == (
        "Prefix                10.0.24.0/24\n"
        "AD/Metric             110/41\n"
        "Next-Hop              10.0.13.3\n"
        "Last update           3d18h\n"
        "Outbound Interface    FastEthernet0/0\n"
    )
    assert task4_7(mac) == "101010101010101010111011101110111100110011001100"
