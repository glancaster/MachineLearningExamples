
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}
access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

def task5_1():
    device = input('Enter name of device: ')
    return london_co[device]
def task5_1a():
    device = input('Enter name of device: ')
    parameter = input('Enter parameter name: ')
    return london_co[device][parameter]
def task5_1b():
    device = input('Enter name of device: ')
    parameterlist = ', '.join(list(london_co[device].keys()))
    parameter = input(f'Enter parameter name ({parameterlist}): ')
    return london_co[device][parameter] 
def task5_1c():
    device = input('Enter name of device: ')
    parameterlist = ', '.join(list(london_co[device].keys()))
    parameter = input(f'Enter parameter name ({parameterlist}): ')
    return london_co[device].get(parameter, "No such parameter")
def task5_1d():
    device = input('Enter name of device: ')
    parameterlist = ', '.join(list(london_co[device].keys()))
    parameter = input(f'Enter parameter name ({parameterlist}): ')
    return london_co[device].get(parameter.lower(), "No such parameter")
def task5_2():
    ipnetwork = input('Enter Ip Network and Mask: ')
    ip, mask = ipnetwork.split('/')
    ip = ip.split('.')
    bitmask = "1"*int(mask) + "0"*(32-int(mask))
    template = "Network:\n"
    template+= "{:10}{:10}{:10}{}\n".format(*ip)
    template+= f"{int(ip[0]):08b}  {int(ip[1]):08b}  {int(ip[2]):08b}  {int(ip[3]):08b}\n\n" 
    template+= "Mask:\n" + f"/{mask}\n" 
    template+= "{:<8}  {:<8}  {:<8}  {}\n".format(int(bitmask[:8],2),int(bitmask[8:16],2), int(bitmask[16:24],2), int(bitmask[24:],2))
    template+=  "{:8}  {:8}  {:8}  {:8}".format(bitmask[:8],bitmask[8:16], bitmask[16:24], bitmask[24:]) 
    
    print(template)
def task5_2a():
    ipnetwork = input('Enter Ip Network and Mask: ')
    ip, mask = ipnetwork.split('/')
    ip = ip.split('.')
    bin_ip = "{:08b}{:08b}{:08b}{:08b}".format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3]))[:-(32-int(mask))] + "0"*(32-int(mask))
    bitmask = "1"*int(mask) + "0"*(32-int(mask))
    template = "Network:\n"
    template+= "{:<10}{:<10}{:<10}{}\n".format(int(bin_ip[:8],2),int(bin_ip[8:16],2), int(bin_ip[16:24],2), int(bin_ip[24:],2))
    template+= "{:10}{:10}{:10}{}\n\n".format( bin_ip[:8] , bin_ip[8:16] ,  bin_ip[16:24] ,  bin_ip[24:] )
    template+= "Mask:\n" + f"/{mask}\n" 
    template+= "{:<8}  {:<8}  {:<8}  {}\n".format(int(bitmask[:8],2),int(bitmask[8:16],2), int(bitmask[16:24],2), int(bitmask[24:],2))
    template+=  "{:10}{:10}{:10}{}".format(bitmask[:8],bitmask[8:16], bitmask[16:24], bitmask[24:]) 

    print(template)
def task5_3():
    interfacemode = input('Enter interface mode (access/trunk): ')
    typeintnum = input('Enter type and interface number: ')
    vlannum = input('Enter number of vlan (vlans): ')
    template = {"access": access_template, "trunk": trunk_template}
    print(f"interface {typeintnum}")
    print("\n".join(template[interfacemode]).format(vlannum))
def task5_3a():
    interfacemode = input('Enter interface mode (access/trunk): ')
    typeintnum = input('Enter type and interface number: ')
    vlanout = {"access": "Enter VLAN number: ", "trunk": "Enter the allowed VLANs: "}
    vlannum = input(vlanout[interfacemode])
    template = {"access": access_template, "trunk": trunk_template}
    print(f"interface {typeintnum}")
    print("\n".join(template[interfacemode]).format(vlannum))



def test_51(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "r2") #mimic a single input
    assert task5_1() == {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    }
    
    monkeypatch.setattr('builtins.input', lambda _: "sw1")
    assert task5_1() == {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    }
