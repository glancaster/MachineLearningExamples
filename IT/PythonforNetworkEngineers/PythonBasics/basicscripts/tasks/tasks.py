
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
    
    
    return [
        "Network:\n",
        "{:10}{:10}{:10}{:10}\n".format(ip),
        f"{int(ip[0]):10b}{int(ip[1]):10b}{int(ip[2]):10b}{int(ip[3]):10b}\n\n",
        "Mask:\n",
        f"/{mask}",
        "{:10}{:10}{:10}{:10}\n".format(int(bitmask[:8]),int(bitmask[8:16]), int(bitmask[16:24]), int(bitmask[24:])),
        "{:10}{:10}{:10}{:10}".format(bitmask[:8],bitmask[8:16], bitmask[16:24], bitmask[24:])
    ]

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
def test_52(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "10.5.5.0/24")
    assert task5_2() == [
        "Network:\n",
        "10        5         5         0\n",
        "00001010  00000101  00000101  00000000\n\n",
        "Mask:\n",
        "/24\n",
        "255       255       255       0\n",
        "11111111  11111111  11111111  00000000"
    ]
    


