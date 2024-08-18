


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
    parameter = input(f'Enter parameter name ({', '.join(list(london_co[device].keys()))}): ')
    return london_co[device][parameter]







def test_51(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "r2")
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
    inputs = iter(['sw1', 'ios'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert task5_1a() == "3.6.XE"
    inputs = iter(['r2', 'ip'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert task5_1a() == "10.255.0.2"