def test_51a(monkeypatch):
    inputs = iter(['sw1', 'ios'])#mimic multiple inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert task5_1a() == "3.6.XE"
    
    inputs = iter(['r2', 'ip'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert task5_1a() == "10.255.0.2"
def test_51b(capsys,monkeypatch):
    # capsys is not capturing input() prompt
    
    inputs = iter(['sw1', 'ios'])#mimic multiple inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert task5_1b() == "3.6.XE"
    
    inputs = iter(['r2', 'ip'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert task5_1b() == "10.255.0.2" 
def test_51c(capsys,monkeypatch):
    
    # capsys is not capturing input() prompt but will captured print()
    
    inputs = iter(['sw1', 'ios'])#mimic multiple inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert task5_1c() == "3.6.XE"
    
    inputs = iter(['r2', 'ip'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert task5_1c() == "10.255.0.2"
    
    inputs = iter(['sw1', 'ips'])#mimic multiple inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert task5_1c() == "No such parameter"
def test_51d(capsys,monkeypatch):
    
    # capsys is not capturing input() prompt but will captured print()
    
    inputs = iter(['sw1', 'IOS'])#mimic multiple inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert task5_1d() == "3.6.XE"
    
    inputs = iter(['r2', 'Ip'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert task5_1d() == "10.255.0.2"
    
    inputs = iter(['sw1', 'ips'])#mimic multiple inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert task5_1d() == "No such parameter"
def test_52(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "10.5.5.0/24")
    task5_2()
    captured = capsys.readouterr()
    
    assert captured.out == (
        "Network:\n"
        "10        5         5         0\n"
        "00001010  00000101  00000101  00000000\n\n"
        "Mask:\n"
        "/24\n"
        "255       255       255       0\n"
        "11111111  11111111  11111111  00000000\n"
    )
def test_52a(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "10.5.5.0/24")
    task5_2a()
    captured = capsys.readouterr()
    
    assert captured.out == (
        "Network:\n"
        "10        5         5         0\n"
        "00001010  00000101  00000101  00000000\n\n"
        "Mask:\n"
        "/24\n"
        "255       255       255       0\n"
        "11111111  11111111  11111111  00000000\n"
    )
    monkeypatch.setattr('builtins.input', lambda _: "10.1.1.193/28")
    task5_2a()
    captured = capsys.readouterr()
    
    assert captured.out == (
        "Network:\n"
        "10        1         1         192\n"
        "00001010  00000001  00000001  11000000\n\n"
        "Mask:\n"
        "/28\n"
        "255       255       255       240\n"
        "11111111  11111111  11111111  11110000\n"
    )  
def test_53(capsys,monkeypatch):
    inputs = iter(["access", "Gi0/3", "55"])#mimic multiple inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    task5_3()
    captured = capsys.readouterr()
    assert captured.out == (
        "interface Gi0/3\n"
        "switchport mode access\n"
        "switchport access vlan 55\n"
        "switchport nonegotiate\n"
        "spanning-tree portfast\n"
        "spanning-tree bpduguard enable\n"
    )
    inputs = iter(["trunk", "Gi0/2", "10,11,12"])#mimic multiple inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    task5_3()
    captured = capsys.readouterr()
    assert captured.out == (
        "interface Gi0/2\n"
        "switchport trunk encapsulation dot1q\n"
        "switchport mode trunk\n"
        "switchport trunk allowed vlan 10,11,12\n"
    )
def test_53a(capsys,monkeypatch):
    # yet to find a good way to test prompt

    inputs = iter(["access", "Gi0/3", "55"])#mimic multiple inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    task5_3()
    captured = capsys.readouterr()
    assert captured.out == (
        "interface Gi0/3\n"
        "switchport mode access\n"
        "switchport access vlan 55\n"
        "switchport nonegotiate\n"
        "spanning-tree portfast\n"
        "spanning-tree bpduguard enable\n"
    )
    inputs = iter(["trunk", "Gi0/2", "10,11,12"])#mimic multiple inputs
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    task5_3()
    captured = capsys.readouterr()
    assert captured.out == (
        "interface Gi0/2\n"
        "switchport trunk encapsulation dot1q\n"
        "switchport mode trunk\n"
        "switchport trunk allowed vlan 10,11,12\n"
    )
