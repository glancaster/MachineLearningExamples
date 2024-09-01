# method chaining

line = 'switchport trunk allowed vlan 10,20,30'
words = line.split()
vlans_str = words[-1]
vlans = vlans_str.split(',')

print(words)
print(vlans_str)
print(vlans)


# simplify the process and reduce temp variables

vlansbetter = line.split()[-1].split(',')

print(vlansbetter)

