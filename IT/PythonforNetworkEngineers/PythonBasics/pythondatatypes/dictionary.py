# dictionary
i = 1
london = {'name': 'london1', 'location': 'london str','vendor':'cisco'}
london1 = {
    'id':1,
    'name':'london',
    'it_vlan':320,
    'user_vlan':5,
    'to_name':None,
    'port':'646/45/1'
}

print(f"{i}:", london['name']);i+=1
london['name'] = 'londen'
print(f"{i}:", london['name']);i+=1

london2 = {
    'user1':{
        'name': 'log',
        'location': '45 wood st'
    },
    'user2':{
        'name': 'bog',
        'location': '546 oak st'
    }
}

print(f"{i}:", london2['user1']['name']);i+=1
print(f"{i}:", sorted(london));i+=1

print('dictionary methods')
london.clear()
print(f"{i}:", london);i+=1

london = {'name': 'london1', 'location': 'london str','vendor':'cisco'}
londoncopy = london
print(f"{i}:", id(london), id(londoncopy));i+=1

london['name'] = 'bug'
print(f"{i}:", londoncopy);i+=1

londoncopy = london.copy()
london['name'] = 'megatron'
print(f"{i}:", id(london), id(londoncopy));i+=1
print(f"{i}:", londoncopy);i+=1
print(f"{i}:", london);i+=1

# london['ip'] -> error

print(f"{i}:", london.get('ip'));i+=1
print(f"{i}:", london.get('ip','not here'));i+=1

print(f"{i}:", london.setdefault('ip'));i+=1
print(f"{i}:", london.setdefault('name'));i+=1
print(f"{i}:", london.setdefault('device','linus'));i+=1
print(f"{i}:", london.setdefault('name','londin'));i+=1

print(f"{i}:", london);i+=1

keys = london.keys()

print(f"{i}:", keys);i+=1
print(f"{i}:", london.values());i+=1
print(f"{i}:", london.items());i+=1

london['os']='bugs'

print(f"{i}:", keys);i+=1

del london['os']
print(f"{i}:", london);i+=1

london.update({'vendor':'caveman','brand':'bubbles'})
print(f"{i}:", london);i+=1

print('dictionary creation')

r1 = {'model':'56','ver':'54.4'}
r2 = dict(model='478', ver='54.8')
r3 = dict([('model','234'),('ver','25.2')])
r4 = dict.fromkeys(['host','model','ip','ver'])
r5 = dict.fromkeys(['host','model','ip','ver'],0)
print(f"{i}:", r1);i+=1
print(f"{i}:", r2);i+=1
print(f"{i}:", r3);i+=1
print(f"{i}:", r4);i+=1
print(f"{i}:", r5);i+=1

routers = dict.fromkeys(['I54','h456','$42E'],[])
print(f"{i}:", routers);i+=1

routers['I54'].append('244564IEIO')
print(f"{i}:", routers);i+=1
