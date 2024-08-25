words = ['list','dict','tuple']

upper_words = []

for word in words:
    upper_words.append(word.upper())
print(upper_words)

for letter in 'string':
    print(letter)

for i in range(10):
    print('interface {}'.format(i))
    
vlans = [10,20,30,40,50]
for vlan in vlans:
    print('vlan {}'.format(vlan))
    print(' name VLAN_{}'.format(vlan))
    
r1 = {
        'ios':'14.5',
        'ip':"10.255.1.0",
        'hostname':"londonr1",
        'location':"24 new globe walk",
        'model':"4545"}
for k in r1:
    print(k)

for k in r1:
    print(k + '=>' + r1[k])

for key,item in r1.items():
    print(key + '=>' + item)

commands = ['switchport mode access', 'spanning-tree portfast']
fast_int = ['0/1','0/2','0/3']
for intf in fast_int:
    print('interface FastEthernet {}'.format(intf))
    for command in commands:
        print(' {}'.format(command))


access_template = ['switchport mode access',
                   'switchport access vlan',
                   'spanning-tree portfast',
                   'spanning-tree bpdugard enable']
access = {'0/12':10, '0/14':11, '0/16':17, '0/17':150}

# for intf,vlan in fast_int['access'].items():
#     print('interface FastEthernet' + intf)
#     for command in access_template:
#         if command.endswith('access vlan'):
#             print(' {} {}'.format(command,vlan))
#         else:
#             print(' {}'.format(command))
