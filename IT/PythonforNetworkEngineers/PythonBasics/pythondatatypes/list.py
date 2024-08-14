# list
i = 1

list1 = [10,20,30,15,45,1]
list2 = ['ten', 'two', 'hi']
list3 = [10,'ten',5.0]
print(f"{i}:", list1); i+=1
print(f"{i}:", list2); i+=1
print(f"{i}:", list3); i+=1

list4 = list('router')
print(f"{i}:", list4); i+=1

print(f"{i}:", list3[1]); i+=1
print(f"{i}:", list3[-1]); i+=1
print(f"{i}:", list3[1::]); i+=1
print(f"{i}:", list3[::-1]); i+=1

list1.reverse()
print(f"{i}:", list1); i+=1

list2[0] = 'one'
print(f"{i}:", list2); i+=1

nestedlist = [[1,2,3],['one','two','three']]
print(f"{i}:", nestedlist[0][1]); i+=1

print(f"{i}:", len(list3)); i+=1
print(f"{i}:", sorted(list1)); i+=1


print('list methods')

vlans = ['10', '20', '90']

print(f"{i}:", ','.join(vlans)); i+=1

vlans.append('189')

print(f"{i}:", vlans); i+=1

vlans1 = ['15','86','56']

vlans.extend(vlans1)
print(f"{i}:", vlans); i+=1
print(f"{i}:", vlans + vlans1); i+=1
print(f"{i}:", vlans.pop(-1)); i+=1

vlans.remove('189')
print(f"{i}:", vlans); i+=1

print(f"{i}:", vlans.index('15')); i+=1
vlans.insert(2,'485')
print(f"{i}:", vlans); i+=1

vlans2 = [2,4,8,1,6,5]
vlans2.sort()
print(f"{i}:", vlans2); i+=1



