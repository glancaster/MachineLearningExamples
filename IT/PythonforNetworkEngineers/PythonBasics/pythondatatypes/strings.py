print("1:", "Hello")
print("2:", 'Hello')

tunnel = """
interface tunnel
    ip address 10.10.10.1
    ip mtu 1485
"""

print("3:",tunnel)

intf = 'interface'
tun = 'tunnel0'

print("4:", intf+tun)
print("5:", intf+' '+tun)

print("6:", intf*5)
print("7:", '#'*10)

string1 = 'interface FastEthernet1/0'

print("8:", string1[0])
print("9:", string1[1])
print("10:", string1[-1])
print("11:", string1[0:9])
print("12:", string1[10:22])
print("13:", string1[10:])
print("14:", string1[-3:])

a = '0123456789'

print("15:", a[1::2])
print("16:", a[::2])
print("17:", a[::])
print("18:", a[::-1])

line = 'interface Gi0/1'

print("19:", len(line))


# String Methods
print('String Methods')

string2 = 'FastEthernet'

print("20:", string2.upper() )
print("21:", string2.lower() )
print("22:", string2.swapcase() )

string3 = 'tunnel 0'

print("23:", string3.capitalize() )

string4 = 'Hello, hello, hello, hello'

print("24:", string4.count("hello"))

string5 = 'interface FastEthernet0/1'
print("25:", string5.find('Fast') )
print("26:", string5[string5.find('Fast')::])

string6 = 'FastEthernet0/1'
print("27:", string6.startswith('Fast') )
print("28:", string6.startswith('fast') )
print("29:", string6.endswith('0/1') )
print("30:", string6.endswith('0/2') )

print("31:", string6.replace('Fast','Gigabit') )

string7 = '\n\tinterface FastEthernet0/1\n'
print("32:", string7.strip())
print("33:", "[1/2]".strip('[]'))

string8 = 'switchport trunk allowed vlan 10,20,30,100-200'
print("34:", string8.split())
print("35:", string8.split()[-1].split(','))


# String Formatting
print("String Formatting")

print("36:", 'eth{}'.format('1'))
print("37:", 'eth{}'.format(1))
print("38:", '{}'.format([10,25]))

vlan,mac,intf = ['100','aabb.cc80.7999','Gi0/1']

print("39:", '{:>15} {:>15} {:>15}'.format(vlan,mac,intf ))
print("40:", '{:15} {:15} {:15}'.format(vlan,mac,intf ))

template = """
IP Address:
{}"""

print("41:", template.format("10.11.1.1"))

print("42:", '{:.3f}'.format(10.0/3))

print("43:", '{:b} {:b} {:b} {:b}'.format(192,154,14,1))
print("44:", '{:8b} {:8b} {:8b} {:8b}'.format(192,154,14,1))
print("45:", '{:08b} {:08b} {:08b} {:08b}'.format(192,154,14,1))

print("46:", '{ip}/{mask}'.format(mask = 24, ip = '10.1.1.1'))
print("47:", '{1}/{0}'.format(24,'10.1.1.1'))

ip_template = '''
IP address:
{:<8} {:<8} {:<8} {:<8}
{:08b} {:08b} {:08b} {:08b}
'''
print("48:", ip_template.format(192,168,1,1,192,168,1,1))

ip_template_better = '''
IP address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print("49:", ip_template_better.format(192,168,1,1))

ip = '10.1.1.1'
mask = 24

print("50:", f"{ip}/{mask}")

oct1,oct2,oct3,oct4 = [10,1,1,1]

ip_template_better_fstring = f'''
IP address:
{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
{oct1:08b} {oct2:08b} {oct3:08b} {oct4:08b}
'''
print("51:", ip_template_better_fstring)

# Literal Strings
print("Literal Strings")

s = ("Hello" "World")
print("52:", s)
s1 = 'Hello' 'World'
print("53:", s1)

regex = (
    '(\S+) +(\S+) +' # interface and IP
    '\w+ +\w+ +'
    '(up|down|administratively down) +' # Status
    '(\w+)' # Protocol
)

longmessage = ('long message about {} \n'
               'which discusses {}')